from mcpi.minecraft import Minecraft
import math

mc = Minecraft.create()

pozycja = mc.player.getTilePos()
x = pozycja.x
z = pozycja.z

obiektX = 800
obiektZ = -230

odleglosc = math.sqrt((obiektX - x) ** 2 + (obiektZ - z)**2)
mc.postToChat(odleglosc)

blisko = 10 
mc.postToChat('Obiekt jest blisko: ' + str(odleglosc<= blisko))
