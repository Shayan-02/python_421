from random import randint

start = int(input("start: "))
end = int(input("end: "))

correct_number = randint(start, end)

i = 5
while i:
    number = int(input(f"enter a number in range {start} and {end}\nyou have {i} chances: "))
    if number == correct_number:
        print("you win")
        break
    elif number > correct_number:
        print("enter lower number")
    else:
        print("enter higher number")
    i -= 1
else:
    print(f"Game over\ncorrect number is {correct_number}")