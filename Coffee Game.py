# All art and code by CatX


# UPDATE 2 OUT NOW!!!
# Features:
# New endings and ending drawings, improved code, and, I finally started work on the making part of the game (where you make your own coffee)
# This godforsaken code drives me insane when trying to fix it, so sadly, update 2 (OUT NOW PLAY IT PLEASE IUDHUAHSDIAUSDDSDSGFG) does not include the maker gamemode:
# (The code:)

"""
# Code here has to be fixed:
        answer = input("How many coffee beans do you want? ")
        coffee_beans -= int(input())
        if coffee_beans > 7:
            Lots_of_coffee_beans = True
        answer = input("How many drops of milk do you want in your coffee? ")
        milk_droplets -= int(input())
        if milk_droplets > 27:
            Lots_of_milk_droplets = True
        answer = input("How many sugar cubes do you want in your coffee? ")
        sugar_cubes -= int(input())
        if sugar_cubes > 3:
            Lots_of_sugar_cubes = True
        print("Making...")
        sleep(3)
        print("Coffee done! Here are the results:")
        if Lots_of_coffee_beans == True:
            sleep(2)
            print("Too many coffee beans!")
        if Lots_of_milk_droplets == True:
            print("A bit too much milk!")
        if Lots_of_sugar_cubes == True:
            sleep(2)
            print("Too many sugar cubes!")
        elif Lots_of_coffee_beans == False:
            sleep(2)
            print("A good amount of coffee beans!")
        elif Lots_of_milk_droplets == False:
            sleep(2)
            print("Just the right amount of milk droplets!")
        elif Lots_of_sugar_cubes == False:
            sleep(2)
            print("You resisted the temptation for more sugar- good job!")
        print("Here are the resources you have left:")
        sleep(1)
        print("You have ", coffee_beans, " coffee beans left over,")
        sleep(1)
        print(milk_droplets, " milk droplets,")
        sleep(1)
        print("And finally, you have ", sugar_cubes, " sugar cubes left over." )
        sleep(1)
        print("Enjoy!")
        # Here is where the code that needs fixing ends.
"""        


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
      |___#############___| |  |   Coffees... haha, get it? No...? Oh...           
      |   |____________|  | |  |   :(
      |                   | |  | 
      | COFFEE COFFEE COF-| |  | 
      | FEE COFFEE COFFEE |----
      | COFFEE COFFEE     |  
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
            sleep(1)
            print("You got the...")
            sleep(1)
            print("""
            
                            Weird, burp inducing, blueberry tasting,
                            ______   _____    _______   _______   ______   ______
                   ~~      |        |     |  |         |         |        | 
                  ~~~~     |        |     |  |_______  |_______  |______  |_______
               ~~~~~       |        |     |  |         |         |        | 
             ~~~~~~        |______  |_____|  |         |         |______  |_______... uh...  thing... ending.
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
      |   WORLD'S BEST    | |  | 
      |     COFFEE        |----
      |   B U R P E R     |  
      |___________________|
            
    Tasty!                   
    
            
            
            
            """)
            quit()
        elif random_coffee == 2:
            print("You got coffee #2!")
            sleep(2)
            print("The shop owner slides a nice coffee down the table. It looks beautiful, and shines in the sunlight. ")
            print("Enjoy the nice, warm, energising liquid!")
            sleep(1)
            print("You got the...")
            sleep(1)
            print("""
            
                            Normal but slightly better than usual tasting          
                            ______   _____    _______   _______   ______   ______
                   ~~      |        |     |  |         |         |        | 
                  ~~~~     |        |     |  |_______  |_______  |______  |_______
               ~~~~~       |        |     |  |         |         |        | 
             ~~~~~~        |______  |_____|  |         |         |______  |_______  ending.
               ~~~~~~
              ~~~~~~~~
            ~~~~~~~~~~~~
           ~~~~~~~~~~~~                
        #################
      |###################| 
      |###################|---- 
      |___#############___| |  |    SLURP SLURP GULP GULP SIP!          
      |   |____________|  | |  |         
      |                   | |  |   
      | i am dependant on | |  | 
      |     COFFEE        |----
      |  to survive       |                 
      |___________________| 
            
            
            
            
            """)
            quit()
        elif random_coffee == 3:
            print("You got coffee #3!")
            sleep(2)
            print("In front of you is a green, bubbling liquid. Something inside the drink seems to be reacting with the liquid.")
            print("Hesitantly, you take a massive gulp.")
            sleep(2)
            print("You start choking on something, and clutch your burning throat. Eventually, you cough up a golden key.")
            sleep(3)
            print("It's covered in drool. This key must have been what the drink was reacting with...?")
            sleep(2)
            drank_key = True
        elif random_coffee == 4:
            print("You got coffee #4!")
            sleep(2)
            print("You get a nice coffee. It smells of strawberries.")
            print("The drink tastes beautiful, and you can't stop buying more and more amd more and more and more...")
            sleep(4)
            while 3 > 1:
                print("and more and more and more... (you got the addiction ending, btw (and btw means by the way, btw)) ")
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
            sleep(1)
            print("You got the...")
            sleep(1)
            print("""
            
            
                            Fitness
                            ______   _____    _______   _______   ______   ______
                   ~~      |        |     |  |         |         |        | 
                  ~~~~     |        |     |  |_______  |_______  |______  |_______
               ~~~~~       |        |     |  |         |         |        | 
             ~~~~~~        |______  |_____|  |         |         |______  |_______  of DEATH ending.
               ~~~~~~
              ~~~~~~~~
            ~~~~~~~~~~~~
           ~~~~~~~~~~~~                
        #################             I'm sure it tasted nice though.
      |###################| 
      |###################|---- 
      |___#############___| |  |              
      |   |____________|  | |  |         
      |                   | |  | 
      | FITNESS POWER     | |  | 
      |   BUT IN...       |----
      |  C O F F E E !    |  
      |___________________|
            
            
            
            
            
            """)
    if answer.lower() == "make":
        coffee_beans = 20
        milk_droplets = 100
        sugar_cubes = 20
        Lots_of_coffee_beans = False
        Lots_of_milk_droplets = False
        Lots_of_sugar_cubes = False
        print("Loading...")
        sleep(3)
        print("Welcome to make a coffee!")
        sleep(1)
        print(""" 


                                   Make a...
                                    ______   _____    _______   _______   ______   ______   
                           ~~      |        |     |  |         |         |        |          |
                          ~~~~     |        |     |  |_______  |_______  |______  |_______   |
                       ~~~~~       |        |     |  |         |         |        |          |
                     ~~~~~~        |______  |_____|  |         |         |______  |_______   #
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
              |  I LOVE COFFEE    | |  | 
              |  AND UHH... STUFF |----
              |   LIKE THAT       |  
              |___________________|       Currently re-stocking coffee beans...

        """)
        sleep(3)
        print("""Welcome to make a coffee! You currently have:"
         
         20 Coffee Beans (5 beans for one coffee)     
         1 Bottle of Milk (1 quarter milk per normal coffee) (you have 100 drops of milk and a quarter takes away 25 drops)
         20 Sugar Cubes (2 per cuppa')     
              """)
        print("Get ready to make your coffee...")
        sleep(4)
        print("Now!")
        sleep(1)

        # Code here has to be fixed:
        answer = input("How many coffee beans do you want? ")
        coffee_beans -= int(input())
        if coffee_beans > 7:
            Lots_of_coffee_beans = True
        answer = input("How many drops of milk do you want in your coffee? ")
        milk_droplets -= int(input())
        if milk_droplets > 27:
            Lots_of_milk_droplets = True
        answer = input("How many sugar cubes do you want in your coffee? ")
        sugar_cubes -= int(input())
        if sugar_cubes > 3:
            Lots_of_sugar_cubes = True
        print("Making...")
        sleep(3)
        print("Coffee done! Here are the results:")
        if Lots_of_coffee_beans == True:
            sleep(2)
            print("Too many coffee beans!")
        if Lots_of_milk_droplets == True:
            print("A bit too much milk!")
        if Lots_of_sugar_cubes == True:
            sleep(2)
            print("Too many sugar cubes!")
        elif Lots_of_coffee_beans == False:
            sleep(2)
            print("A good amount of coffee beans!")
        elif Lots_of_milk_droplets == False:
            sleep(2)
            print("Just the right amount of milk droplets!")
        elif Lots_of_sugar_cubes == False:
            sleep(2)
            print("You resisted the temptation for more sugar- good job!")
        print("Here are the resources you have left:")
        sleep(1)
        print("You have ", coffee_beans, " coffee beans left over,")
        sleep(1)
        print(milk_droplets, " milk droplets,")
        sleep(1)
        print("And finally, you have ", sugar_cubes, " sugar cubes left over." )
        sleep(1)
        print("Enjoy!")
        # Here is where the code that needs fixing ends.
if drank_key == True:
    print("The owner of the shop eyes you suspiciously.")
    print("You hold the sodden key in your hand.")
    sleep(2)
    print("You look around and see a door with a lock. You walk over to it and, just for fun, try to see if the key works.")
    sleep(4)
    print("To your surprise, it works. Just as you are about to step into the pitch black room, you hear a scream from inside,")
    print("and turn around. The owner is holding a bat. She stares a you furiously. WHACK!")
    sleep(5)
    print("You wake up on a conveyer belt. You are moving towards some grinding machine.")
    print("Suddenly you realise you are tied up and can't move.")
    print("You look around. You see the owner staring at you.")
    sleep(4)
    print("'You will make an excellent coffee...' She says, pulling some sort of lever.")
    sleep(5)
    print("'HELP ME!!!!' You scream.")
    print("Her cackles are the last thing you hear before you plummet into the grinder, never to be seen again...")
    sleep(1)
    print("You got the...")
    sleep(2)
    print("""
    
                            You are a
                            ______   _____    _______   _______   ______   ______
                   ~~      |        |     |  |         |         |        | 
                  ~~~~     |        |     |  |_______  |_______  |______  |_______
               ~~~~~       |        |     |  |         |         |        | 
             ~~~~~~        |______  |_____|  |         |         |______  |_______  ending.
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
      |   haha you are a  | |  | 
      |  coffee now haha  |----
      | sip sip gulp gulp |                 _______
      |___________________|                |       |---
                                           |   |   |   |___
                                           |   |   |       |_
                                            -------          |
                                                            _|                  
                                            _______
                                           |       |---
                                           |   |   |   |___
                                           |   |   |       |_
                                            -------          |
                                                            _|                                                  
    
    
    
    """)
elif play == "dp":
    quit()

