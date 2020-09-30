from mcpi.minecraft import Minecraft

mc = Minecraft.create()

haslo = 'Moje tajemnicze haslo'

odpowiedz = input('Podaj haslo dostepu: ')
print('Twoja odpowiedz to: ' +odpowiedz)

if odpowiedz == haslo:
    mc.postToChat('Twoja odpowiedz jest prawidlowa')

mc.postToChat(odpowiedz)