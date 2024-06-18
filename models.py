from pydantic import BaseModel, Field


class UserIn(BaseModel):
    first_name: str = Field(max_length = 32)
    last_name: str = Field(max_length = 32)
    email: str = Field(max_length = 128)
    password: str = Field(min_length = 8)
    
class User(UserIn):
    id: int

class ProductIn(BaseModel):
    name: str = Field(max_length = 32)
    description: str = Field(max_length = 512)
    price: int = Field()
    
class Product(ProductIn):
    id: int
    
class OrderIn(BaseModel):
    user_id: int = Field()
    product_id: int = Field()
    date: str = Field()
    status: bool = Field()
    
class Order(OrderIn):
    id: int
    