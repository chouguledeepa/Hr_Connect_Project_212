from utils.feachdata import Employee

file_name = "employees.csv"

if __name__ == "__main__":
    """
    creating object of a class 
    
    """

    obj = Employee()
    lst = Employee.get_data()

    salary = {}
    for emp in lst:
        for i, j in emp.items():
            if int(emp["SALARY"]) > 9000:
                first_name = emp["FIRST_NAME"]
                last_name = emp["LAST_NAME"]
                name = f"{first_name} {last_name}"
                email = emp["EMAIL"]
                phone_number = emp["PHONE_NUMBER"]
                salary.update({"name": name})
                salary.update({"email": email})
                salary.update({"Phone_Number": phone_number})
        print(salary)
