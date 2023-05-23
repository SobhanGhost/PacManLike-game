# Modules:
import random as r 
import threading as th # For Timers
import os
import winsound as w # For Playing The Sounds
import time as ti
import colorama as c
from math import sqrt

# Variables: global to use them in various functions

global o_map # the original map of the game
global food_index # the list of food indexes on the map
global score # the variable for the score
global t # the variable for playing time
global Diff # the variable for difficulty

# starting values for the variables

Diff = 0
t = 0
score = 1
o_map = ""
food_index = [123, 132, 335, 364, 164, 165] # the constant list for food indexes of the map

# Functions:


def difficulty(Difficulty): # this sets the game difficulty varying:
                            # 01: easy    02. medium
    global Diff
    Diff = Difficulty

################################################################

def get_map(): # this gets the first original map of the game
               # that player, foods and ghosts are in their original form
               
    th.Timer(1,time_1).start() # this line starts the timer to compute total playing time
    global o_map # cause value changes
    o_map = "" # emptying the variable cause this sets the first original map
    ##
    ##
    # the map:
    new_map = """ ----------------------------------
|                                  |
|    G        ########        G    |
| #####       #      #       ##### |
|          # ##  5X  ## #          |
| ######      G      G      ###### |
| ###### # ############## # ###### |
| ###### # #            # # ###### |
| ###### # ############## # ###### |
|                                  |
| ####### # # ######## # # ####### |
|      ###### #Sobhan# ######      |
|      ###### ######## ######      |
|P                                 |
|----------------------------------|

"""
    o_map = new_map # new map
    return new_map

#############################################################

def get_player_co(): # this gets the current coordinates (index) of the player in the map
    # the indexes : line
    # 0-36        : roof
    # 36-71       : 1st
    # 73-108      : 2nd
    # 109-145     : 3rd
    # 147-182     : 4th
    # 184-219     : 5th
    # 221-256     : 6th
    # 258-293     : 7th
    # 295-330     : 8th
    # 332-367     : 9th
    # 369-404     : 10th
    # 406-441     : 11th
    # 443-478     : 12th
    # 480-515     : 13th
    # 517-552     : floor
    for i in o_map:
        if i=="P":
            return o_map.index(i) # returns the players index in the map

#############################################################
        
def get_ghosts_co():# this gets the current coordinates (index) of the ghosts in the map
    g_cos = [] # a list for ghosts indexes to be saved in
    for i in range(len(o_map)):
        if o_map[i] == "G":
            g_cos.append(i)
    return g_cos # returns the players index in the map

###############################################################

