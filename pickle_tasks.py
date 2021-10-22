# import json
# import celeryconfig
import student
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
    students.update(age=(students[0].age + 1))
    return students