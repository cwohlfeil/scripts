#! python3
import re
import pyperclip

# Regex for phone number
phoneRegex = re.compile(r'''
(                           # Super group to prevent findall issues
((\d\d\d)|(\(\d\d\d\)))?    # Area code (optional)
(\s|-)                      # First separator
\d\d\d                      # First 3 digits
-                           # Separator
\d\d\d\d                    # Last 4 digits
(((ext(\.)?\s)|x)           # Extension (optional)
(\d{2,5}))?                 # Extension digits (optional)
)
''', re.VERBOSE)

# Regex for e-mail addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+     # Name
@                   # @ symbol
[a-zA-Z0-9_.+]+     # Domain
''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste()

# Extract the emails and phone numbers from the clipboard
extractedNumbers = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# Clean up the phone numbers
allPhoneNumbers = []
for phoneNumber in extractedNumbers:
    allPhoneNumbers.append(phoneNumber[0])

# Copy back to clipboard, one per line
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
