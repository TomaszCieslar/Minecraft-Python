from mcpi.minecraft import Minecraft
from minecraft import blocks
import math

mc = Minecraft.create()

pozycja = mc.player.getTilePos()
x = pozycja.x
z = pozycja.z

obiektX = 10
obiektZ = 10

odleglosc = math.sqrt((obiektX - x) ** 2 + (obiektZ - z) ** 2)
mc.postToChat(odleglosc)

blisko = 20
mc.postToChat('Obiekt jest blisko: '+str(odleglosc<=blisko))


