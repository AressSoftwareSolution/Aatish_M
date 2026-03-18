import re

text = """
Contact us at support@test.com or sales@test.org
Call: 9876543210 or 9123456780
"""

# find emails
pattern1 = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)

# find 10-digit phone numbers
pattern2 = re.findall(r'\b\d{10}\b', text)

print("Emails:", pattern1)
print("Phone numbers:", pattern2)
