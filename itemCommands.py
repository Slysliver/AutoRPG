#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  itemComs.py
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


class Item:

    def __init__(self, itmname, itemtype, value, weight):
        self.__itmname = itmname
        self.__itemtype = itemtype
        self.__value = value
        self.__weight = weight

    def getiteminfo(self, detail):
        if detail == 'itmname':
            return self.__itmname
        elif detail == 'itemtype':
            return self.__itemtype
        elif detail == 'value':
            return self.__value
        elif detail == 'weight':
            return self.__weight


# Drinkable, temporary item
class Potion(Item):
    def __init__(self, itmname, itemtype, value, weight, effect, effectvalue, potionduration):
        Item.__init__(itmname, itemtype, value, weight)
        self.__effect = effect
        self.__effectvalue = effectvalue
        self.__potionduration = potionduration

    def getpotiondeffect(self):
        return self.__effect

    def getpotionvalue(self):
        return self.__effectvalue

    def getpotionduration(self):
        return self.__potionduration

    def usepotion(self, user, target):
        if self.__effect == 'heal':
            user.removeitem(self)
            target.heal(self.__effectvalue)
        if self.__effect == 'damage':
            user.removeitem(self)
            target.damage(self.__effectvalue)
        if self.__effect == 'buff':
            user.removeitem(self)
            target.buff(self.__effectvalue)
        if self.__effect == 'debuff':
            user.removeitem(self)
            target.debuff(self.__effectvalue)


class Weapon(Item):
    def __init__(self, itmname, itemtype, value, weight, twohanded, damage):
        Item.__init__(itmname, itemtype, value, weight)
        self.__twohanded = twohanded
        self.__damage = damage

    def getwpnhanded(self):
        return self.__twohanded

    def getweapondamage(self):
        return self.__damage

    def equiphand(self):
        equiphand = input('Which hand should item be equipped in?:')
        return equiphand

class Shield(Item):
    def __init__(self, itmname, itemtype, value, weight, defensebonus,):
        Item.__init__(itmname, itemtype, value, weight)
        self.__defensebonus = defensebonus
    def getshieldbonus(self):
        return self.__defensebonus

class Armour(Item):
    def __init__(self, itmname, itemtype, value, weight, armourbonus):
        Item.__init__(itmname, itemtype, value, weight)
        self.__armourbonus = armourbonus

    def getarmourbonus(self):
        return self.__armourbonus


class Key(Item):
    def __init__(self, itmname, itemtype, value, weight, doorid):
        Item.__init__(itmname, itemtype, value, weight)
        self.__doorid = doorid

    def getkeycombo(self):
        return self.__doorid

    def usekey(self, doorid):
        if doorid == self.__doorid:
            return True
        else:
            return False
