import keyboard


def move_bird(bird_y_pos):
    """
    Moves bird based on user inputs
    Moves bird 1 coordinates upward if SPACE is pressed
    Otherwise moves bird 1 coordinate downward
    """
    global upwards 
    bird_y_pos=bird_y_pos+1                                                                                                                              
    
    #Using a variable so that input is detected only after a certain wait time
    can_be_pressed = True                      
    if keyboard.is_pressed("space") and can_be_pressed:
        can_be_pressed= False
        bird_y_pos = max(1,bird_y_pos-2)
    if upwards:
        bird = "\o/" 
        upwards = False
    else:
        bird = "-o-"
        upwards = True
    
    print(pos(bird_x_pos,bird_y_pos)+bird)
    return bird_y_pos

def pos (x:int,y:int):
    """
    Returns ANSI cursor code for given coordinates
    """
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

bird_x_pos = 20
upwards = True
                                                                                                             
                         