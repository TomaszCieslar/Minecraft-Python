import random
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

licznik = 0

while licznik<5:
    x = random.randint(-127,127)
    y = random.randint(0, 64)
    z = random.randint(-127, 127)
    mc.player.setTilePos(x,y,z)
    licznik+=1

print('Koniec przemieszczania')
