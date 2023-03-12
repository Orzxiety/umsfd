from base64 import b64decode
from gzip import decompress

filename = "YOUR_FILE_NAME"

file = open(filename, "rb")
file = file.read()
file = b64decode(file)
data = decompress(file)
result = str(data, "utf-8")
output = open("output.txt", "w")
output.write(result)

print("Done, check output.txt")
