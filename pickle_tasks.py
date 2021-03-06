import student  # We need to import student here. It seems useless but without it, we cannot call update function in line 16
import mongoengine
from student import Student, find_students, raise_exception
from celery import Celery

app = Celery(
    'pickle',
    broker='redis://localhost',
    backend='redis://localhost',
    task_serializer="pickle",
    accept_content=["pickle"],
    result_serializer="pickle",
)

@app.task
def udpate_student_using_pickle(students):
    # students is <class 'mongoengine.queryset.queryset.QuerySet'>
    print(type(students), students, len(students))
    students.update(age=(students[0].age + 1)) # We can call update function directly
    return students

@app.task
def test_exception(name):
    # students is <class 'mongoengine.queryset.queryset.QuerySet'>
    student = raise_exception(name)
    return student