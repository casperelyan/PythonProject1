# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

name = input("What's your name: ")
print("Welcome", name, "to Flags of the World Quiz! ")
quizStart = input("Are you ready to start", name, "?" "[YES/NO]" )
if quizStart.lower() != "yes":
    quit()

print("Okay!", name, "So Let's start! ")
score = 0

answer = input("A red circle on a green background is a flag of? ")
if answer.lower() == "Bangladesh" or "People's Republic of Bangladesh" :
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Which mythical animal is on the Welsh flag ")
if answer.lower() == "Dragon" or "Red Dragon":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")




print(name, "you got " + str(score) + " questions correct!")
print(name, "you got " + str((score / 2) * 100) + "%.")