from mcpi.minecraft import Minecraft

mc = Minecraft.create()

odpowiedz = input('Czy chcesz zrobic dziure? t/n: ')
pozycja = mc.player.getTilePos()

if odpowiedz == 't':
    mc.postToChat('dziura wykopana')
    mc.setBlocks(pozycja.x+1, pozycja.y+1, pozycja.z+1, pozycja.x-1, pozycja.y-1, pozycja.z-1,0)
else:
    mc.postToChat('nie kopiemy')
