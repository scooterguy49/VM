# Lab 1: Hidden Functionality and Improper Authorization

## Objective
In this lab, you will analyze a Python application that contains hidden functionality. You will identify the vulnerability, fix the code, and complete a worksheet that guides you through secure software engineering concepts.

---

## Files Provided
- vulnerable_app.py
- Lab1_Submission_Template.docx

---

## Step 0: Create Your Lab Submission File

1. Locate the file Lab1_Submission_Template.docx  
2. Make a copy of the file  
3. Rename your copy using the format:

   Lab1_<YourName>.docx

   Example:
   Lab1_AllisonPowell.docx

4. Open your copy. You will complete it as you work through the lab.

---

## Section 1: Observing the Vulnerability

### Step 1: Run the Program

Open a terminal in the lab folder and run:

python3 vulnerable_app.py

Go to Section 1, Question 1 in your worksheet.

- Describe what the program is intended to do  
- Identify the main features of the system  

---

### Step 2: Test Valid Logins

Try the following credentials:

- alice / alice123  
- bob / bob123  
- charlie / charlie123  

Go to Section 1, Question 2.

- Record what happens for each user  
- Identify which users can access the admin panel  

---

### Step 3: Identify Suspicious Behavior

Run the program again and try:

- Any username  
- Password: letmein  

Go to Section 1, Question 3.

- Describe what happens  
- Identify what level of access is granted  

Then answer Question 4:

- Explain why this behavior is a security issue  

---

## Section 2: Code Analysis

### Step 4: Inspect the Code

Open vulnerable_app.py in your editor.

Focus on the login() function.

Go to Section 2, Question 5.

- Identify the exact code that allows the bypass  
- Copy or describe the code  

Answer Question 6:

- Explain why this code is insecure  

Answer Question 7:

- Select Hidden Functionality / Backdoor  

---

## Section 3: Fixing the Vulnerability

### Step 5: Modify the Code

Update the program so that:

- Only valid usernames and passwords allow login  
- No hidden password or override exists  
- Admin access is only granted to users with role "admin"  

Go to Section 3, Question 8.

- Describe what changes you made  

---

### Step 6: Update the login() Function

Go to Question 9.

- Paste your updated login() function  

---

### Step 7: Test Your Fix

Run the program again:

python3 vulnerable_app.py

Test the following:

- Valid users should still work  
- The password "letmein" should no longer grant access  

Go to Question 10.

- Describe what happens when using "letmein" after your fix  

---

## Section 4: Misuse Case

### Step 8: Analyze the Attack

Go to Question 11.

- Describe the attacker’s goal  

Go to Question 12.

- List the steps the attacker uses to exploit the system  

Go to Question 13.

- Describe the impact of this vulnerability  

---

## Section 5: Security Use Case

### Step 9: Describe Secure Behavior

Go to Question 14.

- Explain what the system should do instead  

Go to Question 15.

- Describe the correct secure flow of authentication and authorization  

---

## Section 6: Secure Software Principles

### Step 10: Identify Principles

Go to Question 16.

- Select Least Privilege and Secure by Design  

Go to Question 17.

- Explain why these principles apply to this lab  

---

## Section 7: Reflection

### Step 11: Answer Reflection Questions

Answer:

- Question 18: Why is hidden functionality dangerous  
- Question 19: How could this vulnerability be prevented  
- Question 20: What you learned from this lab  

---

## Section 8: Screenshots

### Step 12: Capture Evidence

Insert the following screenshots into your worksheet:

- Normal login working  
- Exploit using "letmein" working  
- Exploit failing after your fix  
- Vulnerable code section  
- Fixed code section  

---

## Section 9: Verifying Security Enhancements

### Step 13: Test Login Attempt Limits

Run the fixed version of the program:

python3 fixed_app.py

Enter incorrect credentials multiple times.

Observe:
- Access is denied after each failed attempt  
- After the maximum number of attempts, the system locks access  

Go to your worksheet and record:
- How many attempts are allowed  
- What message is displayed when access is locked  

---

### Step 14: Review the Audit Log

Locate the file created by the program:

lab1_audit.log

Open the file using a terminal command or text editor:

Linux / VM:
cat lab1_audit.log

Windows:
type lab1_audit.log

Observe the contents of the log file.

Go to your worksheet and answer:
- What types of events are recorded (e.g., login success, failure, lockout, admin access)  
- Why logging is important for system security  

---

### Step 15: Analyze Security Improvements

Go to your worksheet and answer:

- How does limiting login attempts improve security  
- How does logging improve system monitoring and accountability  
- Why these features are important in real-world systems  

These steps demonstrate how secure systems not only prevent unauthorized access but also monitor and record activity to detect potential threats.

---

## Final Submission

Before submitting, ensure:

- All questions are completed  
- Code changes are included  
- Screenshots are inserted and labeled  

Submit your file as:

Lab1_<YourName>.docx
