from random import randint

X = 1
random_number = randint(1 , 1000)

your_number = input("hello! welcome to my app!\nyou just choice number!\nplease enter number:")

while True:
    try:
        your_number = int(your_number)
        break
    except:
        your_number = input("please enter number:")


while your_number != random_number:
    X += 1
    if your_number > random_number:
        print("your number is too big!")
    elif your_number < random_number:
        print("your number is low")
    while True:
        try:
            your_number = int(input("please enter next number: "))
            break
        except:
            print("please enter a valid number!")
print("good job")
print(f"You won with {X} attempts")
input()
