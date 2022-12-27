from utils.feachdata import Employee
from datetime import datetime

if __name__ == "__main__":
    print("name")

    obj = Employee()
    lst_ = Employee.get_data()
    dict = {}
    for emp in lst_:
        if 30 < int(emp["DEPARTMENT_ID"]) < 110 and int(emp["SALARY"]) > 4200:
            first_name = emp['FIRST_NAME'] + ' ' + emp['LAST_NAME']
            hire_date = emp['HIRE_DATE']
            date_ = datetime.strptime(hire_date, "%d-%b-%y")
            result = str(date_.date())
            dict[result] = [first_name]
            dict.update({result: [first_name]})
    print(dict)
