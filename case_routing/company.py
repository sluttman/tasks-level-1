from employee import *
class company:

    def __init__(self):
        self.employees = []
        self.backoffice_employees = []
        self.account_managers = []
        self.directors = []
        self.case_queue = []

    def add_employee(self, employee):
        self.employees.append(employee)
        if type(employee) == AccountManager:
            self.account_managers.append(employee)
        elif type(employee) == Director:
            self.directors.append(employee)
        elif type(employee) == BackofficeEmployee:
            self.backoffice_employees.append(employee)

    def get_employees(self):
        return self.employees
    
    def add_case_into_queue(self, case):
        self.case_queue.append(case)
        print("added case to queue")

    def get_case_from_queue(self):
        if self.case_queue != []:
            return self.case_queue.pop()
        return None