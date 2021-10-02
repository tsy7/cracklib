# cracklib
this is library for crack Hash

## imports used:
* hashlib
## How to use?
```py
import cracklib

# call the class
app = cracklib.Cracker(testWord)

if app.crackHash(testHash):
  print("Done : {}".format(testWord))
else:
  print("it's not {}".format(testWord))
# end app
```
## How to use for Tools?
```py
import cracklib

testWord = input("Enter Word Guess: ")
testHash = input("Enter Hash Guess: ")

app = cracklib.Cracker(testWord)

if app.crackHash(testWord):
  print("Done : {} -> {}".format(testWord, testHash))
else:
  print("Error : {}".format(testWord))
```
## How to use list?
```py
import cracklib

hashes = [
    "5f4dcc3b5aa765d61d8327deb882cf99", # MD5 password
    "58acb7acccce58ffa8b953b12b5a7702bd42dae441c1ad85057fa70b", # SHA224 admin
    "c90023380fc1d5721a5e20d230077a13cd3c0f9c2f407fa7bde17abecac0301dd95baf3fe5784e833a185218763ac549", # SHA3_384 glitch
]

for Hash in hashes:
  app = cracklib.Cracker("glitch")
  if app.crackHash(Hash):
    print("Done : ", Hash)
  else:
    print("Error : ", Hash)
```
## THX
* Thx spooky sec for help
