from mcpi.minecraft import Minecraft

mc = Minecraft.create()

odpowiedz = int(input('Wprowadz miejsce'))

if odpowiedz == 1 :
    mc.player.setPos(123,345,23)
elif odpowiedz == 2:
    mc.player.setPos(34,56,122)
elif odpowiedz == 3:
    mc.player.setPos(67,787,23)
elif odpowiedz == 4:
    mc.player.setPos(678,12,890)
else:
    mc.postToChat('Nie ma takiego miejsca')

mc.postToChat('koniec dzialania programu')