#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  charaComs.py
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
import itemComs

class Chara():
	#Load in character attributes
	def __init__(self, charaname, race, lvl, curhp, maxhp, speed, fitness, knowledge, lefthand, lefthanddmg, lefthandbns,
				 lefthanddef, righthand, righthanddmg, righthandbns, righthanddef, twohanded, armour, armourbns):
		self.__name = charaname		
		self.__race = race
		self.__level = lvl
		self.__curhp = curhp
		self.__maxhp = maxhp
		self.__speed = speed
		self.__fitness = fitness
		self.__knowledge = knowledge
		self.__lefthanditem = lefthand
		self.__lefthanddmg = lefthanddmg
		self.__lefthandbns = lefthandbns
		self.__lefthanddef = lefthanddef
		self.__righthanditem = righthand
		self.__righthanddmg = righthanddmg
		self.__righthandbns = righthandbns
		self.__righthanddef = righthanddef
		self.__twohanded = twohanded
		self.__armour = armour
		self.__armourbns = armourbns
	
	#apply damage
	def damage(self, damage):
		self.__curhp -= damage
		if self.__curhp < 0:
			self.__curhp = 0
		return self.__curhp
	
	#apply healing
	def heal(self, heal):
		self.__curhp += heal
		if self.__curhp > self.__maxhp:
			self.__curhp = self.__maxhp
		return self.__curhp
	
	#get stats
	def getstat(self, stat):
		if stat == 'charname':
			return self.__name
		elif stat == 'race':
			return self.__race
		elif stat == 'lvl':
			return self.__level
		elif stat == 'curhp':
			return self.__curhp
		elif stat == 'maxhp':
			return self.__maxhp
		elif stat == 'speed':
			return self.__speed
		elif stat == 'fitness':
			return self.__fitness
		elif stat == 'knowledge':
			return self.__knowledge
		elif stat == 'lefthand':
			return self.__lefthanditem
		elif stat == 'righthand':
			return self.__righthanditem
		elif stat == 'armour':
			return self.__armour
		elif stat == 'damage':
			return self.__righthanddmg + self.__lefthanddmg
		elif stat == 'atkbns':
			return self.__lefthandbns + self.__righthandbns
		elif stat == 'dfsbns':
			return self.__righthanddef + self.__lefthanddef + self.__armourbns
			
	def equipweapon(self, itemname):
		twohand = itemname.getwpnhanded()
		itemtype = itemname.getiteminfo('itemtype')
		if twohand == True:
			self.__righthanditem = itemname
			self.__lefthanditem = itemname
			self.__twohanded = "yes"
		else:
			hand = equiphand(itemtype)
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
		self.__armourbns = armourbns

	def equiphand(self, itemtype):
			hand = input('Which hand would you like to equip ' + itemtype + 'in?')
			return hand

	#Other character based commands to be added