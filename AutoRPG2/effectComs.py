class Effect():
    def __init__(self, target, efttype, amount, duration):
        self.__target = target
        self.__efttype = efttype
        self.__amount = amount
        self.__duration = duration

    def getefttarget(self):
        return self.__target

    def geteffect(self):
        return self.__efttype

    def geteftamount(self):
        return self.__amount

    def geteftduration(self):
        return self.__duration

    def applyeffect(self):
        if self.__efttype == 'heal':
            self.__target.heal(self.__amount)
            self.__duration -= 1
        elif self.__efttype == 'damage':
            self.__target.damage(self.__amount)
            self.__duration -= 1
        elif self.__efttype == 'buff':
            self.__target.buff(self.__amount)
            self.__duration -= 1
        elif self.__efttype =='debuff':
            self.__target.debuff(self.__amount)
            self.__duration -= 1
