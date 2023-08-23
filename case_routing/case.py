from company import *
from employee import *
class Case:
    def __init__(self, id):
        self.case_id = id
        
class CaseDispatcher:

    def __init__(self):
        self.company = self.createCompany()


    def dispatchCase(self):
        generated_case= Case(1)
        employees_at_company = self.company.get_employees()
        for employee in employees_at_company:
            if employee.status_free and type(employee) == BackofficeEmployee:
                
                employee.assign_case(generated_case)
                print("assigned Case")
                break

    def createCompany(self):
        example_company = company()
        for i in range(0,20):
            print(str(i))
            if i <= 12:
                employee= BackofficeEmployee(i,example_company)
            elif i <= 17:
                employee= AccountManager(i,example_company)
            else:
                employee= Director(i,example_company)
            print(type(employee))
            example_company.add_employee(employee)
        return example_company
    
if __name__ == "__main__":
    example_company = CaseDispatcher()
    example_company.dispatchCase()

#