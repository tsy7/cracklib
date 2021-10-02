# call the file
import cracklib

# type input for user
testWord = input("Enter Word Guess: ")
testHash = input("Enter Hash Guess: ")

# call the class 
app = cracklib.Cracker(testWord)

"""
now use function in class 
and use if statement for look at result
"""
if app.crackHash(testHash):
    print("Done : {}".format(testWord))
else:
    print("it's not {}".format(testWord))
# end app