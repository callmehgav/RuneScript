import time
import threading
import numpy as np
from pynput.mouse import Button as pyB, Controller
from pynput.keyboard import Listener, KeyCode, Key, Controller as C
import random
from time import sleep
from tkinter import *

everyMinute = 60
buttonLeftClick = pyB.left
buttonRightClick = pyB.right
start_stop_key = KeyCode(char='=')
exit_key = KeyCode(char='+')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("Started Clicking")
        self.running = True

    def stop_clicking(self):
        print("Stopped Clicking")
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
    def run(self):
        counter = 0
        while self.program_running:
            counter = 0
            while self.running:
                #if (counter < 215):
                    #counter = counter +1
                    #print(counter)
                #@@@@@@@@@@@@@@@@@@@@@
            #cooking-------------------------------cooking
                #catchNBankKarambwans(self)
                #hosidiousCookingBot(self)
            #crafting-------------------------------crafting
                #cookSeaweedAtFT(self)
                #edgevilleFurnace(self)
                #craftOrFletch(self)
                #superGlassmake(self)
            #firemaking-------------------------------firemaking
                #burnInv(self)
            #agility-------------------------------agility
                #canifisAgilCourse(self)
                seersCourse(self)
            #woodcutting-------------------------------woodcutting
                #clickAndFletchIntoShafts(self)
                #clickAndFletchIntoBows(self)
                #cutFossilIslandTreesAndBank(self)
                #cutFossilIslandTest(self)
                #yewsAndBank(self)
            #fletching-------------------------------fletching
                #broads(self)
                #teakCutNFletch(self)
                #craftOrFletch(self)
                #stringBows(self)
            #mining-------------------------------mining
                #threeTickMiningGranite(self)
                #mlmTopFloor(self)
                #mineIronOreAndBank(self)
                #mineSandstone(self)
                #iron(self)
                #mineSulfur(self)
                #miningCraftingBot(self)
            #magic-------------------------------magic
            #range-------------------------------range
            #melee-------------------------------melee
                #amaniteCrabs2(self)
                #amaniteCrabs3(self)
            #multiUse-------------------------------multiUse
                #quickRandomAutoClicker(self)
                #clickAndDropInv(self)
                #openPacks(self)
                #dropInventory(self)
                #quickAFRandomAutoClicker(self)
                #highAlch(self)
            #fishing-------------------------------fishing
                #counter = minnows(self,counter)
                #fishAndDropInv(self)
                #threeTickFish(self)
            #thieving-------------------------------thieving
                #ardyKnights(self)
                #fruitStalls(self)
            #smithing-------------------------------smithing
                #walkingSteelBlastFurnace(self)
                #goldBlastFurnace(self)
                #BlastFurnaceForMithBars(self)
                #BlastFurnaceForAddyBars(self)
                #BlastFurnaceForSteelBars(self)
                #runCannonBalls(self)
            #construction-------------------------------construction
                #runPlanks(self)
################################################################
####################SUPPORT METHODS#############################
################################################################
def tenPercentChanceOfE():
    # 10% chance of storing ore
    randPercent = np.random.randint(1, 101)
    if randPercent > 80:
        #rint('e clicked')
        keyboard.press('e')
        keyboard.release('e')

def returnInt (minInt, maxInt):
    return np.random.randint(minInt, maxInt)

def moveMouse(x,y):
    mouse.position = (x, y)

def randomInSquare(num):
    return returnInt(num, num+10)


def clickEsc(self):
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(random.uniform(.2,.4))
def clickSpace(self):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(random.uniform(.2,.4))
################################################################
####################BOTS########################################
################################################################
def quickRandomAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(10,15)
    # tenPercentChanceOfE()
    time.sleep(delay)
def quickAFRandomAutoClicker(self):
    mouse.click(self.button)
    # tenPercentChanceOfE()
    time.sleep(random.uniform(.82,.94))
def broads(self):
    # click inv spot one
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.68, .72))  # random.uniform(0.3, .5)
    mouse.click(self.button)
    # click inv spot 5
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[2], rowNums[3]))
    time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
    mouse.click(self.button)  # start herb animation
#assumes set on all with glass in bank spot 1 and pipe in inv slot 1
#do first inv before starting to set space bar
def craftOrFletch(self):
    time.sleep(random.uniform(.2,.4))
    clickSecondInvSlot(self)
    clickFirstBankSpot(self)
    time.sleep(random.uniform(.2,.4))
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(random.uniform(.2,.4))
    clickFirstInvSlot(self)
    clickSecondInvSlot(self)
    time.sleep(random.uniform(.8,.9))
    #keyboard.press('2')
    #keyboard.release('2')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(random.uniform(45,55))
    #clickLilIslandBank(self)
    clickFishingGuildBank(self)
def stringBows(self):
    clickSecondInvSlot(self)
    clickFirstBankSpot(self)
    clickSecondBankSpot(self)
    time.sleep(random.uniform(.2,.4))
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(random.uniform(.2,.4))
    clickFirstInvSlot(self)
    clickLastInvSlot(self)
    time.sleep(random.uniform(.2,.4))
    #keyboard.press('2')
    #keyboard.release('2')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(random.uniform(18,24))
    #clickLilIslandBank(self)
    clickFishingGuildBank(self)
def spec(self):
    moveMouse(returnInt(1257,1267),returnInt(200,206))
    waitClickWait(self,.2,.4)
