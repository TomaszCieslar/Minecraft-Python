from mcpi.minecraft import Minecraft
import math

mc = Minecraft.create()
pozycja = mc.player.getTilePos()

x = pozycja.x
z = pozycja.z

drzewoX = 800
drzewoZ = -230


odleglosc = math.sqrt((drzewoX - x) ** 2 + (drzewoZ - z) ** 2)

mc.postToChat(odleglosc)

blisko = 10
mc.postToChat('Obiekt jest blisko: ' + str(odleglosc<=blisko))