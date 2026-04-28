# Lab 2: Input Validation and SQL Injection
## Objective
In this lab, you will observe two separate Python web applications. One of them contains an SQL injection vulnerability and one of them does not. You will analyze why this is and how an attacker might utilize this vulnerability to gain unauthorized access among possible other things.

---

## Files Provided
- app.py
- secure_app.py
- Lab2student_instructions.md

---

### Step 0: Create Your Lab Submission File

1. Locate the file Lab2_Submission_Template.docx  

2. Make a copy of the file  

3. Rename your copy using the format: La2_<YourName>.docx

   Example:
   Lab1_JohnDoe.docx

4. Open your copy. You will complete it as you work through the lab.

---
## Section 1: Vulnerable login page

### Step 1: Run the vulnerable login page
Open a terminal in the lab folder and run app.py click the URL provided in the console to open up the login page in a web browser, or alternatively copy and paste the URL provided into a web browser to open the login page

### Step 2: Login to Bob
- Bob is a user for this website and he has an account. You know his username is "bob", but you do not know his password. Try to see if you can log in and observe what happens

- Try and log in with his correct password "secure456"

- Notice the "SQL Query Used:" section below the login button.

Answer Questions 1, 2, and 3 on your Template.

- Now, try to use "'OR 1=1--" as the password for bob and see what happens?

Answer questions 4, 5, and 6 on your template.

### Step 3: Login to Administrator

- Now see if you can log into an account with more privileges, try logging into the admin account. *hint, the username might be "admin"*

---

## Section 2: Secure login page
- ### Step 1: Run the secure login page
Open a terminal in the lab folder and run secure_app.py click the URL provided in the console to open up the login page in a web browser, or alternatively copy and paste the URL provided into a web browser to open the login page

###  Step 2: Try to do the same tricks you did from section 1
answer questions 7 on your template

---

## Section 3: Code Review
Open the code for both app.py and secure_app.py in either a text editor or code editor and review it.

Answer questions 8 and 9 on your template

---

## Final Submission
Submit your file as:

Lab2<YourName>.docx


Submit your file as:
Lab2_<YourName>.docx
