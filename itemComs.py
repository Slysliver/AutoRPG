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
class Item():
	def __init__(self, itmname, itemtype, value, weight):
		self.__itmname = itmname
		self.__itemtype = itemtype
		self.__value = value
		self.__weight = weight
	
	def getiteminfo(self, detail):
		if detail == 'itmname'
			return self.__itmname
		elif detail == 'itemtype'
			return self.__itemtype
		elif detail == 'value'
			return self.__value
		elif detail == 'weight'
			return self.__weight
			
#Drinkable, temporary item
class Potion(Item):
	def __init__(self, itmname, itemtype, value, weight, effect, effectvalue, potionduration)
		Item.__init__(itmname, itemtype, value, weight)
		self.__effect = effect
		self.__effectvalue = effectvalue
		self.__potionduration = potionduration
	
	def getpotiondeft(self):
		return self.__effect
		
	def getpotionvalue(self):
		return self.__effectvalue
		
	def getpotionduration(self):
		return self.__potionduration
	
	def usepotion(self, user)
		if self.__effect == heal:
			user.heal(self.__effectvalue)
		
class Weapon(Item):
	def __init__(self, itmname, itemtype, value, weight, twohanded, damage, dmgbns):
		Item.__init__(itmname, itemtype, value, weight)
		self.__twohanded = twohanded
		self.__damage = damage
		self.__dmgbns = dmgbns
		
	def getwpnhanded(self):
			return self.__twohanded
			
	def getwpndmg(self):
		return self.__damage
		
	def getwpnbns(self):
		return self.__dmgbns
		
class Armour(Item):
	def __init__(self, itmname, itemtype, value, weight, armourbns):
		Item.__init__(itmname, itemtype, value, weight)
		self.__armourbns = armourbns
	
	def getarmourbns(self):
		return self.__armourbns

class Key(Item):
	def __init__(self, doorid):
		Item.__init__(itmname, itemtype, value, weight)
		self.__doorid = doorid
	
	def getkeycombo(self):
		return self.__doorid
	
	def usekey(self, doorid):
		if doorid == self.__doorid:
			return True
		else:
			return False
