class company:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
        print("added Employee")
    def get_employees(self):
        return self.employees