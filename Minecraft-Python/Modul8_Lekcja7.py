from mcpi.minecraft import Minecraft

mc = Minecraft.create()

magiczne_miejce = True

x = int(input('Podaj x'))
y = int(input('Podaj y'))
z = int(input('Podaj z'))

if -100 < x < 100:
    magiczne_miejce = False 
if -100 < y < 100:
    magiczne_miejce = False 
if -100 < y < 100:
    magiczne_miejce = False 

if magiczne_miejce:
    mc.player.setPos(x,y,z)
else:
    mc.postToChat('Pozycja nie jest prawidlowa')

mc.postToChat('koniec dzialania programu')