def toggleRun(self):
    moveMouse(returnInt(1232,1246),returnInt(172,182))
    waitClickWait(self,.2,.4)
def yewsAndBank(self):
    #empty inv
    emptyInventoryInBank(self)
    clickEsc(self)

    if(returnInt(0, 10)<5):
        spec(self)
    #Click first yew tree
    moveMouse(randomInSquare(482),randomInSquare(320))
    waitClickWait(self,45,55)
    #Click second yew tree
    moveMouse(randomInSquare(709),randomInSquare(610))
    waitClickWait(self,45,55)
    for i in range (1):
        #Click first yew tree
        moveMouse(randomInSquare(656),randomInSquare(470))
        waitClickWait(self,45,55)
        #Click second yew tree
        moveMouse(randomInSquare(709),randomInSquare(610))
        waitClickWait(self,45,55)
    #click bank
    moveMouse(randomInSquare(858),randomInSquare(708))
    waitClickWait(self,6,7)
#start at bank with deposit all on
#gpu plugin on and atleast 30
def cutFossilIslandTreesAndBank(self):
    #empty inv
    emptyInventoryInBank(self)
    #click on cave
    moveMouse(randomInSquare(101),randomInSquare(285))
    waitClickWait(self,9,11)

    if(returnInt(0, 10)<5):
        spec(self)
    #click on first tree
    moveMouse(randomInSquare(719),randomInSquare(415))
    waitClickWait(self,39,55)
    #aitClickWait(self,2,3)
    #click on second tree
    moveMouse(randomInSquare(541),randomInSquare(520))
    waitClickWait(self,37,57)
    #waitClickWait(self,2,3)
    #click on third tree
    moveMouse(randomInSquare(486),randomInSquare(431))
    waitClickWait(self,34,56)
    #waitClickWait(self,3,4)
    #click on second tree
    moveMouse(randomInSquare(768),randomInSquare(595))
    waitClickWait(self,34,56)
    #waitClickWait(self,2,3)
    #click on cave
    moveMouse(randomInSquare(855),randomInSquare(665))
    waitClickWait(self,5,6)
    #click on bank
    moveMouse(randomInSquare(1207),randomInSquare(723))
    waitClickWait(self,9,10)
    moveMouse(randomInSquare(790),randomInSquare(590))
    waitClickWait(self,5,6)

def cutFossilIslandTest(self):
    #click on first tree
    moveMouse(randomInSquare(719),randomInSquare(415))
    #waitClickWait(self,39,55)
    waitClickWait(self,2,3)
    #click on second tree
    moveMouse(randomInSquare(541),randomInSquare(520))
    #waitClickWait(self,37,57)
    waitClickWait(self,2,3)
    #click on third tree
    moveMouse(randomInSquare(486),randomInSquare(431))
    #waitClickWait(self,34,56)
    waitClickWait(self,3,4)
    #click on second tree
    moveMouse(randomInSquare(768),randomInSquare(595))
    #waitClickWait(self,34,56)
    waitClickWait(self,2,3)
    #click on cave
    moveMouse(randomInSquare(855),randomInSquare(665))
    waitClickWait(self,5,6)

    click_thread.stop_clicking()
#assumes at fishing guild bank camera zoomed in and north
#assumes bank fillers are on with runes in inv
#x set to 18
def superGlassmake(self):
    for x in range(4):
        emptyInventoryInBank(self)
        keyboard.press(Key.shift)
        #click first bank spot with no long wait
        moveMouse(returnInt(413,430), returnInt(151,167))
        time.sleep(random.uniform(0.4,.6))
        mouse.click(self.button)
        time.sleep(random.uniform(.4,.6))
        #click y more seaweeds
        for y in range(2):
            mouse.click(self.button)
            time.sleep(random.uniform(.4,.6))
        keyboard.release(Key.shift)
        clickSecondBankSpot(self)
        clickEsc(self)
        moveMouse(returnInt(1215, 1223), returnInt(858, 868))
        waitClickWait(self,3,4)
        clickFishingGuildBank(self)
    #pick up dropped glass
    emptyInventoryInBank(self)
    clickEsc(self)
    moveMouse(returnInt(652, 680), returnInt(513, 544))
    for x in range(returnInt(25,27)):
        time.sleep(random.uniform(0.4,.6))
        mouse.click(self.button)
    clickFishingGuildBank(self)
def threeTickMiningGranite(self):
    #click rock 2
    moveMouse(randomInSquare(832),randomInSquare(715))
    waitClickWait(self,1,1.2)
    #click 3t
    tickManipulate(self)
    drop3tItems(self)
    #click 3rd rock
    moveMouse(randomInSquare(835),randomInSquare(715))
    waitClickWait(self,1,1.2)
    #click 3t
    tickManipulate(self)
    drop3tItems(self)
    #click 4th
    moveMouse(randomInSquare(464),randomInSquare(694))
    waitClickWait(self,1,1.2)
    #click 3t
    tickManipulate(self)
    drop3tItems(self)
    #click 1st
    moveMouse(randomInSquare(1031),randomInSquare(118))
    waitClickWait(self,1.6,1.8)
    #click 3tick
    tickManipulate(self)
    drop3tItems(self)


