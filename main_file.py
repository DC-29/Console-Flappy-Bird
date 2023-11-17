import random
import os
import time
import keyboard
from bars import TopBar, BottomBar
from bird import move_bird


def pos (x:int,y:int):
    """
    Returns ANSI cursor code for given coordinates
    """
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

def create_encloseing_box():
    """
    Prints out the bounding box for the gameplay
    """
    y=2
    for i in range(10):
        print(pos(1,y)+'|')
        y+=1
    y=2
    for i in range(10):
        print(pos(88,y)+'|')
        y+=1
    print(pos(2,1)+'_'*86)
    print(pos(2,bottom_lim+1)+'_'*86)

def gen_bars(n:int,position:int,lengths:list,orientation:list):
    """
    Generates bars with the first bar starting from the position attribute
    Attributes:
        n : Number of bars
        position : x-coordinate of the first bar
        lengths : lengths of the bars as a list. The size of the list must be equal to the number of bars
        orientation : orientation of bars as a list. The size of the list must be equal to number of bars
                      list must contain only 1s and 0s, where 1 denotes bottom bar and 0 denotes top bar
    """
    bars_right = []
    bars_centre = []
    bars_left = []
    

    
    for i in range(n):
        #Checks for the orientation and creates a new bar based on it.
        #Adds the right side, centre and the left side of the bars into separate lists
        if (orientation[i]==0):
            top = TopBar((position,2),"Full",lengths[i])
            bars_right.append(top.right)
            bars_centre.append(top.centre)
            bars_left.append(top.left)
            
            
        elif (orientation[i]==1):
            bot = BottomBar((position,bottom_lim),"Full",lengths[i])
            bars_right.append(bot.right)
            bars_centre.append(bot.centre)
            bars_left.append(bot.left)

        position+=dist_btw_bars

    return bars_right,bars_centre,bars_left





def calculate_hitspot(n:int,position:int,lengths:list,orientations:list):
    """
    Returns the Y-coordinate of the end of the bar that has the same X-coordinates as the bird
    Attributes:
        n : Number of bars
        position : x-coordinate of the first bar
        lengths : lengths of the bars as a list. The size of the list must be equal to the number of bars
        orientation : orientation of bars as a list. The size of the list must be equal to number of bars
                      list must contain only 1s and 0s, where 1 denotes bottom bar and 0 denotes top bar
    """
    hit_ori = 0
    for i in range(n):
        #The following addition/subtraction have been made to the position attribute because one bar takes up 4 units on X coordinate
        if position-2<=bird_x_pos<=position+3:
            if orientations[i] == 0:
                hitspot = lengths[i]+2
                hit_ori=0
                break
            elif orientations[i] == 1:
                hitspot = bottom_lim - lengths[i] 
                hit_ori=1
                break
        else:
            position+=dist_btw_bars
    else:
        return None,None
    return hit_ori,hitspot



def lose_screen():
    """
    Prints out the lose screen and the score
    """
    os.system('cls')
    create_encloseing_box()
    print(pos(41,6)+"You Lose")
    print(pos(41,7)+f"Score: {score}")
    time.sleep(5)

def title_screen():
    """
    Prints out the title screen
    Game begins once the player presses the enter key
    """
    os.system('cls')
    create_encloseing_box()
    print(pos(41,6)+"ASCII BIRD")
    print(pos(36,7)+"Press enter to begin:")
    input()


