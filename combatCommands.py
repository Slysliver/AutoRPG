#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  combatCommands.py
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


# basic damage dealing, needs fucntions to randomize damage
def meleedmg(attkr, dfndr):
    damage = attkr.getstat('damage')
    bonus = attkr.getstat('atkbns')
    dfns = dfndr.getstat('dfsbns')
    dfndr.damage((damage + bonus) - dfns)


# calculates combat speed ratio, returns rate of attacks for attacker
def initiative(attkr, dfndr, stat):
    attkrspd = attkr.getstat(stat)
    dfndrspd = dfndr.getstat(stat)
    ratio = attkrspd / dfndrspd
    if ratio < 1:
        ratio = dfndrspd / attkrspd
        return [ratio, False]
    else:
        return [ratio, True]


def attackingcombat(attkr, dfndr):
    atkRatio = initiative(attkr, dfndr, 'speed')
    if atkRatio[1] == True:
        while attkr.getstat('curhp') != 0 and dfndr.getstat('curhp') != 0:
            i = 1
            for i in range(i, atkRatio[0]):
                meleedmg(attkr, dfndr)
            meleedmg(dfndr, attkr)
    elif atkRatio[1] == False:
        while attkr.getstat('curhp') != 0 and dfndr.getstat('curhp') != 0:
            i = 1
            for i in range(i, atkRatio[0]):
                meleedmg(dfndr, attkr)
            meleedmg(attkr, dfndr)