def move_player(inp): # this moves the player in the map
                      # in fact this changes the player
                      # index in the map depending on
                      # the user's wish
    
    # inp == second input: second getch:
    # 72 == up , 75 == left , 80 == down , 77 == right
    
    global o_map # cause value changes
    global score # cause value changes
    
    o = o_map # just changing the name for this function (to write lesser)
    p = get_player_co() # getting the player coordinates using mentioned functions
    res = "" # the result string for new generated map
    f = 0 # a simple flag (explaination in further)

    
    if inp==72:  # if the input getch returns 72 meaning going up
        
        if o[p-37]=="#" or o[p-37]=="-" or\
          (o[p-37]==" " and p-37==0): # this checks if is not it possible to go
                                      # if True means we got no moving
                                      # if False player gotta move
            return # returns nothing cause player doesn't move

    
        elif o[p-37]=="G": # this checks if the destination is a ghost
                           # meaning ending the game
            end() # running the end function
            return move_ghosts()
        
        else: # if it was possible to move the player to the destination
            
            if o[p-37]=="X" or o[p-37]=="5": # checks if there is any food on the destination index
                if o[p-36]!="X" and o[p-38]!="5": # checks if is it 5x or not
                    score += 10
                else:
                    score *= 5
                    f = 1 # this flag is used to get this info that
                          # is the 5x food is eaten or not: 1. yes 0. no

            if f == 1: # using the flag to generate the new map
                res = o[:p-38]+" P "+o[p-35:p]+" "+o[p+1:]
            else:
                res = o[:p-37]+"P"+o[p-36:p]+" "+o[p+1:]
            o_map = res # changing the global map variable to the new map              
            return move_ghosts() # this runs the funtion that moves the ghosts and then returns the value coming from it
                                 # (explanation in further)
            

    elif inp==80:  # if the input getch returns 80 meaning going down   
        if o[p+37]=="#" or o[p+37]=="-":
            return
        elif o[p+37]=="G":
            end()
            return move_ghosts()
        else:
        
            if o[p+37]=="X" or o[p+37]=="5":
                if o[p+38]!="X" and o[p+36]!="5":
                    score+=10
                else:
                    score*=5
                    f=1
                    
            if f==1:
                res=o[:p]+" "+o[p+1:p+36]+" P "+o[p+39:]
            else:
                res=o[:p]+" "+o[p+1:p+37]+"P"+o[p+38:]
            o_map=res                
            return move_ghosts()
        

    elif inp==77:  # if the input getch returns 77 meaning going right
        if o[p+1]=="#" or o[p+1]=="|":
            return
        elif o[p+1]=="G":
            end()
            return move_ghosts()
        else:
            if o[p+1]=="X" or o[p+1]=="5":
                if o[p+2]!="X":
                    score+=10
                else:
                    score*=5
                    f=1
                    
            if f==1:
                res=o[:p]+" P"+" "+o[p+3:]
            else:
                res=o[:p]+" P"+o[p+2:]
            o_map=res
            return move_ghosts()
        
        
    elif inp==75:  # if the input getch returns 75 meaning going left
        if o[p-1]=="#" or o[p-1]=="|":
            return
        elif o[p-1]=="G":
            end()
            return move_ghosts()
        else:
            if o[p-1]=="X":
                if o[p-2]!="5":
                    score+=10
                else:
                    score*=5
                    f=1
                    
            if f==1:
                res=o[:p-2]+" P"+" "+o[p+1:]
            else:
                res=o[:p-1]+"P"+" "+o[p+1:]
            o_map=res
            return move_ghosts()

###############################################################
        
def easy_move(move,ghost_co): # this moves the ghosts randomly as the project says
                              # in fact this does the easy level of the game
                              # P.S: this in fact checks that if the given movement
                              # for the given ghost coordinates is possible
    global o_map # cause value changes

    # move == given movement: 1 == up , 2 == down , 3 == right , 4 == left
    # ghost_co == given ghost coordinates
    
    m = move # just changing the name for this function (to write lesser)
    o = o_map # just changing the name for this function (to write lesser)
    g = ghost_co # just changing the name for this function (to write lesser)
    
    if m==1: # if the given move is 1 meaning going up
        # this blocks actually are defined as a recursive function
        # cause it recalls itself in its body

        if o[g-37]=="#" or o[g-37]=="-" or\
           o[g-37]=="G" or 0<=g-37<=36 or\
           g-37 in food_index: # this checks if the given move is possible
            
            return easy_move(2,g) # calling itself to rerun
        else:
            
            return m # if possible, it returns the movement
        
    elif m==2:# if the given move is 2 meaning going down
        
        if o[g+37]=="#" or o[g+37]=="-" or\
           o[g+37]=="G" or 0<=g + 37<=36 or\
           g+37 in food_index:
            
            return easy_move(3,g)
        
        else:
            return m
        
    elif m==3: # if the given move is 3 meaning going right
        
        if o[g+1]=="#" or o[g+1]=="|" or\
           o[g+1]=="G" or 0<=g+1<=36 or\
            g+1 in food_index:
            
            return easy_move(4,g)
        
        else:
            return m
        
    elif m==4: # if the given move is 4 meaning going left
        if o[g-1]=="#" or o[g-1]=="|" or\
           o[g-1]=="G" or 0<=g-1<=36 or\
           g-1 in food_index:
            
            return easy_move(1,g)
            
        else:
            return m

##################################################################

