import characterCommands
from worldCommands import World


def turn(world, characters, activeeffects):

    #beginning of turn effects

    #get active effects and apply them.
    for i in characters:
        i.getaction()
    if activeeffects.length != 0:
        for i in activeeffects:
            i.applyeffect()
            if i.geteftduration == 0:
                activeeffects.pop(i)
    #get actions choices
    for i in characters:
        i.getaction()

    #Priority actions

    #end of turn effects

    #clean up step
    world.nextturn()
