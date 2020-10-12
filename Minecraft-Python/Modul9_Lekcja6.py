from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()


wynik = 0
pozycja = mc.player.getTilePos()
bloczekPowyzej = mc.getBlock(pozycja.x, pozycja.y+2, pozycja.z)

while bloczekPowyzej == 8 or bloczekPowyzej == 9:
    time.sleep(1)
    pozycja = mc.player.getTilePos()
    bloczekPowyzej = mc.getBlock(pozycja.x, pozycja.y+2, pozycja.z)
    wynik = wynik + 1
    mc.postToChat('Twoj wynik: '+ str(wynik))

mc.postToChat('Koncowy wynik: '+ str(wynik))

if wynik > 6:
    finalnaPozycja = mc.player.getTilePos()
    mc.setBlocks(finalnaPozycja.x-5, finalnaPozycja.y+10, finalnaPozycja.z-5,
                 finalnaPozycja.x+5, finalnaPozycja.y+10, finalnaPozycja.z+5, 38)