def move_ghosts(): # this moves the ghosts in the map
                   # in fact this changes the ghosts
                   # indexes in the map depending on
                   # the game's difficulty
    global o_map # cause value changes
    
    r_move = [] # a list containing numbers 1-4 as movements
    res = "" # a new string for the new generated map to be saved in
    
    o = o_map # just changing the name for this function (to write lesser)
    res = o # getting the old map to the string to work with it
    
    if o == "": # this checks if game has ended
        
        return res
    
    l_gh=get_ghosts_co() # this gets the ghosts coordinates adding them to a list
                      # to work with it

    for i in range(4): # this generate 4 random movements as described before
        r_move.append(r.randint(1,4))
    
    for i in range(4): # this is the moving block
                       # in this block in fact
                       # the ghosts are moved depending on the difficulty
                       
        temp = l_gh[i] # a temperory variable in which is the ghost index taking turn
        
        if Diff==2: # this checks the difficulty of the game as described before
            t_move = medium_ghosts(temp) # calling the medium function getting the move
        else:
            t_move = easy_move(r_move[i],temp) # calling the easy function getting the move
        
            # as described before:
            
        if t_move == 1: # if the given move is 1 meaning going up
            # this block is like the moving player code found and also described at line 116
            # the only difference is that this blocks have no codes relating to the foods
            
            if res[temp-37]=="#" or res[temp-37]=="-": # checks if it is possible
                pass
            else:
                if res[temp-37]!="G" and res[temp-37]!="P": # P.S: this conditions have been defined somewhere else...
                    res=res[:temp-37]+"G"+res[temp-36:temp]+" "+res[temp+1:]
                
                
        elif t_move==2: # if the given move is 2 meaning going down
            if res[temp+37]=="#" or res[temp+37]=="-":
                pass
            else:
                if res[temp+37]!="G":
                    res=res[:temp]+" "+res[temp+1:temp+37]+"G"+res[temp+38:]

        elif t_move==3: # if the given move is 3 meaning going right
            if res[temp+1]=="#" or res[temp+1]=="|":
                pass
            else:
                if res[temp+1]!="G":
                    res=res[:temp]+" "+"G"+res[temp+2:]
                
        elif t_move==4: # if the given move is 4 meaning going left
            if res[temp-1]=="#" or res[temp-1]=="|":
                pass
            else:
                if res[temp-1]!="G":
                    res=res[:temp-1]+"G"+" "+res[temp+1:]
            

    o_map = res # changing the global map variable to the new map   
    return res
######################################################################

def Score(): # this just returns the score
    
    return "Your Score: %i"%(score)

#######################################################################

def time_food(): # this function changes the food index each 10 seconds
    
    global o_map # cause value changes
    
    if o_map!="":
        for i in food_index: # this removes the foods from the map
            
            if i!=164 and o_map[i]=="X":
                o_map=o_map[:i]+" "+o_map[i+1:len(o_map)]
                
        if o_map[164]=="5": 
            o_map=o_map[:164]+"  "+o_map[166:len(o_map)]
            
        r_f_index=r.randint(0,4) # a random int that represents a random index for the food
                                 # to be displayed

        for i in food_index: # this adds the foods into the map depending on the random index
            
            if o_map[food_index[r_f_index]]==" " and r_f_index!=4:
                o_map=o_map[:food_index[r_f_index]]+"X"+o_map[food_index[r_f_index]+1:len(o_map)]
            elif o_map[food_index[r_f_index]]==" " and r_f_index==4:
                o_map=o_map[:food_index[r_f_index]]+"5X"+o_map[food_index[r_f_index]+2:len(o_map)]
            if "X" in o_map:
                break
                
    th.Timer(10,time_food).start() # this starts the timer for the 10 second process
    if o_map=="": # this checks if the game has ended
                  # stops the timer if True, else pass
        th.Timer(10,time_food).cancel()

##############################################################################
        
