import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = str(uuid.uuid4())

people = [Person("Tom", "tom@email.com"),
          Person("Bob", "bob@email.com")
          ]


def find_person(id):
    for person in people:
        if person.id == id:
            return person
    return None


app = FastAPI()


@app.get("/")
async def main():
    return {'message': 'Hello'}


@app.get("/api/users")
def get_people():
    return people


@app.get("/api/users/{id}")
def get_person(id):
    person = find_person(id)
    print(person)
    if person is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}
        )
    return person


@app.post("/api/users")
def create_person(data=Body()):
    person = Person(data["name"], data["email"])
    # добавляем объект в список people
    people.append(person)
    return person


@app.put("/api/users")
def edit_person(data=Body()):
    person = find_person(data["id"])
    if person is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}
        )
    person.age = data["age"]
    person.name = data["name"]
    return person


@app.delete("/api/users/{id}")
def delete_person(id):
    person = find_person(id)
    if person is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}
        )
    people.remove(person)
    return person