# By Tyler Hong, 1/16/23
import time
print("Welcome to the test of Knowledge")
print("This test will show how much you know about Tyler")
answer1=input("Question 1, has Tyler ever been in a shark tank? True for yes, False for no")
if answer1 == "True":
    print("Correct you got the first one, can you keep it up?")
else:
    if answer1 == "False":
        print("Incorrect. How did you get it wrong?")
    else:
        print("Please answer in True or False")
        time.sleep(3)
        exit()
print("Question 2, What video games does Tyler play?")


