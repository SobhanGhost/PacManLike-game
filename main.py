# Modules:
from funtions import * # the functions
import msvcrt as m
import threading as th # for timers
import winsound as w # for playing music
import os
import colorama as c # colorizing
import random as r
import time as ti # waiting time


global t # the variable for playing time

# Functions:
def time(): # this counts the seconds to represent the playtime 
    global t # cause value changes
    
    t+=1 # 1 second per run
    
    th.Timer(1,time).start() # this starts the timer for counting the seconds
    
    if o_map=="": # this checks if the game has ended
                  # stops the timer if True, else pass
        th.Timer(1,time).cancel()



t=0
z=0 # the loops variable
o_map = get_map() # getting the first original map of the game

music(0) # starts the main theme song

####################################
loading(0)
####################################

while z==0: # this loop gets the user's desired difficulty
    try:
        x=int(input("Choose Your Difficulty:\nFor an easy game type in: 1\nFor a medium game type in: 2\nType: "))
        if (x!=1 and x!=2): # checks if the input is valid
            raise
        difficulty(x)
        z=1
    except:
        
        print("Error! Invalid input")
        ti.sleep(2)
        os.system("cls")
        print(o_map)
        
os.system("cls")
ti.sleep(3)
#####################################
# starting the timers of the game
th.Timer(10,time_food).start()
th.Timer(1,time).start()

print(o_map)
z=0 
fl=0 # simple flag
color_v=0 # a variable that demonstrates the time of changing the map color

while z==0: # the main loop of the game
    color_v=r.randint(0,500)
    
    a=ord(m.getch())
    b=ord(m.getch())
    if a==224:
        f=move_player(b)
        if f!=None and f=="":
            break
        elif f!=None and "P" not in f:
            fl=1
            break
        if f!=None and o_map!="":
            if f!="":
                os.system("cls")
            if color_v%2==0:
                print(eval("c.Fore."+color())+f)
                print(eval("c.Fore."+color())+Score())
            else:
                print(f)
                print(Score())
            if f!="":
                print("Your Playing Time: %i"%(t))
            o_map=f
            
if fl==1:
    end()
    o_map=get_map()
    
th.Timer(10,time_food).cancel()
th.Timer(1,time).cancel()


exit()


    








    
