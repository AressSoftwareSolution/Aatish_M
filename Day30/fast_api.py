from fastapi import FastAPI, HTTPException #Used to return errors from the API.
from pydantic import BaseModel # Pydantic is used for data validation.
from typing import List
from fastapi import FastAPI  # FastAPI is a Python framework used to build APIs quickly and efficiently.
from fastapi.middleware.cors import CORSMiddleware  # Allow requests from any website.

app = FastAPI() # This creates the main API application.

# We add middleware to the app.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow requests from any website.
    allow_credentials=True, # Allow cookies and authentication.
    allow_methods=["*"], # Allow all HTTP methods.
    allow_headers=["*"], # Allow all headers.
)

#This defines an API endpoint.
# Function that runs when user visits /.
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# -------- Pydantic Models --------

# Request Model
# Defines structure of incoming data.
class Product(BaseModel):
    name: str
    price: float
    quantity: int

# Response Model
# Defines structure of response returned by API.
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


# -------- Fake Database --------
# This is an in-memory database.
# It stores products temporarily.
products = []


# -------- Routes --------

# GET - Get all products
@app.get("/products", response_model=List[ProductResponse])
def get_products():
    return products


# GET - Get product by ID
@app.get("/products/{product_id}", response_model=ProductResponse)  #This ensures response matches:
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:  # Check matching product.
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# POST - Create product
# POST method is used to create new data.
@app.post("/products", response_model=ProductResponse)
def create_product(product: Product):
    product_id = len(products) + 1

    new_product = {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    }

    products.append(new_product)
    return new_product


# PUT - Update product
# PUT is used to update existing data.
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: Product):
    for p in products:
        if p["id"] == product_id:
            p["name"] = product.name
            p["price"] = product.price
            p["quantity"] = product.quantity
            return p
    raise HTTPException(status_code=404, detail="Product not found")


# DELETE - Delete product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

