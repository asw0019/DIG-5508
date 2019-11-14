#3-3
class Tree(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, yspeed):
        self.c = c
        self.xpos = xpos
        self.yspeed = yspeed
        self.a = 40
        self.b = 10
      #  self.myList = []
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, self.a, self.b);
    
    def grow(self):
        frameRate(10)
        self.ypos = height
        self.b += self.yspeed
        if self.b > height:
            self.xpos += 5
            self.b = 0
            if self.xpos > width:
                self.xpos = 0
    

    def size_increase(self):

        if (keyPressed) and (key == ' '):
               self.a +=1

myList = []   
myTree1 = Tree(color(150,75,0), random(300), random(5))
myTree2 = Tree(color(150,25,0), random(300), random(5))
myList.append(myTree1)
myList.append(myTree2)
    
#3-4
class Sun(object):
    
    def __init__(self, c, x, y):
        self.c = c
        self.a = 25
        self.b = 25
        self.myList = []
        self.x = x
        self.y = y
    
    def display(self):
        ix = width - mouseX
        iy = height - mouseY
        fill(255,255,0)
        ellipse(self.x, self.y, width/2, height/2)
        stroke(0)
        ellipseMode(CENTER)
    
    def updatePosition(self, x, y):
        x = x.self
        y = y.self
    
    def grow(self):
        frameRate(10)
        self.xpos = width
        self.ypos = height
        ellipseMode(CENTER)
        ellipse(self.a, self.b, 20, 30)
        
mySun = None

def mousePressed():
    global mySun
    mySun = Sun(color(255,255,0), mouseX, mouseY)

class Cloud(object):
    
        def __init__(self, c):
           self.c = c
           self.a = 50
           self.b = 50
           self.myList = []
           
        def display(self):
            shape = ellipse
            fill(self.c)
            if keyPressed:
                shape = rect
            if shape == rect:
                rect(50,50,100,70)
            else:
                ellipse(50,50,100,70)

   

myCloud = Cloud(color(128,128,128))


def setup():
  size(300,300)
  noStroke()
    
def draw(): 
  background(204)
  if mySun != None:
     mySun.display()
  myCloud.display()
  for i in myList:
      i.grow()
      i.display()
      i.size_increase()
