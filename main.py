import mongoengine
from pickle_tasks import udpate_student_using_pickle, test_exception
from json_tasks import udpate_student_using_json
from student import Student, find_students

def testPickleException():
    try:
        result = test_exception.apply_async(
            args=["ABC"], queue="pickle_queue", serializer="pickle"
        ).get()
        print("Test exception:", result)
    except mongoengine.errors.DoesNotExist as e:
        print(e, type(e))
    return

def testPickle():
    students = find_students(_name="Nguyen")
    print(type(students))
    result = udpate_student_using_pickle.apply_async(
        args=[students], queue="pickle_queue", serializer="pickle"
    ).get()
    print(" -----> ", result[0])
    return

def testJson():
    students = find_students(_name="Nguyen")
    result = udpate_student_using_json.apply_async(
        args=[students.to_json()], queue="json_queue"
    ).get()
    print(" -----> ", result)
    return

if __name__ == "__main__":
    testPickleException()
    # testPickle()
    # testJson()
