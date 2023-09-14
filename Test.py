'''
Welcome to my test
Please don't cheat and look at the code
It's not fun like that :(
'''
import time
print("Welcome to the test of Knowledge")
print("This test will show how much you know about Tyler")
answer1=input("Question 1, has Tyler ever been in a shark tank? true for yes, false for no ")
if ((answer1 == "True") or (answer1 == "true")):
    print("Correct you got the first one, can you keep it up?")
else:
    if ((answer1 == "False") or (answer1 == "false")):
        print("Incorrect. How did you get it wrong?")
        time.sleep(2)
        exit()
    else:
        print("Please answer in True or False")
        time.sleep(2)
        exit()
answer2=int(input("What year was Tyler born? "))
if answer2 == 2010:
    print("Congrats! You got another one. Now the question is how many can you do? ")
else:
    print("Oh no!! You got it wrong!! Try again")
    time.sleep(2)
    exit()
print("What Soccer Club do I play for?")
answer3=input("Snohomish United, NSC, Seattle United, Sound FC, or Liverpool FC")
if ((answer3 == "NSC") or (answer3 == "nsc")):
    print("Correct! No way! That's luck")
else:
    print("WRONG! Restart he he")
    time.sleep(2)
    exit()
print("You have made it to the final question")
answer4=int(input("This is a 1 in 50 chance you get this. Pick a number in 1-50 and good luck!"))
if answer4 == 21:
    print("No way... You must have cheated...")
    time.sleep(3)
    print("I lied before. There is one final question that you have to ask me in person... Cya soon!")
    time.sleep(7)
    print("Son Heung-Min")
    time.sleep(2)
else:
    print("Nope! Try again :)")
