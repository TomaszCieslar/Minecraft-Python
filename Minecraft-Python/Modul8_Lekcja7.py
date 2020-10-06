from mcpi.minecraft import Minecraft

mc = Minecraft.create()

magiczne_miejsce = True

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
z = int(input('Podaj z: '))

if -100 < x < 100:
    magiczne_miejsce = False
if -100 < y < 100:
    magiczne_miejsce = False
if -100 < z < 100:
    magiczne_miejsce = False

if magiczne_miejsce:
    mc.player.setPos(x,y,z)
else:
    mc.postToChat('Pozycja nie jest prawidlowa')

mc.postToChat('Koniec dzialania programu')