def end(): # this is run when the game ends
           # in fact it stops all the timers and the processes
           
    global o_map # cause value changes
    
    music(1) # this plays the game over sound
    ti.sleep(1.5) # a waiting time just making it more
                  # reasonable
    
    print("""
      GGGGGGGGGGGGGGGGGGGGGGGGGG   AAAAAAAAAAAAAAAAAAAA   MMMMMMMMMMMMMMMMMMMMMMMMMMM   EEEEEEEEEEEEEEEEEEEEEEEEEEE
      GGGGGGGGGGGGGGGGGGGGGGGGGG   AAAAAAAAAAAAAAAAAAAA   MMMMMMMMMMMMMMMMMMMMMMMMMMM   EEEEEEEEEEEEEEEEEEEEEEEEEEE
      GGG                          AAA              AAA   MMM         MMM         MMM   EEE
      GGG                          AAA              AAA   MMM         MMM         MMM   EEE
      GGG                          AAA              AAA   MMM         MMM         MMM   EEE
      GGG                          AAA              AAA   MMM         MMM         MMM   EEE
      GGG                          AAA              AAA   MMM         MMM         MMM   EEE
      GGG         GGGGGGGGGGGGGG   AAAAAAAAAAAAAAAAAAAA   MMM         MMM         MMM   EEEEEEEEEEEEEEEEEE
      GGG         GGGGGGGGGGGGGG   AAAAAAAAAAAAAAAAAAAA   MMM         MMM         MMM   EEEEEEEEEEEEEEEEEE
      GGG    OOOOOOOOO    GGGGGG   AAA  VV      VV  AAA   MMM EEEEEEE MMM EEEEEEE MMM   EEE  RRRRRR
      GGG    OO     OO    GGGGGG   AAA   VV    VV   AAA   MMM EE      MMM         MMM   EEE  R    R
      GGG    OO     OO    GGGGGG   AAA    VV  VV    AAA   MMM EEEE    MMM         MMM   EEE  RRRRRR
      GGG    OO     OO    GGGGGG   AAA     VVVV     AAA   MMM EE      MMM         MMM   EEE  R   R
      GGG    OOOOOOOOO    GGGGGG   AAA      VV      AAA   MMM EEEEEEE MMM EEEEEEE MMM   EEE  R    R
      GGG                 GGGGGG   AAA              AAA   MMM         MMM         MMM   EEE  R     R
      GGGGGGGGGGGGGGGGGGGGGGGGGG   AAA              AAA   MMM         MMM         MMM   EEEEEEEEEEEEEEEEEEEEEEEEEEE
      GGGGGGGGGGGGGGGGGGGGGGGGGG   AAA              AAA   MMM         MMM         MMM   EEEEEEEEEEEEEEEEEEEEEEEEEEE
""") # printing the 'game over' graffiti
    
    sc=save_file() # this runs the file saving function as described further
    
    print("\n") # two additional lines just to make it more beatiful :)

    for i in sc: # this prints the best score, best playtime, and last score of the game
        
        print(i,sc[i])
        
    o_map="" # emptying the original global map variable to end the game and its functions
    
    th.Timer(1,time_1).cancel() # stopping the timer for counting the seconds
    
    return o_map
############################################################################

def time_1(): # this counts the seconds to represent the playtime
    
    global t # cause value changes
    
    t+=1 # 1 second per run
    
    th.Timer(1,time_1).start() # this starts the timer for counting the seconds
    
    if o_map=="": # this checks if the game has ended
                  # stops the timer if True, else pass
        th.Timer(1,time_1).cancel()
    
###########################################################################
def save_file(): # this saves the records to a txt file
    temp = [] # a temp' list to store the previous records in it
    temp1 = [] # a temp' list to store the info of the records (which number represents what)
    sc_l = [] # this represents the number of the records

    b_s = 0 # represents best score
    b_p = 0 # represents best playtime
    l_s = 0 # represents last score
    
    res = "" # the result string that will be saved in the file
    res_1 = [] # the result list that will be used to print
    
    f = open("Save\\Score.txt","r") # openin the file for reading the info (making a file handler)
    file_l = (f.readlines()).copy() # getting the records from the file using file handler
    f.close() # closing the file handler
    
    f = open("Save\\Score.txt","w") # openin the file for writing the info (making a file handler)
    
    if file_l == []: # this checks if the file is empty
                   # if True it writes the new records to the file
                   # and adds them into the result list
        f.write("Best Score: %i \n"%(t+score))
        f.write("Best PlayTime: %i \n"%(t))
        f.write("Last Score: %i \n"%(t+score))

        res_1.append(t+score)
        res_1.append(t)
        res_1.append(t+score)
        
    else: # this replaces the new records with the old ones
        for i in file_l: # this transforms  the records from the file handler
                         # into the lists mentioned above
                         
            temp = i.split() 
            sc_l.append(int(temp[2]))
            temp1.append(temp[0]+temp[1])
