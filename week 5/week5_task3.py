class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def introduce(self):
        return f"Person: {self._name}, {self._age} years old"


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self._major = major

    def introduce(self):
        return f"Student: {self._name}, {self._age} years old, major {self._major}"


people = [Person("Alice", 30), Student("Bob", 20, "Cybersecurity")]

for p in people:
    print(p.introduce())