def cookSeaweedAtFT(self):
    #click empty inv
    emptyInventoryInBank(self)
    time.sleep(random.uniform(.2,.4))
    #click bank spot 1
    clickFirstBankSpot(self)
    time.sleep(random.uniform(.2,.4))
    #click esc
    clickEsc(self)
    time.sleep(random.uniform(.9,1.4))
    #click fire
    moveMouse(randomInSquare(714), randomInSquare(695))
    time.sleep(random.uniform(.2,.4))
    mouse.click(self.button)
    #wait while running
    time.sleep(random.uniform(4,5))
    #space
    clickSpace(self)
    #click bank after waiting few sec

    time.sleep(random.uniform(7,9 ))
    moveMouse(randomInSquare(671), randomInSquare(391))
    time.sleep(random.uniform(.2,.4))
    mouse.click(self.button)
    time.sleep(random.uniform(3,4))
#assumes on spell tab
def highAlch(self):
    moveMouse(returnInt(1371, 1374), returnInt(845, 853))
    time.sleep(random.uniform(0.6, .7))
    mouse.click(self.button)
    time.sleep(random.uniform(0.9, 1.2))
    mouse.click(self.button)
#assums starting top of seers bank
#zoomed out and north
def seersCourse(self):

    highAlch(self)
    #jump to next roof
    moveMouse(returnInt(483, 506), returnInt(424, 539))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    highAlch(self)
    #cross rope
    moveMouse(returnInt(626, 641), returnInt(656, 668))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    highAlch(self)
    #jump to next roof
    moveMouse(returnInt(686, 809), returnInt(634, 657))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    highAlch(self)
    #jump to next roof
    moveMouse(returnInt(451, 507), returnInt(614, 627))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    highAlch(self)
    #jump down
    moveMouse(returnInt(715, 736), returnInt(543, 664))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    highAlch(self)

    if(returnInt(0,10)>5):
        #click mid square
        moveMouse(returnInt(1201, 1213), returnInt(261, 274))
        time.sleep(random.uniform(0.3, .5))
        mouse.click(self.button)
        time.sleep(random.uniform(0.3, .5))
        highAlch(self)
        time.sleep(random.uniform(7,8))
        highAlch(self)
        #climb up bank
        moveMouse(returnInt(742, 752), returnInt(259, 281))
        time.sleep(random.uniform(0.3, .5))
        mouse.click(self.button)
        time.sleep(random.uniform(9, 10))
    else:
        #click left square
        moveMouse(returnInt(1174, 1192), returnInt(261, 274))
        time.sleep(random.uniform(0.3, .5))
        mouse.click(self.button)
        time.sleep(random.uniform(0.3, .5))
        highAlch(self)
        time.sleep(random.uniform(7,8))
        highAlch(self)
        #climb up bank
        moveMouse(returnInt(763, 779), returnInt(259, 278))
        time.sleep(random.uniform(0.3, .5))
        mouse.click(self.button)
        time.sleep(random.uniform(9, 10))


#assumes zoomed in
def clickFishingGuildBank(self):
    moveMouse(randomInSquare(407), randomInSquare(516))
    waitClickWait(self,.2,.4)
    time.sleep(random.uniform(.8,1))
#assumes zoomed in
def clickLilIslandBank(self):
    moveMouse(randomInSquare(412), randomInSquare(465))
    waitClickWait(self,.2,.4)
    time.sleep(random.uniform(.2,.4))
#assumes mould is in inv spot 1 and x set to all
def edgevilleFurnace(self):
    clickSecondInvSlot(self)
    clickFirstBankSpot(self)
    #click furnace
    moveMouse(randomInSquare(1011), randomInSquare(438))
    waitClickWait(self,6,8)
    #click space
    clickSpace(self)
    time.sleep(random.uniform(40,50))
    #click bank
    moveMouse(randomInSquare(406), randomInSquare(676))
    waitClickWait(self,6,8)

def runCannonBalls(self):
    #deposit all cannonballs
    clickSecondInvSlot(self)
    #grab more bars
    clickFirstBankSpot(self)

    #click furnace
    moveMouse(randomInSquare(1011), randomInSquare(438))
    waitClickWait(self,6,8)
    #click space
    clickSpace(self)
    time.sleep(random.uniform(120,136))
    #click bank
    moveMouse(randomInSquare(406), randomInSquare(676))
    waitClickWait(self,6,8)

def amaniteCrabs3(self):
    for x in range(10):
        #click
        #wait 15.6 seconds
        mouse.click(self.button)
        time.sleep(random.uniform(62,67))
        print(x)
    # regain agro
    moveMouse(returnInt(760, 777), returnInt(1037, 1046))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    moveMouse(returnInt(628, 644), returnInt(51, 66))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    moveMouse(returnInt(628, 644), returnInt(95, 106))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    mouseUnderPerson(self)
def amaniteCrabs2(self):
    for x in range(9):
        #click
        #wait 15.6 seconds
        mouse.click(self.button)
        time.sleep(random.uniform(45,55))
        print(x)
    #regain agro
    moveMouse(returnInt(77, 98), returnInt(418, 437))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    moveMouse(returnInt(603, 619), returnInt(545, 558))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(3,5))
    moveMouse(returnInt(1201, 1215), returnInt(647, 660))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    moveMouse(returnInt(806, 819), returnInt(546, 559))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(3,5))
    mouseUnderPerson(self)
def mouseUnderPerson(self):
    #move mouse to under person
    moveMouse(returnInt(698, 709), returnInt(546, 556))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
