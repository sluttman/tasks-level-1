class company:
    
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees