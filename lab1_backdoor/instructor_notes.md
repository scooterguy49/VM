# Instructor Notes for Lab 1

## Main Vulnerability
The vulnerable application contains a hidden authentication path inside the `login()` function:

```python
elif password == "letmein":
    print("\nMaintenance override accepted.")
    return "maintenance_user", "admin"