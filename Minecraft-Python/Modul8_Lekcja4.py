from mcpi.minecraft import Minecraft

mc = Minecraft.create()

odpowiedz = input('Czy chcesz niszczyc swiat? t/n: ')

if odpowiedz == 't':
    mc.setting('world_immutable', False)
    mc.postToChat('Swiat da sie zniszczyc')
else:
    mc.setting('world_immutable', True)
    mc.postToChat('Swiata nie da sie niszczyc')


mc.postToChat('Koniec dzialania programu')