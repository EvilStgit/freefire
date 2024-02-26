import os
from itertools import product
import string as str
path = os.getcwd()
file = input("Enter File Name (with .txt) : ")
file_path = path+"/"+file
print(f"File will be {file_path}")
# ch = str.ascii_letters + str.digits + str.punctuation
min = int(input("min: "))
max = int(input("max: "))

ch1 = input("Want to make change the word from which wordlist is being formed ").lower()
if ch1 == "n":
  ch = str.ascii_letters + str.digits + str.punctuation
  c = 0
  with open(file,"w") as f:
    for i in range(min , max+1):
      for j in product(ch , repeat=i):
        pswd = "".join(j)
        f.write(pswd)
        f.write("\n")
        c+=1
    f.write(f"{c} passwords generated")
  print(c)
elif ch1 == "y":
  ch2 = input("Want to use template type y ? else create your own words type n").lower()
  if ch2 == "y":
    ch = ""
    small = input("want to add letters (y)?").lower()
    if small == "y" :
      ch += str.ascii_letters
    number = input("want to add numbers (y)?").lower()
    if number == "y":
      ch += str.digits
    punc = input("Want to add speacial caracters (y)?").lower()
    if punc == "y":
      ch += str.punctuation
    if ch == "":
      print("word cannot be empty")
    elif ch != "" :
      print(f"word from where wordlist will be created : {ch}")
      c = 0
      with open(file_path,"w") as f:
        for i in range(min , max+1):
          for j in product(ch , repeat=i):
            pswd = "".join(j)
            f.write(pswd)
            f.write("\n")
            c+=1
        f.write(f" {c} passwords generated")
      print(c)
  elif ch2 == " ":
    ch = input("Enter the words from the wordlist to bee formed: ")
    c = 0
    with open(file,"w") as f:
      for i in range(min , max+1):
        for j in product(ch , repeat=i):
          pswd = "".join(j)
          f.write(pswd)
          f.write("\n")
          c+=1
      f.write(f"{c} passwords generated")
    print(c)
    
print("Thnax for using please feel free to use it again(-_-)")