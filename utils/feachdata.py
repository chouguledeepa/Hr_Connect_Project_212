import csv

class Employee:
    filename = "employees.csv"

    @classmethod
    def get_data(cls):
        """
        classmethod
        :return: csv to list of directory format
        """
        lst = []
        with open(cls.filename,mode='r')as f:
            data = csv.DictReader(f)
            for row in data:
                lst.append(dict(row))
            return(lst)


    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            return foo.readlines()

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()

    @classmethod
    def convert(cls):
        dict={}
        with open(cls.filename)as bar:
            for line in bar:
                key,val = line.split()
                dict[key]=val
                print(dict)

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
