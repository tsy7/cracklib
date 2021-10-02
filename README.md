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

 
