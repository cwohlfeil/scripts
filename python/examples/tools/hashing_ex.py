import hashlib
md5 = hashlib.md5()
try:
    md5.update('Python rocks!')
except TypeError:
    print("Type Error")
md5.update(b'Python rocks!')
print(md5.digest())

sha = hashlib.sha1(b'Hello Python').hexdigest()
print(sha)


# With salt
import binascii

dk = hashlib.pbkdf2_hmac(hash_name='sha256', password=b'bad_password34', salt=b'bad_salt', iterations=100000)
print(binascii.hexlify(dk))