def temp(self):
    for x in range (16):
        moveMouse(randomInSquare(675),randomInSquare(545))
        time.sleep(random.uniform(1.2,1.4))
        mouse.click(self.button)
        time.sleep(random.uniform(1.8,2))
        moveMouse(randomInSquare(699),randomInSquare(569))
        time.sleep(random.uniform(1.2,1.4))
        mouse.click(self.button)
        time.sleep(random.uniform(3,4.2))
def depositAll(self):
    #deposit all
    moveMouse(randomInSquare(765), randomInSquare(833))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(.8, 1.2))

def mineIronOreAndBank(self):
    temp(self)
    #click connector square
    moveMouse(randomInSquare(1207), randomInSquare(392))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(16,18))
    #bank box
    moveMouse(randomInSquare(1032), randomInSquare(523))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    #deposit all
    moveMouse(randomInSquare(655), randomInSquare(567))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(.8, 1.2))
    #connector
    moveMouse(randomInSquare(314), randomInSquare(584))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    #first ore
    moveMouse(randomInSquare(214), randomInSquare(729))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(16,18))


# alkarhid power mining
def iron(self):
    for ii in range(8):
        moveMouse(returnInt(696, 709), returnInt(566, 574))
        waitClickWait(self, 2, 2.5)
        moveMouse(returnInt(670, 685), returnInt(541, 555))
        waitClickWait(self, 2, 2.5)
        moveMouse(returnInt(696, 709), returnInt(518, 532))
        waitClickWait(self, 2, 2.5)
    dropInventory(self)


columnNums = [1225,1245,1269,1287,1311,1328,1352,1370]
rowNums = [760,775,800,813,834,848,871,882,906,922,944,956,975,992]
lastColSlot=[columnNums[6],columnNums[7]]
lastRowSlot=[rowNums[12],rowNums[13]]
global firstTime
def minnows(self,counter ):
    for x in range(4):
        #click
        #wait 15.6 seconds
        mouse.click(self.button)
        if counter != 0 and x==0:
            time.sleep(random.uniform(13.5,13.55))
            print('timer1')
            #time.sleep(13.53)
        else:
            time.sleep(random.uniform(14.27,14.3))
            print('timer2')
            #time.sleep(14.27)
        #move left
        if x !=3:
            moveMouse(returnInt(454, 560), returnInt(300,310))
            time.sleep(random.uniform(0.8, 1))
        #repeat x4
    moveMouse(returnInt(1214, 1315), returnInt(300,310))
    time.sleep(random.uniform(1,1.4))
    mouse.click(self.button)
    return counter +1

