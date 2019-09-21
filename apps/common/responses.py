class StudentResponse:

    def __init__(self, data):
        pass

    @classmethod
    def students_entity(cls, src_object):
        print(src_object.__dict__)
        stud = dict()
        stud["name"] = src_object.name
        stud["sid"] = src_object.sid
        stud["gender"] = src_object.gender
        stud["course"] = src_object.course
        stud["year"] = src_object.year
        stud["address"] = src_object.address
        stud["mobile"] = src_object.mobile
        stud["email"] = src_object.email
        return stud

