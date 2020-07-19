import random
import time

def removePick(whatpick):
    number_of_pick = lotterylist.count(whatpick)
    for i in range(number_of_pick):
        lotterylist.remove(whatpick)

print("Welcome to the 2020 nba draft lottery")

Golden_State_Warriors = []
GSWpicks = 140
name = "Golden State Warriors"
for gsw in range(GSWpicks):
    Golden_State_Warriors.append(name)


Cleveland_Cavaliers = []
Clepicks = 140
name2 = "Cleveland Cavaliers"
for cle in range(Clepicks):
    Cleveland_Cavaliers.append(name2)

Minnesota_Timberwolves = []
Minpicks = 140
name3 = "Minnesota Timberwolves"
for min in range(Minpicks):
    Minnesota_Timberwolves.append(name3)

Atlanta_Hawks = []
Atlpicks = 125
name4 = "Atlanta Hawks"
for atl in range(Atlpicks):
    Atlanta_Hawks.append(name4)


Detroit_Pistons = []
Detpicks = 105
name5 = "Detroit Pistons"
for det in range(Detpicks):
    Detroit_Pistons.append(name5)

New_York_Knicks = []
Nykpicks = 90
name6 = "New York Knicks"
for nyk in range(Nykpicks):
    New_York_Knicks.append(name6)

Chicago_Bulls = []
Chipicks = 60
name7 = "Chicago Bulls"
for chi in range(Chipicks):
    Chicago_Bulls.append(name7)

Charlotte_Hornets = []
Chapicks = 60
name8 = "Charlotte Hornets"
for cha in range(Chapicks):
    Charlotte_Hornets.append(name8)

Washington_Wizards = []
Waspicks = 60
name9 = "Washington Wizards"
for was in range(Waspicks):
    Washington_Wizards.append(name9)

Phoenix_Suns = []
Phxpicks = 30
name10 = "Phoenix Suns"
for phx in range(Phxpicks):
    Phoenix_Suns.append(name10)

San_Spurs = []
Saspicks = 20
name11 = "San Antonio Spurs"
for sas in range(Saspicks):
    San_Spurs.append(name11)

Sacramento_Kings = []
Sacpicks = 10
name12 = "Sacramento Kings"
for sac in range(Sacpicks):
    Sacramento_Kings.append(name12)

NOPA_Pelicans = []
NOPpicks = 10
name13 = "New Orleans Pelicans"
for nop in range(NOPpicks):
    NOPA_Pelicans.append(name13)

Blazers = []
Porpicks = 10
name14 = "Portland Trail Blazers"
for por in range(Porpicks):
    Blazers.append(name14)

lotterylist = Golden_State_Warriors + Cleveland_Cavaliers + Minnesota_Timberwolves + Atlanta_Hawks + Detroit_Pistons + New_York_Knicks + Chicago_Bulls + Charlotte_Hornets + Washington_Wizards + Phoenix_Suns + San_Spurs + Sacramento_Kings + NOPA_Pelicans + Blazers
random.shuffle(lotterylist)

pick1 = random.choice(lotterylist)
removePick(pick1)

pick2 = random.choice(lotterylist)
removePick(pick2)

pick3 = random.choice(lotterylist)
removePick(pick3)

pick4 = random.choice(lotterylist)
removePick(pick4)

pick5 = random.choice(lotterylist)
removePick(pick5)

pick6 = random.choice(lotterylist)
removePick(pick6)

pick7 = random.choice(lotterylist)
removePick(pick7)

pick8 = random.choice(lotterylist)
removePick(pick8)

pick9 = random.choice(lotterylist)
removePick(pick9)

pick10 = random.choice(lotterylist)
removePick(pick10)

pick11 = random.choice(lotterylist)
removePick(pick11)

pick12 = random.choice(lotterylist)
removePick(pick12)

pick13 = random.choice(lotterylist)
removePick(pick13)

pick14 = random.choice(lotterylist)
removePick(pick14)

time.sleep(3)
print("The fourteenth pick goes to the " + pick14)
time.sleep(3)
print("The thirteenth pick goes to the " + pick13)
time.sleep(3)
print("The twelfth pick goes to the " + pick12)
time.sleep(3)
print("The eleventh pick goes to the " + pick11)
time.sleep(3)
print("The tenth pick goes to the " + pick10)
time.sleep(3)
print("The ninth pick goes to the " + pick9)
time.sleep(3)
print("The eighth pick goes to the " + pick8)
time.sleep(3)
print("The seventh pick goes to the " + pick7)
time.sleep(3)
print("The sixth pick goes to the " + pick6)
time.sleep(3)
print("The fifth pick goes to the " + pick5)
time.sleep(3)
print("The fourth pick goes to the " + pick4)
time.sleep(3)
print("The third pick goes to the " + pick3)
time.sleep(3)
print("The second pick goes to the "+ pick2)
time.sleep(3)
print("The first pick goes to the  " + pick1)
running = True













