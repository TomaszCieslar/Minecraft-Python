from mcpi.minecraft import Minecraft

mc = Minecraft.create()

odleglosc_od_kaktusa = 20
odleglosc_od_domu = 30

wynik = odleglosc_od_kaktusa == 20 and odleglosc_od_domu == 30
mc.postToChat(str(wynik))

wynik = odleglosc_od_kaktusa == 20 or odleglosc_od_domu == 30
mc.postToChat(str(wynik))

# OR
#----------------------------------------------
# Warunek 1          Warunek 2           Wynik
#----------------------------------------------
#  TRUE               TRUE               TRUE
#  TRUE               FALSE              TRUE
#  FALSE              TRUE               TRUE
#  FALSE              FALSE              FALSE






# AND
#----------------------------------------------
# Warunek 1          Warunek 2           Wynik
#----------------------------------------------
#  TRUE               TRUE               TRUE
#  TRUE               FALSE              FALSE
#  FALSE              TRUE               FALSE
#  FALSE              FALSE              FALSE