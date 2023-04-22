#snake water gun solution
import random
condition = [
    ["D", "W", "L"],
    ["L", "D", "W"],
    ["W", "L", "D"]
]
choice = ["Snake", "Water", "Gun"]

print("\n")
while True:
    try:
        urchoice = int(input("Enter your choice (0 for Snake, 1 for Water, 2 for Gun): "))
        compChoice = random.randint(0,2)
        if urchoice < 0 and urchoice > 3:
            raise ValueError
        
        else:
            print(f"You Choose {choice[urchoice]} and computer choose {choice[compChoice]}")
            match condition[urchoice][compChoice]:
                case 'W':
                    print("You Win")
                case "L":
                    print("You Loose")
                case "D":
                    print("You Draw")
    except:
        print("wrong choice")
        
    if input("\npress y for continue: ") != "y":
        break
    else:
        continue
