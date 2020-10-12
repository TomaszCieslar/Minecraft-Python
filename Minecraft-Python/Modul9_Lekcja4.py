from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()


licznik =0

while licznik<30:
    pozycja = mc.player.getTilePos()
    mc.setBlock(pozycja.x, pozycja.y, pozycja.z, 8)
    time.sleep(1)
    print(licznik)
    licznik+=1
print('Koniec przemieszczania')
