from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert, select, update, delete
from pydantic import BaseModel
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///DataBase.db')
metadata = MetaData()
sesion = Session()

class Meal(BaseModel):
    name:str
    recipe:str
class SMeal(BaseModel):
    id:int

Meals = Table(
    "Meals", metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String),
    Column("recipe",String)
)
metadata.create_all(engine)

def add_meal(meal):# функция записи в таблицу
     with engine.connect() as connection:
         insertSQL = insert(Meals).values(name=meal.name, recipe=meal.recipe)
         connection.execute(insertSQL)
         connection.commit()

def check_menu():#функция вывода меню
    with engine.connect() as connection:
        select_query = select(Meals)
        result = connection.execute(select_query)
        return str(result.fetchall())

def update_meal(filter:SMeal,upd_data:Meal):
    with engine.connect() as connection:
        dict_upd_data = upd_data.model_dump()
        update_query = update(Meals).where(Meals.c.id == filter.id).values(dict_upd_data)
        connection.execute(update_query)
        connection.commit()
        print("completed")

def delete_meal_by_id(filter:SMeal):
    with engine.connect() as connection:
        delete_query = delete(Meals).where(Meals.c.id == filter.id)
        connection.execute(delete_query)
        connection.commit()
        print("was deleted")



print(check_menu())