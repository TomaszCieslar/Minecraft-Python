from mcpi.minecraft import Minecraft

mc = Minecraft.create()

odpowiedz = input('Czy chcesz niszczyc? t/n')

if odpowiedz == 't':
    mc.setting('world_immutable', True)
    mc.postToChat('Swiat da sie niszczyc')
else:
    mc.setting('world_immutable', False)
    mc.postToChat('Swiat nie da sie zniszczyc')


mc.postToChat('koniec dzialania programu')