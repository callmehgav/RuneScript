
def ardyKnights(self):
    #click coin poich
    clickFirstInvSlot(self)
    #wait random amount of time
    time.sleep(random.uniform(.6,1.2))
    #move mouse to knight
    moveMouse(randomInSquare(1200), randomInSquare(453))
    time.sleep(random.uniform(.6,1.2))
    #click knights until coinpouch is full
    for x in range(returnInt(23,26)):
        quickAFRandomAutoClicker(self)

def mineSulfur(self):
    dropInventory(self)
    moveMouse(returnInt(739, 745), returnInt(243,249))
    time.sleep(random.uniform(.6,1.2))
    mouse.click(self.button) 
    # tenPercentChanceOfE()
    time.sleep(random.uniform(75,100))


def canifisAgilCourse(self):

    #1 climb tree
    mouse.click(self.button)
    time.sleep(random.uniform(7, 8))
    #2 run to next spot
    moveMouse(returnInt(670, 710), returnInt(387,433))
    time.sleep(random.uniform(.6,.8))
    mouse.click(self.button)
    time.sleep(1.1)
    #2.5 double click to prevent misplacement
    moveMouse(returnInt(686, 700), returnInt(455,480))
    waitClickWait(self,5,6)
    # on house 2
    moveMouse(returnInt(567, 587), returnInt(529,569))
    waitClickWait(self,6,7)
    #3 on house 3
    moveMouse(returnInt(544, 558), returnInt(640,678))
    #4
    waitClickWait(self,7,8)
    moveMouse(returnInt(664, 683), returnInt(699,735))
    #5
    waitClickWait(self,7,8)
    moveMouse(returnInt(736, 755), returnInt(608,624))
    #5
    waitClickWait(self,8,9)
    moveMouse(returnInt(1033, 1046), returnInt(547,557))
    #6
    waitClickWait(self,8,9)
    moveMouse(returnInt(743, 750), returnInt(548,555))
    #6.5 this pause will be used in event of camera miss alignment
    time.sleep(.5)
    mouse.click(self.button)
    moveMouse(returnInt(743, 750), returnInt(542,549))
    #this will be used to sync back up with the track
    mouse.click(self.button)
    time.sleep(random.uniform(3,4))
    mouse.click(self.button)
    time.sleep(random.uniform(2,3))
    mouse.click(self.button)
    time.sleep(random.uniform(2,3))
    mouse.click(self.button)
    time.sleep(random.uniform(2,3))
    mouse.click(self.button)
    time.sleep(random.uniform(2,3))
    #from the corner of bank move to finish
    moveMouse(returnInt(583, 600), returnInt(424,436))
    #7
    time.sleep(random.uniform(0.6, 1))
    waitClickWait(self,5,6)
    moveMouse(returnInt(645, 662), returnInt(450,462))
    time.sleep(random.uniform(0.6, 1))

