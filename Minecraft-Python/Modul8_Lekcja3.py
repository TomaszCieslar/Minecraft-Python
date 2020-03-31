from mcpi.minecraft import Minecraft

mc = Minecraft.create()

odpowiedz = input('Czy chcesz zrobić dziure t/n')
pozycja = mc.player.getPos()


if odpowiedz == 't':
    mc.setBlocks(pozycja.x+1, pozycja.y+1, pozycja.z +1, pozycja.x - 1, pozycja.y-1, pozycja.z - 1, 0)
else:
    mc.postToChat('Nie robimy dziury')


mc.postToChat('koniec dzialania programu')