def catchNBankKarambwans(self):
    #move mouse to fairy ring
    xVal = returnInt(714, 729)
    yVal = returnInt(714,726)
    moveMouse(xVal, yVal )
    time.sleep(random.uniform(.6, 1.2))
    #right click on fairy ring and configure
    rightClickThridOption(self, xVal, yVal)
    #run to the fairy ring
    time.sleep(random.uniform(3, 4))
    #select locaton in quick select
    moveMouse(returnInt(1236, 1348), returnInt(828,853))
    waitClickWait(self,.6,1.2)
    #select submit center screen
    moveMouse(returnInt(522, 657), returnInt(553,595))
    waitClickWait(self,3,4)
    #click to get bank in frame
    #moveMouse(returnInt(1325, 1336), returnInt(708,715))
    #waitClickWait(self,11,12)
    #click bank
    #moveMouse(returnInt(698, 710), returnInt(657,670))
    #waitClickWait(self,2,4)
    #click bank and wait 11,12
    keyboard.press('e')
    time.sleep(random.uniform(.3, .5))
    keyboard.release('e')
    moveMouse(returnInt(1264, 1276), returnInt(810,821))
    time.sleep(random.uniform(.6,1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(.6,1.2))
    keyboard.press('e')
    time.sleep(random.uniform(.1, .3))
    keyboard.release('e')
    time.sleep(random.uniform(11, 12))
    #click item with all selected to bank all karams
    moveMouse(returnInt(columnNums[6], columnNums[7]), returnInt(rowNums[6], rowNums[7]))
    waitClickWait(self,2,4)
    #click to get ring in frame
    #moveMouse(returnInt(30, 49), returnInt(331,345))
    #waitClickWait(self,11,12)
    #move mouse to fairy ring
    xVal = returnInt(0, 14)
    yVal = returnInt(242,258)
    moveMouse(xVal, yVal )
    time.sleep(random.uniform(.6,1.2))
    #right click on fairy ring and configure
    rightClickThridOption(self, xVal, yVal)
    time.sleep(random.uniform(11,12))
    #select locaton in quick select
    moveMouse(returnInt(1236, 1345), returnInt(792,811))
    waitClickWait(self,.6,1.2)
    #select submit center screen
    moveMouse(returnInt(522, 657), returnInt(553,595))
    waitClickWait(self,3,4)
    #move mouse to fishing spot
    moveMouse(returnInt(674, 687), returnInt(382,393))

    time.sleep(random.uniform(0.8, 1))
    #click and fish for 2 minutes
    waitClickWait(self,115,120)
def fruitStalls(self):
    for i in range(np.random.randint(16,20)):
        mouse.click(self.button)
        time.sleep(random.uniform(3.4,3.6))
    dropInventory2(self)
    moveMouse(returnInt(412,530), returnInt(454,546))
    time.sleep(random.uniform(0.4, .45)) #random.uniform(0.3, .5)

    #assums x = 14 and bank on steel smithing tab. wearing ice gaunts
def walkingSteelBlastFurnace(self):
    #click last inv spot
    clickSecondInvSlot(self)

    clickFirstBankSpot(self)
    clickSecondBankSpot(self)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    #walk to deposit
    moveMouse(randomInSquare(567), randomInSquare(294))
    waitClickWait(self,13,14)

    #walk to collect
    moveMouse(randomInSquare(657), randomInSquare(629))
    waitClickWait(self,6,7)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(random.uniform(0.8, 1))

    # switch to gold gaunts
    clickFirstInvSlot(self)

    time.sleep(random.uniform(0.8, 1))
    #click bank
    moveMouse(randomInSquare(879), randomInSquare(723))
    waitClickWait(self,7,8)
#assumes starting with full run and coffer filled
def goldBlastFurnace(self):
    for x in range (10):
        #click last inv spot
        clickLastInvSlot(self)

        clickFirstBankSpot(self)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        #run to deposit
        moveMouse(randomInSquare(567), randomInSquare(294))
        waitClickWait(self,12,13)

        #switch to ice gaunts
        clickFirstInvSlot(self)
        time.sleep(random.uniform(0.8, 1))

        #run to collect
        moveMouse(randomInSquare(657), randomInSquare(629))
        waitClickWait(self,4,5)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(random.uniform(0.8, 1))

        # switch to gold gaunts
        clickFirstInvSlot(self)

        time.sleep(random.uniform(0.8, 1))
        #click bank
        moveMouse(randomInSquare(879), randomInSquare(723))
        waitClickWait(self,5,6)
    toggleRun(self)
    moveMouse(randomInSquare(697), randomInSquare(571))
    waitClickWait(self,1,2)
    for x in range (5):
        # click last inv spot
        clickSecondInvSlot(self)

        clickFirstBankSpot(self)

        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        # walk to deposit
        moveMouse(randomInSquare(567), randomInSquare(294))
        waitClickWait(self, 15, 16)

        #switch to ice gaunts
        clickFirstInvSlot(self)
        time.sleep(random.uniform(0.8, 1))
        # walk to collect
        moveMouse(randomInSquare(657), randomInSquare(629))
        waitClickWait(self, 6, 7)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(random.uniform(0.8, 1))

        # switch to gold gaunts
        clickFirstInvSlot(self)

        time.sleep(random.uniform(0.8, 1))
        # click bank
        moveMouse(randomInSquare(879), randomInSquare(723))
        waitClickWait(self, 9, 10 )
    toggleRun(self)
    moveMouse(randomInSquare(697), randomInSquare(571))
    waitClickWait(self,1,2)
def BlastFurnaceForMithBarsWalking(self):
    for x in range(2):
        for y in range(3):
            # deposit bars
            clickSecondInvSlot(self)
            # grab mith
            if (y == 0):
                # grab coal
                clickSecondBankSpot(self)
            if (y == 1 or y == 2):
                # grab coal and mith
                clickFirstBankSpot(self)
            # grab coal
            clickFirstInvSlot(self)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            # walk to deposit
            moveMouse(randomInSquare(567), randomInSquare(294))
            waitClickWait(self, 15, 16)

            #place coalfrom bag
            keyboard.press(Key.shift)
            clickFirstInvSlot(self)
            keyboard.release(Key.shift)
            moveMouse(randomInSquare(720), randomInSquare(546))
            waitClickWait(self,.4,.8)
            # walk to collect
            moveMouse(randomInSquare(657), randomInSquare(629))
            waitClickWait(self, 6, 7)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            time.sleep(random.uniform(0.8, 1))

            # click bank
            moveMouse(randomInSquare(879), randomInSquare(723))
            waitClickWait(self, 9, 10 )
def BlastFurnaceForAddyBarsWalking(self):
    for x in range(2):
        for y in range(2):
            # deposit bars
            clickSecondInvSlot(self)
            # grab mith
            if (y == 0):
                # grab coal
                clickSecondBankSpot(self)
            if (y == 1 or y == 2):
                # grab coal and mith
                clickFirstBankSpot(self)
            # grab coal
            clickFirstInvSlot(self)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            # walk to deposit
            moveMouse(randomInSquare(567), randomInSquare(294))
            waitClickWait(self, 15, 16)

            #place coalfrom bag
            keyboard.press(Key.shift)
            clickFirstInvSlot(self)
            keyboard.release(Key.shift)
            moveMouse(randomInSquare(720), randomInSquare(546))
            waitClickWait(self,.4,.8)
            # walk to collect
            moveMouse(randomInSquare(657), randomInSquare(629))
            waitClickWait(self, 6, 7)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            time.sleep(random.uniform(0.8, 1))

            # click bank
            moveMouse(randomInSquare(879), randomInSquare(723))
            waitClickWait(self, 9, 10 )
def BlastFurnaceForMithBars(self):
    for x in range (3):
        for y in range (3):
            #deposit bars
            clickSecondInvSlot(self)
            #grab mith
            if(y==0):
                #grab coal
                clickSecondBankSpot(self)
            if(y==1 or y==2):
                #grab coal and mith
                clickFirstBankSpot(self)
            #grab coal
            clickFirstInvSlot(self)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            #run to deposit
            moveMouse(randomInSquare(567), randomInSquare(294))
            waitClickWait(self,12,13)
            #place coalfrom bag
            keyboard.press(Key.shift)
            clickFirstInvSlot(self)
            keyboard.release(Key.shift)
            moveMouse(randomInSquare(720), randomInSquare(546))
            waitClickWait(self,.4,.8)
            #run to collect
            moveMouse(randomInSquare(657), randomInSquare(629))
            waitClickWait(self,4,5)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            time.sleep(random.uniform(0.8, 1))

            #click bank
            moveMouse(randomInSquare(879), randomInSquare(723))
            waitClickWait(self,5,6)
    toggleRun(self)
    moveMouse(randomInSquare(697), randomInSquare(571))
    waitClickWait(self,1,2)
    BlastFurnaceForMithBarsWalking(self)
    toggleRun(self)
    moveMouse(randomInSquare(697), randomInSquare(571))
    waitClickWait(self,1,2)
def BlastFurnaceForAddyBars(self):
    for x in range (5):
        for y in range (2):
            #deposit bars
            clickSecondInvSlot(self)
            #grab mith
            if(y==0):
                #grab coal
                clickSecondBankSpot(self)
            if(y==1 or y==2):
                #grab coal and mith
                clickFirstBankSpot(self)
            #grab coal
            clickFirstInvSlot(self)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            #run to deposit
            moveMouse(randomInSquare(567), randomInSquare(294))
            waitClickWait(self,8,10)
            #place coalfrom bag
            keyboard.press(Key.shift)
            clickFirstInvSlot(self)
            keyboard.release(Key.shift)
            moveMouse(randomInSquare(720), randomInSquare(546))
            waitClickWait(self,.4,.8)
            #run to collect
            moveMouse(randomInSquare(657), randomInSquare(629))
            waitClickWait(self,4,5)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            time.sleep(random.uniform(0.8, 1))

            #click bank
            moveMouse(randomInSquare(879), randomInSquare(723))
            waitClickWait(self,5,6)
    toggleRun(self)
    moveMouse(randomInSquare(697), randomInSquare(571))
    waitClickWait(self,1,2)
    BlastFurnaceForAddyBarsWalking(self)
    toggleRun(self)
    moveMouse(randomInSquare(697), randomInSquare(571))
    waitClickWait(self,1,2)
def BlastFurnaceForSteelBarsWalking(self):
    for x in range(5):
        # deposit bars
        clickSecondInvSlot(self)
        # grab iron ore
        clickFirstBankSpot(self)
        # grab coal
        clickFirstInvSlot(self)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        # grab coal
        clickFirstInvSlot(self)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        # walk to deposit
        moveMouse(randomInSquare(567), randomInSquare(294))
        waitClickWait(self, 15, 16)

        #place coalfrom bag
        keyboard.press(Key.shift)
        clickFirstInvSlot(self)
        keyboard.release(Key.shift)
        moveMouse(randomInSquare(720), randomInSquare(546))
        waitClickWait(self,.4,.8)
        # walk to collect
        moveMouse(randomInSquare(657), randomInSquare(629))
        waitClickWait(self, 6, 7)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(random.uniform(0.8, 1))

        # click bank
        moveMouse(randomInSquare(879), randomInSquare(723))
        waitClickWait(self, 9, 10 )
def BlastFurnaceForSteelBars(self):
    for x in range (8):
        #deposit bars
        clickSecondInvSlot(self)
        clickFirstBankSpot(self)
        #grab coal
        clickFirstInvSlot(self)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        #run to deposit
        moveMouse(randomInSquare(567), randomInSquare(294))
        waitClickWait(self,12,13)
        #place coalfrom bag
        keyboard.press(Key.shift)
        clickFirstInvSlot(self)
        keyboard.release(Key.shift)
        moveMouse(randomInSquare(720), randomInSquare(546))
        waitClickWait(self,.6,1)
        #run to collect
        moveMouse(randomInSquare(657), randomInSquare(629))
        waitClickWait(self,4,5)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(random.uniform(0.8, 1))

        #click bank
        moveMouse(randomInSquare(879), randomInSquare(723))
        waitClickWait(self,5,6)
    toggleRun(self)
    moveMouse(randomInSquare(697), randomInSquare(571))
    waitClickWait(self,1,2)
    BlastFurnaceForSteelBarsWalking(self)
    toggleRun(self)
    moveMouse(randomInSquare(697), randomInSquare(571))
    waitClickWait(self,1,2)
def clickFirstBankSpot(self):
    moveMouse(returnInt(413,430), returnInt(151,167))
    waitClickWait(self,1.3, 2.5)
def clickSecondBankSpot(self):
    moveMouse(returnInt(459,477), returnInt(151,167))
    waitClickWait(self,1.3, 2.5)
def emptyInventoryInBank(self):
    moveMouse(returnInt(773,789), returnInt(832,852))
    waitClickWait(self,1,2)
def mlmTopFloor(self):
    #empty inventory
    emptyInventoryInBank(self)
    #press esc
    keyboard.press(Key.esc)
    time.sleep(random.uniform(.1,.2))
    keyboard.release(Key.esc)
    #click ladder
    moveMouse(randomInSquare(581), randomInSquare(370))
    waitClickWait(self,6,7)
    #click first ore spot
    moveMouse(randomInSquare(495), randomInSquare(348))
    waitClickWait(self,30,41)
    #waitClickWait(self,10,12)
    #2nd
    moveMouse(randomInSquare(690), randomInSquare(564))
    waitClickWait(self,30,34)
    #waitClickWait(self,3,4)
    #third
    moveMouse(returnInt(716,725), returnInt(565,569))
    waitClickWait(self,32,39)
    #waitClickWait(self,3,4)

    #waitClickWait(self,1,2)
    #4th
    moveMouse(returnInt(720,727), returnInt(565,569))
    waitClickWait(self,33,40)
    #waitClickWait(self,3,4)

    #click ladder
    moveMouse(returnInt(804,809), returnInt(738,742))
    waitClickWait(self,8,9)
    #click hopper
    moveMouse(returnInt(527,536), (returnInt(542,547)))
    waitClickWait(self,7,10)
    #click sack
    moveMouse(randomInSquare(670), randomInSquare(838))
    waitClickWait(self,7,9)
    #click sack
    if(returnInt(1,10)>8):
        moveMouse(randomInSquare(669), randomInSquare(547))
        waitClickWait(self,2,3)
    #click bank
    moveMouse(randomInSquare(969), randomInSquare(385))
    waitClickWait(self,7,9)

#assumes north faceing zoomed out camera
#set quantity to all
def runPlanks(self):

    #click second inv spot
    clickSecondInvSlot(self)
    #click first bank spot
    clickFirstBankSpot(self)
    #click square
    #wait while running
    moveMouse(randomInSquare(996), randomInSquare(118))
    waitClickWait(self,12,14)
    #click sawmill dude
    moveMouse(returnInt(1039,1053), returnInt(520,528))
    waitClickWait(self,9,10)
    #click space
    clickSpace(self)
    #click square
    #wait while running
    moveMouse(returnInt(0,7), returnInt(680,700))
    waitClickWait(self,10,12)
    #click bank
    moveMouse(returnInt(531,541), returnInt(1007,1012))
    waitClickWait(self,8,10)

def hosidiousCookingBot(self):
    #empty inventory
    emptyInventoryInBank(self)
    #click karams
    moveMouse(returnInt(413,430), returnInt(151,167))
    waitClickWait(self,1.3, 2.5)
    #press esc
    keyboard.press(Key.esc)
    time.sleep(random.uniform(.3,.6))
    keyboard.release(Key.esc)
    #click range and run there

    moveMouse(returnInt(738,748), returnInt(408,420))
    waitClickWait(self,3.7,3.9)
    #click option 2
    #keyboard.press("2")
    keyboard.press(Key.space)
    time.sleep(random.uniform(.3,.6))
    #keyboard.release("2")
    keyboard.release(Key.space)
    #cook and wait
    time.sleep(random.uniform(64,67))
    #move mouse to bank
    moveMouse(returnInt(656,664), returnInt(679,688))
    waitClickWait(self,3.4,3.6)

#stand west of tree and camera points north. zoom in all the way
def teakCutNFletch(self):
    #click 5 times
    for i in range(7):
        waitClickWait(self,15,20);
    #click last inv spot
    clickLastInvSlot(self)
    #click first inv spot
    clickFirstInvSlot(self)
    #click space
    keyboard.press(Key.space)
    time.sleep(random.uniform(40, 45))
    #drop inv
    dropInventory(self)

    #click tree
    moveMouse(returnInt(832,949), returnInt(515,641))

def rightClickThridOption(self,xVal,yVal):
    mouse.click(self.button.right)
    time.sleep(random.uniform(.6, 1.2))
    # move mouse down to configure X pixels down from the saved location
    newxVal = xVal + random.uniform(-38, 30)
    if (newxVal < 5):newxVal=5
    moveMouse(newxVal, yVal + random.uniform(53, 60))
    time.sleep(random.uniform(.6, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(.6, 1.2))
def tickManipulate(self):
    # click inv spot one
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.48, .62))  # random.uniform(0.3, .5)
    mouse.click(self.button)
    # click inv spot 5
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[2], rowNums[3]))
    time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
    mouse.click(self.button)  # start herb animation
