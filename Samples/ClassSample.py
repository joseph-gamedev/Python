class Student:
    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num

class GameObject:
    def __init__(self, name, obj_id):
        self.name = name
        self.obj_id = obj_id

student = Student("Alice", 37)
print(student.name)
print(student.roll_num)

object = GameObject("Dummy", 1)
print(object.name)
print(object.obj_id)


