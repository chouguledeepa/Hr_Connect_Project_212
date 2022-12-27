"""

Create a flask application with following API endpoints for HRConnect project.
"""
# ownload .csv data from following website -
# https://gist.github.com/kevin336/acbb2271e66c10a5b73aacf82ca82784
# TASK 1:
# Write a program to get details of employees who's salary is > 9000. The output should
# be in following format
# {
"""
"Name": "<first_name last_name>",
"email": "<email>",
"phone number": "<phone number without DOT>"
}

"""
# TASK 2
# Write a program to get "HIRE DATE" of employee who's department is within range 30
# to 110 AND who's salary is > 4200.
# The output should be in following format.
# {
"""
"<HIRE DATE in YYYY-MM-DD format>": [
"<first_name last_name>",
...,
"<first_name last_name>"
],
}

<home-url>:8080/api/taskone
<home-url>:8080/api/tasktwo

"""

"""
NOTES
1. Our first basic application runs on `localhost` (IP address - 127.0.0.1)
2. You
"""
# `route` decorator allows us to bind function to certain `relative URL path`.
from flask import Flask, redirect, url_for

# Flask` is the class we use to instantiate an application.
app = Flask(__name__)

@app.route("/employee1")
def employee_Destail():
    url = url_for("employee_Destail", F_name="Den", L_name="Raphaely", Phone_Num="5151274561")
    print(url)
    return "<h1>employee::{'Den', 'Raphaely', '515.127.4561', '11000'}</h1>"

#114	Den	Raphaely	DRAPHEAL	515.127.4561	07-DEC-02	PU_MAN	11000	-	100	30

@app.route("/employee/<Employee>")
def greet_employee(Employee):
    return f"<h1>employee:: Den Raphaely 515.127.4561 11000,{Employee}</h1>"


# @app.route("/client/<client>")
# def greet_client(client):
#     return f"<h1>client:: good morning, {client}</h1>"
#
#
# @app.route("/user/<use_type>/<name_>")
# def greet_everyone(use_type, name_):
#     if use_type == "employee":
#         emp_url = url_for("greet_employee", name=name_)
#         return redirect(emp_url)
#     elif use_type == "client":
#         client_url = url_for("greet_client", client=name_)
#         return redirect(client_url)
#     return f"<h1>choose either employee or client</h1>"


if __name__ == "__main__":
    app.run(debug="true", host="localhost", port=8080)