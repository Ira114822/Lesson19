
class Student:
    """class description of student"""

    def __init__(self, name, age, mark=4, alive=True):
        self._name = name
        self._age = age
        self._mark = mark
        self._alive = alive

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def del_age(self):
        del self._age

    def get_mark(self):
        return self._mark

    def set_mark(self, mark):
        self._mark = mark

    def get_alive(self):
        return self._alive

    def set_alive(self, alive):
        self._alive = alive

    def __str__(self):
        msg = self.name
        msg += (" is still alive "
    if self.alive else " is dead ")
        msg += "(mark: " + str(self.mark) + ")"

        return msg






class Killer():
    """class description of
  student killer """

    # study or die
    def kill(self, student, mark):
        if isinstance(student, Student):
            if student.alive and student.mark < mark:
                student.alive = False
                return True

        return False


