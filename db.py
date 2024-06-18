import sqlalchemy
from sqlalchemy import create_engine
import databases as databases

from settings import settings

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata, sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True),
                         sqlalchemy.Column("first_name", sqlalchemy.String(32)), 
                         sqlalchemy.Column("last_name", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)), 
                         sqlalchemy.Column("password", sqlalchemy.String))

products = sqlalchemy.Table("products", metadata, sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)), 
                         sqlalchemy.Column("description", sqlalchemy.String(512)),
                         sqlalchemy.Column("price", sqlalchemy.DECIMAL))

orders = sqlalchemy.Table("orders", metadata, sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True),
                         sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key = False), 
                         sqlalchemy.Column("product_id", sqlalchemy.Integer, primary_key = False),
                         sqlalchemy.Column("date", sqlalchemy.Date),
                         sqlalchemy.Column("status", sqlalchemy.Boolean))

engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread" : False})                    

metadata.create_all(engine)
