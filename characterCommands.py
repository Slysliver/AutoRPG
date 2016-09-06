#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  characterCommands.py
#  
#  Copyright 2016 Slysliver <slysliver@Bucket-Lite>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import itemCommands

class Character:
    #Load in character attributes
    def __init__(self, name, race, level, currenthp, maxhp, speed, fitness, knowledge, lefthanditem, lefthandeffect,
                 lefthandeffectvalue, righthanditem, righthandeffect, righthandeffectvalue,  twohanded, armour,
                 armourbonus,
                 inventory):
        self.__name = name
        self.__race = race
        self.__level = level
        self.__currrenthp = currenthp
        self.__maxhp = maxhp
        self.__speed = speed
        self.__fitness = fitness
        self.__knowledge = knowledge
        self.__lefthanditem = lefthanditem
        self.__lefthandeffect = lefthandeffect
        self.__lefthandeffectvalue = lefthandeffectvalue
        self.__righthanditem = righthanditem
        self.__righthandeffect = righthandeffect
        self.__righthandeffectvalue = righthandeffectvalue
        self.__twohanded = twohanded
        self.__armour = armour
        self.__armourbonus = armourbonus
        self.__inventory = inventory

    #apply damage
    def damage(self, damage):
        self.__currrenthp -= damage
        if self.__currrenthp < 0:
            self.__currrenthp = 0
        return self.__currrenthp

    #apply healing
    def heal(self, heal):
        self.__currrenthp += heal
        if self.__currrenthp > self.__maxhp:
            self.__currrenthp = self.__maxhp
        return self.__currrenthp

    #apply buff
    def buff(self, buff, bufftype, world, duration):
        if 'fitness' in buff:
            self.__fitness += buff.get('fitness')
        if 'knowledge' in buff:
            self.__knowledge += buff.get('knowledge')
        elif 'speed' in buff:
            self.__speed += buff.get('speed')

    #apply debuff
    def debuff(self, buff):
        if 'fitness' in buff:
            self.__fitness -= buff.get('fitness')
        if 'knowledge' in buff:
            self.__knowledge -= buff.get('knowledge')
        elif 'speed' in buff:
            self.__speed -= buff.get('speed')
    #get stats
    def getstat(self, stat):
        statsdictionary = dict()
        if 'name' in stat:
            statsdictionary['name'] = self.__name
        if 'race' in stat:
            statsdictionary['race'] = self.__race
        if 'level' in stat:
            statsdictionary['level'] = self.__level
        if 'currenthp' in stat:
            statsdictionary['currenthp'] = self.__currrenthp
        if 'maxhp' in stat:
            statsdictionary['maxhp'] = self.__maxhp
        if 'speed' in stat:
            statsdictionary['speed'] = self.__speed
        if 'fitness' in stat:
            statsdictionary['fitness'] = self.__fitness
        if 'knowledge' in stat:
            statsdictionary['knowledge'] = self.__knowledge
        if 'lefthand'in stat:
            statsdictionary['lefthanditem'] = self.__lefthanditem
            statsdictionary['lefthandeffects'] = self.__lefthandeffect
            statsdictionary['lefthandeffectsvalue'] = self.__lefthandeffectvalue
        if 'righthand' in stat:
            statsdictionary['righthanditem'] = self.__righthanditem
            statsdictionary['righthandeffects'] = self.__righthandeffect
            statsdictionary['righthandeffectsvalue'] = self.__righthandeffectvalue
        if 'twohanded' in stat:
            statsdictionary['twohanded'] = self.__twohanded
        if 'armour'in stat:
            statsdictionary['armour'] = self.__armour
        if 'inventory' in stat:
            statsdictionary['inventory'] = self.__inventory
        return statsdictionary

    def equipweapon(self, itemname):
        if itemname.getiteminfo('itemtype') != 'weapon':
            return False
        twohand = itemname.getwpnhanded()
        itemtype = itemname.getiteminfo('itemtype')
        if twohand == True:
            self.__righthanditem = itemname
            self.__lefthanditem = itemname
            self.__twohanded = "yes"
        else:
            hand = itemname.equiphand(itemtype)
            if hand == 'right':
                if self.__twohanded == 'yes':
                    self.__lefthanditem = 'none'
                    self.__righthanditem = itemname
                    if self.__twohanded == 'yes':
                        self.__twohanded = 'no'
            elif hand == 'left':
                if self.__twohanded == 'yes':
                    self.__righthanditem = 'none'
                    self.__lefthanditem = itemname
                    if self.__twohanded == 'yes':
                        self.__twohanded = 'no'


    #set armour
    def equiparmour(self, armour, armourbns):

        self.__armour = armour
        self.__armourbonus -= self.__armourbonus
        self.__armourbonus = armourbns

    def equiphand(self, itemtype):
            hand = input('Which hand would you like to equip ' + itemtype + 'in?')
            return hand
    #get player actions based on situation
    def getaction(self, situation):
        if situation == 'combat':
            characteraction = self.getcombatoptions()
            return characteraction
        elif situation == 'adventure':
            characteraction = self.getadventureoptions()
            return characteraction
        elif situation == 'conversation':
            characteraction = self.getconversationoptions()
            return characteraction

    def getcombatoptions(self):
        abilities = ['fight', 'spell' 'item', 'run']
        attributes = self.getstat({'currenthp', 'maxhp', 'speed', 'fitness', 'knowledge'})
        if attributes['currenthp'] < (attributes['maxhp']/3):
            availableitems = self.getitems()
            if availableitems == 0:
                return 'fight'
            elif availableitems > 0:
                for i in availableitems:
                    if i.getiteminfo('itemtype') == 'potion':
                        effect = i.getpotioneffect()
                        if effect == 'heal':
                            i.usepotion(self, self)
            else:
                return ' fight'

    def getitems(self):
        return self.__inventory

    def additem(self, item):
        if item in self.__inventory:
            self.__inventory[item] += 1
        else:
            self.__inventory[item] = 1
    def removeitem(self, item):
        self.__inventory[item] -= 1
        if self.__inventory[item] == 0:
            del self.__inventory[item]
    def savecharacter(self):
        savefile = open('./CharacterSaves/' + self.__name + '.txt', 'w')
        playerdetails = self.getstat({'name', 'race', 'level', 'currenthp', 'maxhp', 'speed', 'fitness', 'knowledge',
                                    'lefthand', 'righthand', 'twohanded', 'armour', 'inventory'})
        playerdetails = playerdetails.values()
        for i in playerdetails:
            savefile.write(str(i))
        savefile.close()
    #Other character based commands to be added
