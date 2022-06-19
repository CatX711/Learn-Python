# Go to test.py for the testing grounds for this game. Do updates in there
# before copying them into here.

from time import sleep
import random

# TODO:
# Create Battle system
# Make workers mine 5 gold every second automatically
# Make miner robots take 4 seconds to mine but increase gold by 15
# Finish Instructions Manual (Cmd #5)



gold = 0
worker = 0
enemy_dmg = random.randint(1, 10)  # how much damage enemy robots do, from 1 to 10 hp
mining_robots = 0

print("""
       =============
      |             |
      | Super       |
      | Battle      |
      | Game        |
       =============   
      |             |
      | By Daniel C.|
      |             |
       =============



""")

name = input("What's your name, commando? ")
print("Welcome to the resistance, ", name)
print("We need as much help as we can get to fight off those robots.")
sleep(1)
print("There are some gold mines we can use for money. We need money to buy parts for")
print("robots.")
sleep(2)
print("Here's your command panel. It's where you can do anything you want to benefit")
print("our base:")
print("1: Mine ")
print("2: Buy Workers (W.I.P)")
print("3: Show Gold ")
print("4: Show Workers ")
print("5: Help")
print("6: Buy Miner Robot (W.I.P)")
print("7: Quit Game")
print("(1/2/3/4/5/6/7)")
sleep(5)
print("We've been holding them back for quite some time, but its now that we are")
print("desperate for help. We need to destroy the 5 enemy bases so that we can live in")
print("peace.")
sleep(5)
print("Good luck fighting off those dastardly bots.")
sleep(1)
print("""
































""")

while True:  # creates gameplay loop
    print("=============")
    print("YOUR MISSION:")
    print("DESTROY ENEMY")
    print("    BASES    ")
    print("=============")
    print("1: Mine ")
    print("2: Buy Workers (W.I.P)")
    print("3: Show Gold ")
    print("4: Show Workers ")
    print("5: Help")
    print("6: Buy Miner Robot (W.I.P)")
#   print("7: Raid")
#   print("8: Open Map")
    print("9: Quit Game")
    print("(1/2/3/4/5/6/7/8/9)")
    print("---------------")
    print("YOUR ANSWER:")
    answer1 = input()
    if answer1 == "1":
        gold += 15
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Gold: ", gold)
    elif answer1 == "2":
        worker += 1
        print("You got a worker.")
        gold -= 20
        print("Workers: ", worker)
    elif answer1 == "3":
        gold = gold
        print("\n")
        print("=====================")
        print("Current gold: ", gold)
        print("=====================")
        print("\n")
    elif answer1 == "4":
        worker = worker
        print("\n")
        print("==========================")
        print("Current workers: ", worker)
        print("==========================")
        print("\n")
    elif answer1 == "5":
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("""
        INSTRUCTIONS MANUAL:
        
        - TYPE 1 TO MINE FOR GOLD.
          YOUR GOLD INCREASES BY 15 IF YOU MINE.
        - TYPE 2 TO BUY WORKERS.
          WORKERS GET 5 GOLD FOR YOU EVERY SECOND.
          WORKERS ARE CURRENTLY W.I.P.    
        - TYPE 3 TO SHOW HOW MUCH GOLD YOU CURRENTLY HAVE.
        - TYPE 4 TO SHOW THE AMOUNT OF WORKERS EMPLOYED.
        - TYPE 5 TO OPEN UP THE INSTRUCTIONS MANUAL.
        - TYPE 6 TO BUY A MINER ROBOTS. MINER ROBOTS ARE WORKERS ON STEROIDS.
          THEY TAKE 4 SECONDS TO FULLY MINE SOME GOLD, BUT IN THAT TIME SPAN COLLECT
          15 GOLD IN TOTAL. THAT MEANS THAT EVEN WITH A MAXIMUM AMOUNT OF WORKERS,
          MAXIMUM MINER ROBOTS WILL ALWAYS MINE MUCH MORE GOLD.
          MINER ROBOTS ARE CURRENTLY W.I.P.
        - TYPE 7 TO QUIT THE GAME. GOODBYE!
        - MORE FEATURES WILL BE ADDED LATER.
        """)
    # code fo mining robots
    elif answer1 == "6":
        mining_robots += 1
        gold -= 50
        # put rest of code here

    # put raid code here
    # Map code:
    # # raid1_completed = False
    # # raid2_completed = False
    # # raid3_completed = False
    # # raid4_completed = False
    # # answer1 = input("placeholder ")
    # #
    # # if answer1 == "8":
    # #     if raid1_completed True:
    # #         print("""
    # #      =========================================================================================================================================================
    # #      MAP:                                                                                                            ! RAID 5 !
    # #                                   Raid 2                                                                            FINAL RAID
    # #     Raid 1
    # #     (COMPLETED)
    # #
    # #
    # #
    # #
    # #
    # #
    # #
    # #                                                             Raid 3        Raid 4
    # #     ===========================================================================================================================================================
    # #
    # #
    # #
    # #     """)
    # #     if raid2_completed True:
    # # print("""
    # #      =========================================================================================================================================================
    # #      MAP:                                                                                                            ! RAID 5 !
    # #                                   Raid 2                                                                            FINAL RAID
    # #     Raid 1                        (COMPLETED)
    # #     (COMPLETED)
    # #
    # #
    # #
    # #
    # #
    # #
    # #
    # #                                                             Raid 3        Raid 4
    # #     ===========================================================================================================================================================
    # #
    # #
    # #
    # #     """)
    # # if raid3_completed True:
    # #     print("""
    # #      =========================================================================================================================================================
    # #      MAP:                                                                                                            ! RAID 5 !
    # #                                   Raid 2                                                                            FINAL RAID
    # #     Raid 1                        (COMPLETED)
    # #     (COMPLETED)
    # #
    # #
    # #
    # #
    # #
    # #
    # #                                                         (COMPLETED)
    # #                                                         Raid 3        Raid 4
    # #     ===========================================================================================================================================================
    # #
    # #
    # #
    # #     """)
    # # if raid3_completed True:
    # #     print("""
    # #      =========================================================================================================================================================
    # #      MAP:                                                                                                            ! RAID 5 !
    # #                                   Raid 2                                                                            FINAL RAID
    # #     Raid 1                        (COMPLETED)
    # #     (COMPLETED)
    # #
    # #
    # #
    # #
    # #
    # #
    # #                                                         (COMPLETED)   (COMPLETED)
    # #                                                         Raid 3        Raid 4
    # #     ===========================================================================================================================================================
    # #
    # #
    # #
    # #     """)

    elif answer1 == "9":
        print("Good bye, thank you for playing.")
        quit()
    else:
        print("Invalid option, ya idiot. Try again.")

    # LEVEL 1
