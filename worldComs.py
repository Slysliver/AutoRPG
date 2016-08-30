#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  worldComs.py
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
class World(self, seed):


class Location():
	
	def __init__(self, timeofday, worlddate, currentturn, weather, 
				 temperature, location):
		self.__timeofday = timeofday
		self.__worlddate = worlddate
		self.__currentturn = currentturn
		self.__weather = weather
		self.__tempurature = tempurature
		self.__location = location
	
	def getcurrtime(self):
		return self.__timeofday
	
	def getworlddate(self):
		return self.__worlddate
		
	def getturn(self):
		return self.__currentturn
	
	def getweather(self):
		return self.__weather
	
	def gettemperature(self):
		return self.__tempurature
	
	def getLocation(self):
		return self.__location
	
	def nextTurn(self):
		curturn = self.getturn()
		curturn += 1
		if curturn > 60:
			self.dailycyclechange()
			self.__currentturn = 0
		else:
			self.__currentturn = curturn
	def dailycyclechange(self):
		currentcycle = self.__timeofday
		currentcycle += 1
		if currentcycle = 10:
			self.worlddatechange()
			self.__worlddate = 0
		else:
			self.__worlddate = currentcycle
	def daychange(self):
		self.__worlddate += 1
	
	

