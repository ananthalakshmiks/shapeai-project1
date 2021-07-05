import hashlib

value=input("Enter the value : ")
output=value.encode()
print(hashlib.md5(output))