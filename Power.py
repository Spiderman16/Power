#this just prints a blank line
print("\n\n")
#this just prints the title
print("Power Tounament")
#this just prints a blank line
print("\n\n")
#this just puts in the name value of what you are entering to name yourself
name = input("Please enter your name: ")
#this just prints a blank line
print("\n\n")
#this enters the vaule of your strength level
strength = int(input("Please enter your strength level: "))
#this just prints a blank line
print("\n\n")
#this enters the vaule of your IQ level
IQ = int(input("Please enter your IQ level: "))
#this just prints a blank line
print("\n\n")
#this enters the vaule of your speed level
speed = int(input("Please enter your speed level: "))
#this just prints a blank line
print("\n\n")
#this enters the vaule of your chi level
chi = int(input("Please enter your chi level: "))
#this just prints a blank line
print("\n\n")
#this is the total of all of your levels
power = str(int(strength + IQ + speed + chi))
#prints the total level of your power
print("Power total is: " + power)

#this just prints a blank line
print("\n\n")
#this is just a Chose of options to choose from mostly a print of sentences
print("A: Satan")
print("B: Vilgax")
print("C: Madara")
print("D: Green Goblin")
#This is putting the vaule of what you will choose
oppnent = input("Choose your opponent: ")
#these are just senarios of what vaule you put in and results of what opponet you choose
if power >= 1000 :
    if oppnent == "A":
        print("It is not your destiny to fight him")
    elif oppnent == "B":
        print("You both come charging at each other")
        print("You both then start trading hits at each other then")
        print("Vilgax falls")
        print(name + "Wins")
    elif oppnent == "C":
        print("You both come running at each other")
        print("madrara jumps up but you come with a rasenshurigen from below")
        print("madara is hit and falls")
        print(name + "Wins")
    elif oppnent == "D":
        print("You both come charging at each other")
        print("Green Goblin comes with pumkin bombs and throws them")
        print("but you catch one of his bombs and throw them back")
        print("which knocks him down off his glider then ")
        print("You grab it then shank him with it")
        print(name + "Wins")
