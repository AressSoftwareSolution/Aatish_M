

from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import get_db, engine, Base
from models import User
from auth import hash_password, verify_password, create_token, verify_token


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
async def register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if user:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "User already exists"}
        )

    new_user = User(
        email=email,
        hashed_password=hash_password(password)
    )

    db.add(new_user)
    await db.commit()

    return RedirectResponse("/login", status_code=303)


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "User not found"}
        )

    if not verify_password(password, user.hashed_password):
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Invalid password"}
        )

    token = create_token(email)

    response = RedirectResponse("/dashboard", status_code=303)

    response.set_cookie(key="token", value=token)

    return response


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    token = request.cookies.get("token")

    if not token:
        return RedirectResponse("/login")

    email = verify_token(token)

    if not email:
        return RedirectResponse("/login")

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "email": email
        }
    )

@app.get("/logout")
async def logout():

    response = RedirectResponse("/login")

    response.delete_cookie("token")

    return response