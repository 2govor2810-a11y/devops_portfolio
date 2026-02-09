from fastapi import FastAPI, Body
import os
from typing import Optional
import os
from app import database
from app.database import SMeal, Meal

app = FastAPI()

#GET - вывод меню
@app.get("/check_menu")
def get_all_students():
    return {"message":database.check_menu()}
#POST - добавление блюда
@app.post("/add_meal")
def add_new_meal(meal : Meal):
    database.add_meal(meal)
    return {"message": "Meal was created",
            "meal": meal}
#PUT - обновлениe
@app.put("/update_meal")
def update_meal_by_id(filter:SMeal,upd_data:Meal):
    database.update_meal(filter,upd_data)
    return {"message": f"Meal {filter} was updated"}

@app.delete("/delete_meal")
def delete_meal(filter : SMeal):
    database.delete_meal_by_id(filter)
    return {"message": "Meal was deleted",
            "filter": filter}




