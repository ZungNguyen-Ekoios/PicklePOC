import datetime

from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import (
    DateTimeField,
    IntField,
    StringField,
    ObjectIdField,
)

connect(host="mongodb://localhost:27017/mydb", alias="my-db")

class Student(Document):
    _id = ObjectIdField()
    name = StringField()
    age = IntField()
    address = StringField()
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
    meta = {"db_alias": "my-db"}

    def __str__(self) -> str:
        return " [[ Id = " + str(self._id) + " | Name = " + self.name + " | Age = " + str(self.age) + " | Date = " + str(self.date_modified) + "]] "

def find_students(_name):
    students = Student.objects(name= _name)
    return students

def raise_exception(_name):
    student = Student.objects.get(name=_name)
    return student

def add_student():
    student = Student()
    student.name = "Nguyen"
    student.age = 20
    student.address = "Hanoi"
    student.save()
    return

if __name__ == "__main__":
    add_student()
