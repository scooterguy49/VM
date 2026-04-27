Lab 2: SQL Injection and Secure Authentication
Objective
In this lab, you will analyze a Python web application that contains an SQL injection vulnerability. You will observe how improper handling of user input can allow unauthorized access, compare a vulnerable and secure implementation, and complete a worksheet covering secure software engineering concepts. 

Files Provided


app.py


secure_app.py


templates/login.html


templates/secure_login.html


Lab2_Submission_Template.docx



Step 0: Create Your Lab Submission File


Locate the file Lab2_Submission_Template.docx


Make a copy of the file


Rename your copy using the format:


Lab2_<YourName>.docx
Example:
Lab2_AllisonPowell.docx


Open your copy. You will complete it as you work through the lab.



Section 1: Observing the Vulnerability
Step 1: Run the Vulnerable Program
Open a terminal in the lab folder and run:
python3 app.py
Open the browser and go to:
http://127.0.0.1:5000
Go to Section 1, Question 1 in your worksheet.


Describe what the application is intended to do


Identify the main features of the login system



Step 2: Test Valid Credentials
Try the following credentials:


alice / password123


bob / secure456


admin / adminpass


Go to Question 2.


Record what happens for each login


Explain how the system verifies users



Step 3: Test Invalid Credentials
Try incorrect usernames or passwords.
Go to Question 3.


Describe what happens when invalid credentials are entered


Explain the expected behavior of a secure login system



Step 4: Perform SQL Injection
Try entering payloads such as:
Username:
' OR '1'='1
Password:
anything
Go to Question 4.


Record what happens


Explain whether authentication was bypassed


Then answer Question 5:


Explain why this behavior is a security vulnerability



Section 2: Code Analysis
Step 5: Inspect Vulnerable Code
Open app.py in your editor.
Focus on the login function and query construction.
Go to Question 6.


Identify the exact line of code that makes the application vulnerable


Copy or describe the vulnerable SQL statement


Go to Question 7.


Explain why directly combining user input into SQL is insecure



Step 6: Analyze the Attack
Go to Question 8.


Explain how the SQL payload changes the meaning of the query


Describe why the database returns a user record



Section 3: Secure Implementation
Step 7: Run the Secure Program
Open a terminal and run:
python3 secure_app.py
Visit:
http://127.0.0.1:5000
Go to Question 9.


Describe the differences between the secure and vulnerable versions



Step 8: Test the Same Injection Payload
Use the same SQL injection input from Step 4.
Go to Question 10.


Record what happens in the secure version


Explain why the attack fails



Step 9: Inspect Secure Code
Open secure_app.py.
Locate the parameterized query.
Go to Question 11.


Copy or describe the secure SQL statement using placeholders


Go to Question 12.


Explain how parameterized queries prevent SQL injection



Section 4: Misuse Case
Step 10: Analyze the Attacker
Go to Question 13.


Describe the attacker’s goal


Go to Question 14.


List the steps used to exploit the vulnerable application


Go to Question 15.


Describe the impact of unauthorized login access



Section 5: Security Use Case
Step 11: Describe Secure Behavior
Go to Question 16.


Explain what the system should do when receiving malicious input


Go to Question 17.


Describe the proper secure authentication flow



Section 6: Secure Software Principles
Step 12: Identify Principles
Go to Question 18.


Select Input Validation, Secure by Design, and Defense in Depth


Go to Question 19.


Explain why these principles apply to this lab



Section 7: Reflection
Step 13: Answer Reflection Questions
Answer:


Question 20: Why is SQL injection dangerous


Question 21: How can developers prevent SQL injection


Question 22: What did you learn from this lab



Section 8: Screenshots
Step 14: Capture Evidence
Insert the following screenshots into your worksheet:


Normal successful login


Failed login attempt


SQL injection bypass working in app.py


Same injection failing in secure_app.py


Vulnerable query construction code


Secure parameterized query code



Final Submission
Before submitting, ensure:


All questions are completed


Screenshots are inserted and labeled


Code explanations are included


Submit your file as:
Lab2_<YourName>.docx