#####################################
        if sc_l[0]<(score+t): # this checks if the new score is better than the old one
                              # if True replaces them, if not doesn't bother itself
            b_s = score+t
        else:
            b_s = sc_l[0]
#####################################
        if sc_l[1]<t: # this checks if the new playtime is better than the old one
                      # if True replaces them, if not doesn't bother itself
            b_p = t
        else:
            b_p =sc_l[1]
#####################################
        l_s = score+t # this writes the last score

    
        res = """Best Score: %i
Best PlayTime: %i
Last Score: %i"""%(b_s,b_p,l_s) # creating the new info to be written into file
            
        f.write(res) # writes the info
    f.close() # closes the file

    if res_1 != []: # this checks if the file was empty

        return dict(zip(temp1,res_1))
    
    res = [b_s,b_p,l_s] # the result list
    
    return dict(zip(temp1,res))
    
#######################################################   

def music(start_stop): # this plays music :}
    
    s = start_stop # just changing the name for this function (to write lesser)
    
    if s == 0: # this checks if the game is started or ended
        w.PlaySound("Music\\Main_Theme.PCM",w.SND_ASYNC) # starting music (theme song)
    else:
        w.PlaySound("Music\\Game_Over.PCM",w.SND_ASYNC) # game over music

#########################################################
        
def medium_ghosts(ghost_co): # this makes the ghosts to move closer to the player
                             # in fact this represents the medium difficulty
                             # it computes the destination index aiming for the player using phythagoras law:
                             # a^2 == b^2 + c^2 :: a == rad( b^2 + c^2 )
                             # that in here we got:
                             # d == rad( (yp - yg)^2 + (xp - xg)^2 )
                             
    # ghost_co == the given ghost coordinates(index)
    
    global o_map # cause value changes
    
    p = get_player_co() # gets the player coordinates

 
    g = (ghost_co%37,ghost_co//37) # getting the x,y of the given ghost coordinates
    p_co = (p%37,p//37) # getting the x,y of the player coordinates
    
    fis = lambda x,y: sqrt((p_co[0] - x)**2+(p_co[1] - y)**2) # creating a lambda for phythagoras law
    
    l_move = [] # this list is the list that the possible shorter movements are stored in
    l_dis = [] # this list is the list that the possible shorter distances are stored in
    t_ind = {} # this dictionary represents the movements [1 up, 2 down, 3 right, 4 left] as keys
               # and the destination index as value of the keys
               
    g_p = fis(g[0],g[1]) # this gets the distance between the ghost and player
    
    t1 = 0 # this temp' variable represents the distances to get the shortest

    # this ifs gets the distances and the movements putting then into the mentioned dictionary
    
    if o_map[ghost_co-37]==" " or o_map[ghost_co-37]=="P":
        t_ind[1]=ghost_co-37
        
    if o_map[ghost_co+37]==" " or o_map[ghost_co+37]=="P":
        t_ind[2]=ghost_co+37
        
    if o_map[ghost_co-1]==" " or o_map[ghost_co-1]=="P":
        t_ind[4]=ghost_co-1
        
    if o_map[ghost_co+1]==" " or o_map[ghost_co+1]=="P":
        t_ind[3]=ghost_co+1
    
    for j in t_ind: # this block gets the shortest distances
        t1=fis(t_ind[j]%37,t_ind[j]//37)
        
        if t1<=g_p:
            l_move.append(j)
            l_dis.append(t1)
            
    if l_move==[]: # this runs if there is no shorter option
        l_move.append(r.randint(1,4))
    
    if len(l_move)==1:
        return l_move[0]
    else:
        return l_move[l_dis.index(min(l_dis))]

####################################################################

def color(): # this presents the coloring process of the map
    
    l_color=["RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"]
    return l_color[r.randint(0,len(l_color)-1)]

def loading(t):
    if t==0:
        for i in o_map: # printing the map in yellow
            print(i,end="")
            ti.sleep(0.001)
