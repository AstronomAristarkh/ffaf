from fastapi import APIRouter, HTTPException

from db import users, database, products, orders
from models import User, UserIn, ProductIn, Product, OrderIn, Order


router = APIRouter()

@router.get("/users/", response_model = list[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)

@router.post("/users/")
async def creat_user(user: UserIn):
    query = users.insert().values(first_name = user.first_name, last_name = user.last_name, email = user.email)
    last_record_id = await database.execute(query)
    return {**user.dict, "id":last_record_id}

@router.get("/users/{user_id}", response_model = User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    result = await database.fetch_all(query)
    if result:
        return result
    raise HTTPException(status_code = 404, detail = "User not found")

@router.put("/users/{user_id}", response_model = list[User])
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict, "id":user_id}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message':'User deleted'}

@router.get("/products/", response_model = list[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)

@router.post("/products/")
async def creat_product(product: ProductIn):
    query = products.insert().values(name = product.name, description = product.description, price = product.price)
    last_record_id = await database.execute(query)
    return {**product.dict, "id":last_record_id}

@router.get("/products/{product_id}", response_model = Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    result = await database.fetch_all(query)
    if result:
        return result
    raise HTTPException(status_code = 404, detail = "Product not found")

@router.put("/products/{product_id}", response_model = list[Product])
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict, "id":product_id}

@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message':'Product deleted'}

@router.get("/orders/", response_model = list[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)

@router.post("/orders/")
async def creat_orders(order: OrderIn):
    query = orders.insert().values(user_id = order.user_id, product_id = order.product_id, date = order.date, status = order.status)
    last_record_id = await database.execute(query)
    return {**order.dict, "id":last_record_id}

@router.get("/orders/{order_id}", response_model = Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    result = await database.fetch_all(query)
    if result:
        return result
    raise HTTPException(status_code = 404, detail = "Order not found")

@router.put("/orders/{order_id}", response_model = list[Order])
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict, "id":order_id}

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message':'Order deleted'}

