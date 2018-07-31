u = chr(40960) + 'abcd' + chr(1972)
print(u)
try:
    u.encode('ascii')
except UnicodeEncodeError:
    print("UnicodeEncodeError")
print(u.encode('ascii', 'ignore'))
print(u.encode('ascii', 'replace'))
