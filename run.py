
# Python simply flag chellange quiz

name = input("What's your name:")  # user provide name
print("Welcome", name, "to Flags of the World Quiz! ")
quizStart = input("Are you ready to start" + name + "?" "[YES/NO]")
if quizStart.lower() == "yes":
    print("Okay! " + name + " so Let's start! ")
    score = 0   # quiz start with zero score
else:
    print("Good bye!")
    quit()

answer = input("A red circle on a green background is a flag of?")  # 1 question
if answer.lower() == "bangladesh":
    print('Correct!')
    score += 1  # user provide correct answer one point is added to score
else:
    print("Incorrect!")


answer = input("Which mythical animal is on the Welsh flag ")  # 2 question
if answer.lower() == "dragon":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Which weapon is on Mozambique flag? ")  # 3 question
if answer.lower() == "gun" or answer.lower() == "ak47" or answer.lower() == "kalashnikov" or answer.lower() == "rifle":
    # several possible correct answers when the answer ca be ambiguous
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("On whose country flag is green cedar tree presented? ")  # 4 question
if answer.lower() == "lebanon":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Which animal is biting a snake in the centre of the Mexican flag? ")  # 5 question
if answer.lower() == "eagle" or answer.lower() == "mexican eagle":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Which central African country has a bird on its flag? ")  # 6 question
if answer.lower() == "uganda":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("The Albanian flag features an eagle with how many heads? ")  # 7 question
if answer.lower() == "2" or answer.lower() == "two":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which animal will you find clutching a sword on the SriLanka flag? ")  # 8 question
if answer.lower() == "lion":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which is the only country in the world to have a flag with more than four sides?' ")  # 9 question
if answer.lower() == "nepal":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Which country in Europe has the same flag like Poland but colours displayed in oposite order? ")  # 10 question
if answer.lower() == "monako" or answer.lower() == "monaco":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("That was the last question, here you have a results:")
print(name, "you answered " + str(score) + " questions correct!")
print(name, "you got " + str((score / 10) * 100) + "% score")  # this calculate percentage of correct responses
