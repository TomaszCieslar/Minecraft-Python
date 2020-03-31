from mcpi.minecraft import Minecraft

mc = Minecraft.create()

haslo = 'Moje tajemne haslo'

odpowiedz = input('Podaj haslo dostępu')

if odpowiedz == haslo:
    mc.postToChat('To jest wlasciwa odpowiedz')

mc.postToChat('koniec dzialania programu')