def drop3tItems(self):
    # click inv spot 9
    if (random.uniform(0, 10) > 2):
        moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[4], rowNums[5]))
        time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
        mouse.click(self.button)
    # 10% chance to click inv spot 10
    if (random.uniform(0, 10) > 100):
        moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[4], rowNums[5]))
        time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
        mouse.click(self.button)
    # 50% chance to click inv spot 13
    if (random.uniform(0, 10) > 100):
        moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[6], rowNums[7]))
        time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
        mouse.click(self.button)
def threeTickFish(self):
    tickManipulate(self)
    drop3tItems(self)
    #click inv spot 9
    if(random.uniform(0,10)>2):
        moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[4], rowNums[5]))
        time.sleep(random.uniform(0.2, .25)) #random.uniform(0.3, .5)
        mouse.click(self.button)
    #10% chance to click inv spot 10
    if(random.uniform(0,10)>9):
        moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[4], rowNums[5]))
        time.sleep(random.uniform(0.2, .25)) #random.uniform(0.3, .5)
        mouse.click(self.button)
    #50% chance to click inv spot 13
    if(random.uniform(0,10)>9):
        moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[6], rowNums[7]))
        time.sleep(random.uniform(0.2, .25)) #random.uniform(0.3, .5)
        mouse.click(self.button)
    #click fishing spot
    moveMouse(returnInt(1040,1132), returnInt(856,928))
    time.sleep(random.uniform(0.2, .25)) #random.uniform(0.3, .5)
    mouse.click(self.button)
    time.sleep(random.uniform(0.2 ,.3))
