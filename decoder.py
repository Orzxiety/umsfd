from base64 import b64decode
from gzip import decompress

filename = "YOUR_FILE_NAME"

print("Decoding...", end=" ")

file = open(filename, "rb")
file = file.read()
file = b64decode(file)
data = decompress(file)
mystring = str(data, "utf-8")
output = open("output.txt", "w")
output.write(mystring)

print("done (check output.txt)")
