
# Just a simple game about coffee... or is it?
import random
from time import sleep
drank_key = False
print("""


                           A totally normal
                            ______   _____    _______   _______   ______   ______
                   ~~      |        |     |  |         |         |        | 
                  ~~~~     |        |     |  |_______  |_______  |______  |_______
               ~~~~~       |        |     |  |         |         |        | 
             ~~~~~~        |______  |_____|  |         |         |______  |_______  game.
               ~~~~~~
              ~~~~~~~~
            ~~~~~~~~~~~~
           ~~~~~~~~~~~~                
        #################
      |###################| 
      |###################|---- 
      |___#############___| |  |              
      |   |____________|  | |  |         
      |                   | |  | 
      |                   | |  | 
      |                   |----
      |                   |  
      |___________________|
      
""")
sleep(4)
print("Loading...")
sleep(7)
play = input("Play? Don't play? (p/dp) ")
if play == "p":
    print("In front of you are 6 delicious coffees. You stare at them happily.")
    print("At this coffee shop, you may create your own coffee, or spin a wheel to get a random coffee.")
    sleep(4)
    answer = input("What would you like to do? (spin/make) (make currently W.I.P) ")
    if answer.lower() == "spin":
        random_coffee = random.randint(1, 6)
        if random_coffee == 1:
            print("You got... coffee #1!")
            sleep(3)
            print("You receive a purple liquid that jiggles around in the mug.")
            print("You are skeptical if this is actually coffee or not but are encouraged by the owner to drink it.")
            sleep(4)
            print("Slowly, you put the mug to your mouth, before pouring the gelatinous liquid down your throat.")
            print("As it gently slides down your throat, you feel a burning in your stomach.")
            sleep(3)
            print("Just as you feel like you are going to explode, you let out a massive...")
            print("BUUUUURRRRPPPPPPPP!!!!!!!!!")
            sleep(3)
            print("Dazed, you give the shop owner a crazed look. It tasted like blueberries, though, so, that's a bonus.")
            quit()
        elif random_coffee == 2:
            print("You got coffee #2!")
            sleep(2)
            print("The shop owner slides a nice coffee down the table. It looks beautiful, and shines in the sunlight. ")
            print("Enjoy the nice, warm, energising liquid!")
            quit()
        elif random_coffee == 3:
            print("You got coffee #3!")
            sleep(2)
            print("In front of you is a green, bubbling liquid. Something inside the drink seems to be reacting with the liquid.")
            print("Hesitantly, you take a massive gulp.")
            sleep(2)
            print("You start choking on something, and clutch your burning throat. Eventually, you cough up a golden key.")
            sleep(3)
            print("It's covered in drool. This must have been what the drink was reacting with...?")
            sleep(2)
            drank_key = True
        elif random_coffee == 4:
            print("You got coffee #4!")
            sleep(2)
            print("You get a nice coffee. It smells of strawberries.")
            print("The drink tastes beautiful, and you can't stop buying more and more amd more and more and more...")
            sleep(4)
            while 3 > 1:
                print("and more and more and more...")
        elif random_coffee == 5:
            print("The owner shrugs and states that coffee #5 is out of stock, for... reasons...")
        elif random_coffee == 6:
            print("You got coffee #6!")
            sleep(2)
            print("A crimson red liquid wobbles around your mug. Hesitantly, you drink it.")
            sleep(1)
            print("You immediately become energised, and exit the shop, do a 50 mile run and break your legs and die.")
            sleep(2)
            print("The end!")
    if drank_key == True:
        print("The owner of the shop eyes you suspiciously.")
        print("You hold the sodden key in your hand.")
        sleep(2)
        print("You look around and see a door with a lock. You walk over to it and, just for fun, try to see if the key works.")
        sleep(4)
        print("To your surprise, it works. Just as you are about to step into the pitch black room, you hear a scream from inside,")
        print("and turn around. The owner is holding a bat. She stares a you furiously. WHACK!")
        sleep(3)
        print("You wake up on a conveyer belt. You are moving towards some grinding machine.")
        print("Suddenly you realise you are tied up and can't move.")
        print("You look around. You see the owner staring at you.")
        sleep(3)
        print("'You will make an excellent coffee...' She says, pulling some sort of lever.")
        sleep(2)
        print("'HELP ME!!!!' You scream.")
        print("Her cackles are the last thing you hear before you plummet into the grinder, never to be seen again...")
elif play == "dp":
    quit()

