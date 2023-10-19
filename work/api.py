from asyncio import current_task
from operator import index
from turtle import pos, title
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException , Depends
from fastapi.params import Body
from passlib.context import CryptContext
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas,utils
from .database import engine, get_db
from .routers import post, user



models.Base.metadata.create_all(bind=engine)



app = FastAPI()




    
while True:

    try:
        conn = psycopg2.connect(host='localhost',
                             user='postgres',
                             password='olaoluwa99',
                             database='fastapi',
                             cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful")
        break
    except Exception as error:
         print("Connection to database failed")
         print("Error: ", error)
         time.sleep(3)



my_posts =[{"title": "title of post 1", "content": "content of post 1","id" : 1},
 {"title": "type of foods", "content": "i like pizza", "id": 2} ]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i 
    

 
app.include_router(post.router)
app.include_router(user.router)
























































#To hash(*) password on database for security purpose of passwords getting leasked we instsll 2 packages pip install passlib[bcrypt]