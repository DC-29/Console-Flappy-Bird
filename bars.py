class TopBar():
    """
    Class handling the obstacle pillars hanging from the top
    Attributes:
        Position: X and Y coordinates of the top of the pillar
        State: How much of the pillar needs to be shown
        Length: Size of the pillar

    Each pillar is made of 3 components:
        The right side made of vertical lines
        The centre made of two hyphens
        The left side made of vertical lines
    """


    straight_line = '|'
    states = ["Full","Centre","End"]
    
    def __init__(self, position:tuple,state:str,length:int):
        self.random_num_t=length
        self.position_x,self.position_y = position
        if state == self.states[0]:
            #All three components are visible. Each printed one after another
            self.right = self.print_bar_right(0)
            self.centre = self.print_bar_centre(1)
            #Since the centre takes 2 spots, offset is increased by 2
            self.left = self.print_bar_left(3)
        elif state == self.states[1]:
            #The right component is not visible
            self.right = ""
            self.centre = self.print_bar_centre(0)
            self.left = self.print_bar_left(2)
        else:
            #Only the left component is visible
            self.right = ""
            self.centre=""
            self.left = self.print_bar_left(0)
            
        
    def print_bar_right(self,offset:int):
        bar = ""
        for i in range(self.random_num_t):
            bar+=pos(self.position_x+offset,self.position_y)+self.straight_line
            #Y coordinate is increased because the position attribute tells the position of the top of the pillar.
            #The pillar extends downwards from the position
            self.position_y+=1
        
        self.position_y-=self.random_num_t
        
        
        return bar
    
    def print_bar_left(self,offset:int):
        bar = ""
        for i in range(self.random_num_t):
            bar+=pos(self.position_x+offset,self.position_y)+self.straight_line
            self.position_y+=1
       
        self.position_y-=self.random_num_t
        return bar

    def print_bar_centre(self,offset:int):
        bar= ""
        bar+=pos(self.position_x+offset,self.position_y+self.random_num_t)+'--'
        return bar


class BottomBar():
    """
    Class handling the obstacle pillars on the ground
    Attributes:
        Position: X and Y coordinates of the bottom of the pillar
        State: How much of the pillar needs to be shown
        Length: Size of the pillar

    Each pillar is made of 3 components:
        The right side made of vertical lines
        The centre made of two hyphens
        The left side made of vertical lines
    """

    straight_line = '|'
    states = ["Full","Centre","End"]
    
    def __init__(self, position:tuple,state:str,length:int):
        self.random_num_t=length
        self.position_x,self.position_y = position
        if state == self.states[0]:
            self.right = self.print_bar_right(0)
            self.centre = self.print_bar_centre(1)
            self.left = self.print_bar_left(3)
        elif state == self.states[1]:
            self.right = ""
            self.centre = self.print_bar_centre(0)
            self.left = self.print_bar_left(2)
        else:
            self.right = ""
            self.centre=""
            self.left = self.print_bar_left(0)
            
        
    def print_bar_right(self,offset:int):
        bar = ""
        for i in range(self.random_num_t):
            bar+=pos(self.position_x+offset,self.position_y)+self.straight_line
            #Y coordinate is decreased because the position attribute marks the bottom of the pillar
            #The pillar extends upwards from the position
            self.position_y-=1
        self.position_y+=self.random_num_t
        
        
        return bar
    
    def print_bar_left(self,offset:int):
        bar = ""
        for i in range(self.random_num_t):
            bar+=pos(self.position_x+offset,self.position_y)+self.straight_line
            self.position_y-=1
        self.position_y+=self.random_num_t
        return bar

    def print_bar_centre(self,offset:int):
        bar= ""
        bar+=pos(self.position_x+offset,self.position_y-self.random_num_t)+'--'
        return bar

def pos (x:int,y:int):
    """
    Returns ANSI cursor code for given coordinates
    """
    return '\x1b[' + str(y) + ';' + str(x) + 'H'