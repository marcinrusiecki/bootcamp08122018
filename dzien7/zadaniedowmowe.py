import sys
import os
dirname = os.path.join("c:\\Users\kurs\workspace")

os.listdir(dirname)
print(dirname)
for f in os.listdir(dirname):
    if os.path.isdir(os.path.join(dirname, f)):
        print(f)