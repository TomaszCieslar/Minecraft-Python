from mcpi.minecraft import Minecraft
from minecraft import blocks
import math

mc = Minecraft.create()
pozycja = mc.player.getTilePos()
x = pozycja.x
y = pozycja.y
z = pozycja.z

zagroda_x = 10
zagroda_y = 10
zagroda_z = 10

jestem_w_srodku = zagroda_x < x and zagroda_y<y and zagroda_z < z


mc.postToChat('Czy jestem w srodku: '+ str(jestem_w_srodku))