def fishAndDropInv(self):
    dropInventory(self)

    time.sleep(random.uniform(.4,.6))
    moveMouse(returnInt(722, 731), returnInt(547,556))

    time.sleep(random.uniform(.6,1.2))
    counter = 0
    # click randomly for a few minutes
    while counter < returnInt(5,6):
        mouse.click(self.button)
        # tenPercentChanceOfE()
        time.sleep(random.uniform(15, 20))
        counter += 1

def clickAndDropInv(self):
    counter = 0
    # click randomly for a few minutes
    while counter < returnInt(13, 14):
        mouse.click(self.button)
        delay = np.random.randint(15, 18)
        # tenPercentChanceOfE()
        time.sleep(random.uniform(.3, 1))
        counter += 1
    dropInventory(self)

    moveMouse(returnInt(722, 731), returnInt(547,556))
    delay = np.random.randint(2, 3)
def clickAndFletchIntoShafts(self):
    counter = 0
    # click randomly for a few minutes
    while counter < returnInt(17,20):
        mouse.click(self.button)
        delay = np.random.randint(5,8)
        # tenPercentChanceOfE()
        time.sleep(delay)
        counter += 1
    #dropInventory(self)
    clickLastSlot(self)
    clickFirstInvSlot(self)
    keyboard.press(Key.space)
    time.sleep(random.uniform(.3, 1))
    keyboard.release(Key.space)
    time.sleep(random.uniform(25, 35))
    #dropInventory(self)
    moveMouse(returnInt(729, 738), returnInt(538, 548))
    time.sleep(random.uniform(.3, 1))
    moveMouse(returnInt(702, 709), returnInt(581, 591))
    time.sleep(random.uniform(.3, 1))


