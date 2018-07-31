import smtplib

"""
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
smtpObj.sendmail('bob@example.com', 'alice@example.com',
                 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()
"""

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(smtpObj.ehlo())
smtpObj.starttls()
smtpObj.login('minusthewohlfe@gmail.com', 'zwwwwggzkfdprllb')
smtpObj.sendmail('minusthewohlfe@gmail.com', 'dedgediragato@gmail.com',
                 "Subject: Test.\nDear Dedge, so long and thanks for all the fish. Sincerely, Wohlfe")
smtpObj.quit()
