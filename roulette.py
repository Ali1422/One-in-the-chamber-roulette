import random
import time
print("****************************")
print("Welcome to russian roulette!")
print("****************************")
while True:
    number = int(input("please enter a random number from 1 to 6"))
    random = random.randint(1,6)
    time.sleep(2)
    print("bullet being placed into chamber...")
    time.sleep(2)
    print("spinning......")
    time.sleep(2)
    print("trigger being pulled")
    time.sleep(3)
    if number == random:
        print("you have pulled the trigger")
        time.sleep(1)
        print("The bullet shoots and the chamber and shoots you dead, you have lost")
    elif number != random:
        print("you have pulled the trigger")
        time.sleep(1)
        print("The chamber clicks, you have survived")
    else:
        print("error, please try again")
        quit()


            
    

