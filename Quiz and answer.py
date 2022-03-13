print("Answer the following questions correctly with answers in capital letter: ")
print()

correct = 0

print("\tQUESTION 1")
quest1 = input("How many colour does nigerian flag has? ")
answer1 = "TWO"

if quest1.upper()==answer1 or 2:
    correct += 1
    print("You got it right")
else:
    print("You got it wrong, the correct answer is: ", answer1)

#Question 2
print("\t Questions")
print()
quest2 = input("What year is the nigerian independenc? ")
answer2 = 1960
if quest2==answer2:
    correct+=1
    print("You got it right")
else:
    print("You got it wrong, the correct answer is ", answer2)