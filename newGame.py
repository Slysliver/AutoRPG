from worldCommands import World
from characterCommands import Character
from itemCommands import Weapon
from itemCommands import Armour
from itemCommands import Shield
import random


def createworld():
    timeofday = random.randrange(1, 10)
    worlddate = random.randrange(1, 264)
    worldyear = random.randrange(1262, 1568)
    currentturn = random.randrange(1, 60)
    location = [random.randrange(1, 264), random.randrange(1, 264)]
    weather = getweather()
    temperature = gettemperature(weather)
    world = World(timeofday, worlddate, worldyear, currentturn, location, weather, temperature)
    return world


def getweather():
    weather = random.randrange(1, 4)
    if weather == 1:
        weather = 'sunny'
    elif weather == 2:
        weather = 'cloudy'
    elif weather == 3:
        weather = 'rainy'
    elif weather == 4:
        weather = 'snowing'
    return weather


def gettemperature(weather):
    if weather == 'sunny':
        temperature = random.randrange(10, 30)
    elif weather == 'cloudy':
        temperature = random.randrange(5, 19)
    elif weather == 'rainy':
        temperature = random.randrange(1, 15)
    elif weather == 'snowing':
        temperature = random.randrange(0, 10)
        temperature -= 10
    else:
        temperature = random.randrange(0, 30)
    return temperature


def createcharacter():
    name = input('What is the characters name?: ')
    raceselectionvalid = False
    race = ''
    while raceselectionvalid != True:
        race = input('Plese select a race (Human, Dwarf, or Elf: ')
        if race.lower == 'human' or 'elf' or 'dwarf':
            raceselectionvalid = True
        else:
            print 'Invalid selection made, try again.'
    print 'Stats are currently randomized. Future releases will allow for these to be set.'
    #change to stat generation to come later.
    characterstats = createstats()
    #Selecting class for weapons and items to be added later
    items = loadbasicitems()
    player = Character(name, race, 1, characterstats[0], characterstats[0], characterstats[1], characterstats[2],
                       characterstats[3], items[0], items[0].getiteminfo('itemtype'), items[0].getweapondamage,
                       items[1], items[1].getiteminfo('itemtype'), items[1].getshieldbonus(), False, items[2],
                       items[2].getarmourbonus(), {'Gold': 5, 'Healing Potion': 1})
    return player


def createstats():
    characterstats = [1, 1, 1, 1]
    for i in range(1, 16):
        randomstat = random.randrange(0,3)
        characterstats[randomstat] += 1
    return characterstats


def loadbasicitems():
    basicitems = []
    shortsword = Weapon('Short Sword', 'weapon', 4, 5, False, 3)
    basicitems.append(shortsword)
    woodshield = Shield('Wooden Shield', 'shield', 2, 4, 1)
    basicitems.append(woodshield)
    leatherarmour = Armour('Leather Armour', 'armour', 10, 9, 1)
    basicitems.append(leatherarmour)
    return basicitems