def main(first_bar_pos,second_bar_pos, first_length,lengths, first_ori, orientations, bird_y_pos):
    """
    Contains the main gameplay loop
    Continuously generates bars, decreasing the position everytime so they appear to move

    Attributes:
        first_bar_pos: X coordinates of the start of the first bar
        second_bar_pos: X coordinates of the start of the second bar. 
                        Used to call gen_bars function to generate all bars except the first
        first_length: Length of the first bar
        lengths: List containing lengths of the bars, second bar onwards
        first_ori: Orientation of the first bar
        orientationsL List containing orientations of the bars, second bar onwards
        bird_y_pos: Initial Y Coordinates of the bird
    """
    title_screen()
    i=0
    global score
    while True:
        #Clearing the screen before every loop
        os.system('cls')
        
        create_encloseing_box()

         

        b_r,b_c,b_l = gen_bars(num_of_bars,second_bar_pos,lengths,orientations)
        hit_ori,hitspot = calculate_hitspot(num_of_bars,second_bar_pos,lengths,orientations)
        
        bird_y_pos = move_bird(bird_y_pos) 
    
        
        #Depending on the loop count, we change the first bar's state between full, centre and end.
        #Then we shift all other bars one coordinate to the left
        if i%8==0:
            if first_ori == 0:
                first_bar = TopBar((first_bar_pos,2),"Full",first_length)
            elif first_ori == 1:
                first_bar = BottomBar((first_bar_pos,bottom_lim),"Full",first_length)
            print(first_bar.right+first_bar.centre+first_bar.left)
            score += 1
            
            
            
        
        
        elif i%8 ==1:
            if first_ori == 0:
                first_bar = TopBar((first_bar_pos,2),"Centre",first_length)
            elif first_ori == 1:
                first_bar = BottomBar((first_bar_pos,bottom_lim),"Centre",first_length)
            print(first_bar.right+first_bar.centre+first_bar.left)
            
            

        
        
        elif i%8==2:
            if first_ori == 0:
                first_bar = TopBar((first_bar_pos,2),"End",first_length)
            elif first_ori == 1:
                first_bar = BottomBar((first_bar_pos,bottom_lim),"End",first_length)
            print(first_bar.right+first_bar.centre+first_bar.left)
            

        
        #Now the first bar has gone off-screen and the rest of the bars still move towards left
        elif i%8 < 6:
            pass

        
        #We begin showing another bar towards the rightmost end, showing one more component (right, centre, left) after each loop
        elif i%8 == 6:
            if first_ori == 0:
                last_bar = TopBar((86,2),"Full",first_length)
            elif first_ori == 1:
                last_bar = BottomBar((86,bottom_lim),"Full",first_length)
            print(last_bar.right)
            
            

        
        elif i%8==7:
            if first_ori == 0:
                last_bar = TopBar((84,2),"Full",first_length)
            elif first_ori == 1:
                last_bar = BottomBar((84,bottom_lim),"Full",first_length)
            print(last_bar.right+last_bar.centre)
            
            #We have reached the screen from which we started
            #Now the ex second bar is the first one and the ex first bar is the last one
            temp_length = first_length
            first_length = lengths[0]
            lengths = lengths[1:]+[temp_length]

            temp_orientation = first_ori
            first_ori = orientations[0]
            orientations = orientations[1:] + [temp_orientation]

            first_bar_pos = 3
            second_bar_pos = first_bar_pos+dist_btw_bars


        
        print("".join(b_r)+"".join(b_c)+"".join(b_l))
        second_bar_pos -= 1


        #Checking if the bird's Y coordinates lie in the hitspot
        if hitspot:
            if hit_ori==0 and bird_y_pos<=hitspot:
                break
            elif hit_ori == 1 and bird_y_pos>=hitspot:
                break
        if bird_y_pos>bottom_lim or bird_y_pos<2:
            break

        time.sleep(wait_time)
        i+=1

    time.sleep(5)
    lose_screen()



wait_time = 0.65
lengths = [4,2]
orientations = [0,1]
for i in range(8):
    lengths.append(random.randint(1,5))
    orientations.append(random.randint(0,1))
first_length = 2
first_ori = 0
dist_btw_bars = 8
bottom_lim = 10

bird_x_pos = 20
upwards = True
bird_y_pos=5

first_bar_pos = 3
second_bar_pos = first_bar_pos+dist_btw_bars

num_of_bars = 10
os.system('cls')
create_encloseing_box()

score = -1

main(first_bar_pos,second_bar_pos,first_length,lengths,first_ori,orientations, bird_y_pos)
print(pos(1,500)+'--')

