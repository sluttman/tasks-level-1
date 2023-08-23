from company import *
from employee import *


class Case:
    def __init__(self, id):
        self.case_id = id
        self.case_level = 1
        # level 1 is all employees, level 2 is for account Managers and directors and level 3 is only for directors.

    def increment_case_level(self):
        self.case_level += 1


def dispatchCase(company, case):
    case_dispatched = False
    for employee in company.backoffice_employees:
        case_dispatched = employee.assign_case(case)
        if case_dispatched:
            print(
                "Case was dispatched to Employee with the ID "
                + str(employee.employee_id)
            )
            return

    for employee in company.account_managers:
        case_dispatched = employee.assign_case(case)
        if case_dispatched:
            print(
                "Case was dispatched to Employee with the ID "
                + str(employee.employee_id)
            )
            return

    for employee in company.directors:
        case_dispatched = employee.assign_case(case)
        if case_dispatched:
            print(
                "Case was dispatched to Employee with the ID "
                + str(employee.employee_id)
            )
            return
    company.add_case_into_queue(case)
    return


# This is just for testing purposes
def createCompany():
    example_company = company()

    Mike = BackofficeEmployee(1, example_company)
    Peter = BackofficeEmployee(2, example_company)
    Michelle = BackofficeEmployee(3, example_company)
    Sandra = BackofficeEmployee(4, example_company)

    Manager1 = AccountManager(5, example_company)
    Manager2 = AccountManager(6, example_company)
    Manager3 = AccountManager(7, example_company)

    Director1 = Director(8, example_company)

    return example_company


if __name__ == "__main__":
    example_company = createCompany()
    for i in range(1, 10):
        case = Case(i)
        a = dispatchCase(example_company, case)

    example_company.directors[0].finish_case()
    example_company.backoffice_employees[0].finish_case()
    example_company.account_managers[0].finish_case()
    example_company.backoffice_employees[1].escalate_case()
    example_company.account_managers[0].escalate_case()
    case = Case(10)
    a = dispatchCase(example_company, case)
