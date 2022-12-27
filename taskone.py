import csv

class Employee:
    file_name = 'employees.csv'

    @classmethod
    def Read_CSV_File(cls):
        with open(cls.file_name, 'r') as csv_files:
            print('read data from a csv file  ')

            return csv_file.readlines()

    @classmethod
    def csv_read_lines(cls):
        with open(cls.file_name, 'r') as csv_file1:
            print('read data from a csv file  ')

            yield csv_file1.readlines()

    @classmethod
    def Employee_Details(cls):
        salary = {}
        with open(cls.file_name, encoding='utf8') as csv_file1:
            csv_reader = csv.DictReader(csv_file1)

            for emp in csv_reader:
                if int(emp['SALARY']) > 9000:
                    first_name = emp['FIRST_NAME']
                    last_name = emp['LAST_NAME']
                    name = f'{first_name}{last_name}'
                    email = emp['EMAIL']
                    phone_number = emp['PHONE_NUMBER']
                    salary.update({'name': name})
                    salary.update(({'email': email}))
                    salary.update({'phone_number': phone_number}, )
                    print(salary)


csv_file = Employee()
file = csv_file.Read_CSV_File()
print("entier file details \n ", file)
print("#######" * 100)

csv_file1 = csv_file.csv_read_lines()
print("line by line details")

for lines in csv_file1:
    print(lines)
print("######" * 50, "\n")

print("salary is grater than 9000 employee: \n", )
csv_file.Employee_Details()

# sum_salary()

# first_name = []
#
# with open('employees.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     fields = next(csv_reader)
#     for row in csv_reader:
#         first_name.append(row[0])
#         print("first name are", " ".join(first_name))

# def salary_grater():
#     with open('employees.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
#         for i in csv_reader:
#             if i[1] >9000:
#                 print(i)
#         csv_file.close()
#
#
# salary_grater()
