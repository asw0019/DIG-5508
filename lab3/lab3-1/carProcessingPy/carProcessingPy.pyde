# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.a = 20
        self.b = 10
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, self.a, self.b);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
        if self.ypos > height:
            self.ypos = 0
    
#3-1
    def size_increase(self):
#3-2
        if (keyPressed) and (key == ' '):
               self.a +=1

    
myCar1 = Car(color(255, 0, 255), 0, 100, .25)
myCar2 = Car(color(0, 255, 255), 0, 10, 1)
    
def setup():
  size(300,300)

def draw(): 
  background(0)
  myCar1.drive()
  myCar1.display()
  myCar1.size_increase()
  myCar2.drive()
  myCar2.display()
  myCar2.size_increase()
