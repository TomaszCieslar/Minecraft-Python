from mcpi.minecraft import Minecraft
mc = Minecraft.create()

szerokosc = 5
wysokosc = 5
dlugosc = 5

startX = 227
startY = 66
startZ = 201

pozycja = mc.player.getTilePos()

x = pozycja.x 
y = pozycja.y 
z = pozycja.z 

if startX <= x < startX + szerokosc:
    mc.setBlocks(startX, startY + wysokosc, startZ,
                    startX+szerokosc, startY+wysokosc, startZ+dlugosc,8)
else:
        mc.setBlocks(startX, startY + wysokosc, startZ,
                    startX+szerokosc, startY+wysokosc, startZ+dlugosc,0)

mc.postToChat('koniec gry') 