from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


licznik =0

while True:
    pozycja = mc.player.getTilePos()
    mc.setBlock(pozycja.x, pozycja.y, pozycja.z, 46,1)
    time.sleep(1)

print('Koniec demolki')
