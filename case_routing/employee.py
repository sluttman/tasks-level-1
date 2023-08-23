from company import *
class Employee:
    def __init__(self, id, company):
        self.status_free = True
        self.assigned_case = []
        self.employee_id = id
        self.company = company
        company.add_employee(self)

    def assign_case(self, case):
        if self.status_free:
            self.assigned_case.append(case)
            self.set_status_free(False)
            return True
        else:
            return False
         #if a employee has 1 case assigned he is not longer considered free for new cases
       
    def finish_case(self):
        finished_case = self.assigned_case.pop()
        self.set_status_free(True)
        print("finished case "+ str(finished_case.case_id))

    def set_status_free(self, available):
        self.status_free = available



class BackofficeEmployee(Employee):

    def __init__(self,id,company):
        super().__init__(id, company)


    def escalate_case(self):
        case_dispatched = False
        self.assigned_case[0].increment_case_level()
        for account_manager in self.company.account_managers:
            case_dispatched = account_manager.assign_case(self.assigned_case[0])
            if case_dispatched:
                print("Case was dispatched to Employee with the ID " + str(account_manager.employee_id))
                self.finish_case()
                return

        for director in self.company.directors:
            case_dispatched = director.assign_case(self.assigned_case[0])
            if case_dispatched:
                print("Case was dispatched to Employee with the ID " + str(director.employee_id))
                self.finish_case()
                return
            
        self.company.add_case_into_queue(self.assigned_case[0])
        self.finish_case()
        return
            

class AccountManager(Employee):
    def __init__(self, id, company):
        super().__init__(id, company)

    def escalate_case(self):
        case_dispatched = False
        self.assigned_case[0].increment_case_level()
        
        for director in self.company.directors:
            case_dispatched = director.assign_case(self.assigned_case[0])
            if case_dispatched:
                print("Case was dispatched to Employee with the ID " + str(director.employee_id))
                self.finish_case()
                return
            
        self.company.add_case_into_queue(self.assigned_case[0])
        self.finish_case()
        return

class Director(Employee):
    def __init__(self, id, company):
        super().__init__(id, company)

