class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._salary * 0.15


def display_employees(employees):
    for emp in employees:
        print(f"Role: {emp.get_role()}, Salary: {emp.get_salary()}")


staff = [Employee(50000), Manager(90000)]
display_employees(staff)
