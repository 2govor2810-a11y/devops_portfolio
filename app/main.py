from fastapi import FastAPI, responses
from . import database

app = FastAPI()

#корневая страница

@app.get("/",response_class=responses.HTMLResponse)
def main_page():
    return "<h1>ПРИВЕТ</h1>"
#GET - вывод меню
@app.get("/check_menu")
def get_all_students():
    return {"message":database.check_menu()}
#POST - добавление блюда
@app.post("/add_meal")
def add_new_meal(meal : database.Meal):
    database.add_meal(meal)
    return {"message": "Meal was created",
            "meal": meal}
#PUT - обновлениe
@app.put("/update_meal")
def update_meal_by_id(filter:database.SMeal,upd_data:database.Meal):
    database.update_meal(filter,upd_data)
    return {"message": f"Meal {filter} was updated"}

@app.delete("/delete_meal")
def delete_meal(filter : database.SMeal):
    database.delete_meal_by_id(filter)
    return {"message": "Meal was deleted",
            "filter": filter}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



