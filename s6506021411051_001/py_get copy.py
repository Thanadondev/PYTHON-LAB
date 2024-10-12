#!C:\Users\BOM\AppData\Local\Programs\Python\Python311\python.exe
#coding: utf-8

import cgi

form = cgi.FieldStorage()


user = form.getvalue("textfield")
password = form.getvalue("password")
textarea = form.getvalue("textarea")
radio = form.getvalue("radio")
select = form.getvalue("select")
checkboxes = form.getlist("checkbox[]")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print("<title>result form</title>")
print("</head>")
print("<body>")
print("<h2>result form:</h2>")
print("<p>User: " + user + "</p>")
print("<p>Password: " + password + "</p>")
print("<p>Textarea: " + textarea + "</p>")
print("<p>Radio: " + radio + "</p>")
print("<p>Select: " + select + "</p>")
print("<p>Checkboxes: " + ", ".join(checkboxes) + "</p>")
print("</body>")
print("</html>")
