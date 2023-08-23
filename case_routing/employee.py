class Employee:
    def __init__(self, id, company):
        self.status_free = True
        self.assigned_case = []
        self.employee_id = id
        self.company = company

        pass
    def assign_case(self, case):
        if len(self.assigned_case) == 0:
            self.assigned_case.append(case)
         #if a employee has 1 case assigned he is not longer considered free for new cases
       
    def finish_case(self, case_number):
        del self.assigned_case[case_number]
        self.status_free = True

class BackofficeEmployee(Employee):
    def __init__(self,id,company):
        super().__init__(id, company)


    def escalate_case(self):
        employees= self.company.get_employees()
        for employee in employees:
            if type(employee) == AccountManager and employee.status_free:
                employee.assign_case(self.assigned_case)
                del self.assigned_case[0]
                break
            

class AccountManager(Employee):
    def __init__(self, id, company):
        super().__init__(id, company)

    def escalate_case(self):
        employees= self.company.get_employees()
        for employee in employees:
            if type(employee) == Director and employee.status_free:
                employee.assign_case(self.assigned_case)
                del self.assigned_case[0]
                break

class Director(Employee):
    def __init__(self, id, company):
        super().__init__(id, company)

