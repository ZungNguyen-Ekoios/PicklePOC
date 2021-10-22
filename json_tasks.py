from celery import Celery

app = Celery(
    'json',
    broker='redis://localhost',
    backend='redis://localhost',
)
@app.task
def udpate_student_using_json(students):
    # students is string
    print(type(students), students)  # Cannot update directly like using pickle. We need to deserialize to Student mongo's object
    # student.update(age=student.age + 1) => raise Error
    return students