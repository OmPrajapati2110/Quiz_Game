print("Welcome to my computer quiz!")

playing = input("Do you want to play? \n")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:) ")

score = 0

answer = input("What does CPU stands for?\n")
if answer.lower() == "central processing unit":
    print("It is correct")
    score+=1
else:
    print("It is incorrect")

answer = input("What does GPU stands for?\n")
if answer.lower() == "graphics processing unit":
    print("It is correct")
    score+=1
else:
    print("It is incorrect")

answer = input("What does RAM stands for?\n")
if answer.lower() == "random access memory":
    print("It is correct")
    score+=1
else:
    print("It is incorrect")

answer = input("What does PSU stands for?\n")
if answer.lower() == "power supply":
    print("It is correct")
    score+=1
else:
    print("It is incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
 