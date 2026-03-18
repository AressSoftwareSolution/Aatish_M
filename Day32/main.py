from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, BackgroundTasks, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI(title="Task Manager Demo")

# -----------------------
# Middleware: log all requests
# -----------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Completed response: {response.status_code}")
    return response

# -----------------------
# Enable CORS
# -----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# In-memory "database"
# -----------------------
tasks: List[dict] = []
task_id_counter = 1

# -----------------------
# Background task
# -----------------------
def notify_task_created(title: str):
    print(f"[Background Task] New task created: {title}")

# -----------------------
# WebSocket connections
# -----------------------
connections: List[WebSocket] = []

async def broadcast_message(message: str):
    disconnected = []
    for ws in connections:
        try:
            await ws.send_text(message)
        except:
            disconnected.append(ws)
    for ws in disconnected:
        connections.remove(ws)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    connections.append(ws)
    try:
        while True:
            data = await ws.receive_text()
            await ws.send_text(f"Server received: {data}")
    except WebSocketDisconnect:
        connections.remove(ws)

# -----------------------
# Templates
# -----------------------
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root():
    # Redirect root to dashboard
    return RedirectResponse(url="/dashboard")

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "tasks": tasks})

# -----------------------
# API endpoint to create tasks
# -----------------------
@app.post("/tasks")
async def create_task(title: str = Form(...), background_tasks: BackgroundTasks = None):
    global task_id_counter
    task = {"id": task_id_counter, "title": title, "status": "pending"}
    task_id_counter += 1
    tasks.append(task)

    # Background notification
    background_tasks.add_task(notify_task_created, title)

    # Broadcast to WebSocket clients
    await broadcast_message(f"New task created: {title}")

    return RedirectResponse("/dashboard", status_code=303)

# -----------------------
# API endpoint to update task status
# -----------------------
@app.post("/tasks/{task_id}/status")
async def update_task_status(task_id: int, status: str = Form(...)):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            await broadcast_message(f"Task updated: {task['title']} -> {status}")
            break
    return RedirectResponse("/dashboard", status_code=303)