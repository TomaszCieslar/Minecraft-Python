from mcpi.minecraft import Minecraft
mc = Minecraft.create()

odleglosc_od_kaktusa = 20
odleglosc_od_domu = 30

wynik = odleglosc_od_kaktusa == 30 and odleglosc_od_domu == 30
mc.postToChat(wynik)

wynik = odleglosc_od_kaktusa == 30 or odleglosc_od_domu == 30
mc.postToChat(wynik)

#And
#Warunek 1       Warunek 2         Wynik
# True                True            True
# True                False           False
# False               True            False
# False               False           False

#Or
#Warunek 1       Warunek 2         Wynik
# True                True            True
# True                False           True
# False               True            True
# False               False           False