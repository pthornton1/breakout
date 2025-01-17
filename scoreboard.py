from turtle import Turtle

FONT = ("Courier",80, "normal")
COLOR = "White"
L_POSITION = (-100,200)
R_POSITION = (100,200)
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.hideturtle()
        self.penup()   
        
        self.l_score = 0
        self.r_score = 0
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.goto(L_POSITION)
        self.write(self.l_score, align=ALIGNMENT, font=FONT) 
        self.goto(R_POSITION)
        self.write(self.r_score, align=ALIGNMENT, font=FONT) 
        
    def score(self,player):
        
        if player == "left":
            self.l_score += 1
        else:
            self.r_score += 1
            
        self.write_score()
        
              
    