def clickAndFletchIntoBows(self):
    counter = 0
    # click randomly for a few minutes
    while counter < returnInt(17,20):
        mouse.click(self.button)
        delay = np.random.randint(5,8)
        # tenPercentChanceOfE()
        time.sleep(delay)
        counter += 1
    #dropInventory(self)
    clickLastSlot(self)
    clickFirstInvSlot(self)
    keyboard.press(Key.space)
    time.sleep(random.uniform(.3, 1))
    keyboard.release(Key.space)
    time.sleep(random.uniform(30, 40))
    dropInventory(self)
    moveMouse(returnInt(747, 761), returnInt(547, 556))
    time.sleep(random.uniform(.3, 1))

def waitClickWait(self):
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(1.3, 2.5))
def waitClickWait(self,min,max):
    time.sleep(random.uniform(0.6, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(min, max))

def clickFirstInvSlot(self):
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
def clickSecondInvSlot(self):
    moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
def clickLastInvSlot(self):
    moveMouse(returnInt(columnNums[6], columnNums[7]), returnInt(rowNums[12], rowNums[13]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
def clickLastSlot(self):
    moveMouse(returnInt(lastColSlot[0], lastColSlot[1]), returnInt(lastRowSlot[0], lastRowSlot[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(1.3, 1.8))

def clickInventory(self):
    #moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            waitClickWait(self)
def dropInventory(self):
    #moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    keyboard.press(Key.shift)
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.2, .3))
            mouse.click(self.button)
    keyboard.release(Key.shift)
    time.sleep(random.uniform(.4,.6))
def openPacks(self):
    #moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.2, .3))
            mouse.click(self.button)
    time.sleep(random.uniform(.4,.6))
    click_thread.stop_clicking()
    #assumes 10 waterskins and runs for cast
def mineSandstone(self):
    #mine 4 rocks 3 times
    #moveMouse(randomInSquare(696), randomInSquare(564))
    #waitClickWait(self, .6,1)
    for i in range(5):
        moveMouse(randomInSquare(674), randomInSquare(570))
        waitClickWait(self, 2.7,3.5)
        moveMouse(randomInSquare(644), randomInSquare(544))
        waitClickWait(self, 2.7,3.9)
        moveMouse(randomInSquare(671), randomInSquare(523))
        waitClickWait(self, 2.7,3.6)
        #click first one
        moveMouse(randomInSquare(735), randomInSquare(586))
        waitClickWait(self, 4.7,5.4)
    #deposit into grinder

    moveMouse(randomInSquare(257), randomInSquare(668))
    waitClickWait(self, 7,9)
    #click first rock
    moveMouse(randomInSquare(1006), randomInSquare(487))
    waitClickWait(self, 10,12)
def turnOffBot(self):
    keyboard.press('=')
    time.sleep(random.uniform(.2,.5))
    keyboard.release('=')
def dropInventory2(self):
    #moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    #keyboard.press(Key.shift)
    for i in range(4):
        for ii in range(7):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]),returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.2, .3))
            mouse.click(self.button)
            time.sleep(random.uniform(0.1,.15))
            mouse.click(self.button)
    #keyboard.release(Key.shift)
    time.sleep(random.uniform(.4,.6))
def click(self):
    cm = ClickMouse()
    if self.running == True:
        cm.stop_clicking()
    else:
        cm.start_clicking()

keyboard = C()
mouse = Controller()
click_thread = ClickMouse(1, buttonLeftClick)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
