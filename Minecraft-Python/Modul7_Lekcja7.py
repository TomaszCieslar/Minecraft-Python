from mcpi.minecraft import Minecraft
from minecraft import blocks
import math

mc = Minecraft.create()

moja_odleglosc = 40
odleglosc_od_kaktusa = 20
odleglosc_od_domku = 30

wynik = odleglosc_od_kaktusa == 20 and odleglosc_od_domku > 30   


mc.postToChat(str(wynik))

# AND
#----------------------------------------------
# Warunek 1          Warunek 2           Wynik
#----------------------------------------------
#  TRUE               TRUE               TRUE
#  TRUE               FALSE              FALSE
#  FALSE              TRUE               FALSE
#  FALSE              FALSE              FALSE

# OR
#----------------------------------------------
# Warunek 1          Warunek 2           Wynik
#----------------------------------------------
#  TRUE               TRUE               TRUE
#  TRUE               FALSE              TRUE
#  FALSE              TRUE               TRUE
#  FALSE              FALSE              FALSE