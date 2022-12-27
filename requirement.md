├── HRConnect (project root)
│ ├── my_utils (your custom package)
│ │ ├── __init__.py
│ │ ├── csv.py (csv file related functions)
├── task_one.py (entry-point for task 1)
├── task_two.py (entry-point for task 2)
├── README.md (your documentation on project)

csv.py file should contain a class somewhat like following -
class HandleCSV:
filename = "<absolute-path-of-downloaded-file-here>"
@classmethod
def read_entire_csv(cls):
with open(cls.filename, "r") as foo:
return foo.readlines()
@classmethod
def read_csv_line_by_line(cls):
with open(cls.filename) as bar:
yield bar.readline()

certifi==2022.9.24
charset-normalizer==2.1.1
idna==3.4
requests==2.28.1
urllib3==1.26.13
