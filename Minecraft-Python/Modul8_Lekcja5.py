from mcpi.minecraft import Minecraft

mc = Minecraft.create()

odpowiedz = int(input('Wprowadz liczbe kaktusow'))

if odpowiedz > 20 :
    mc.postToChat('Bardzo duzo kaktusow')
elif odpowiedz > 5:
    mc.postToChat('Malo kaktusow')
elif odpowiedz == 0:
    mc.postToChat('Brak katusow')
else:
    mc.postToChat('Ta liczba jest chyba niewlasciwa')

mc.postToChat('koniec dzialania programu')