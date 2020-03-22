from mcpi import minecraft
from mcpi import block
import random

mc = minecraft.Minecraft.create()

mc.postToChat('komunikat z Pythona')
gracz = mc.player.getTilePos()

mc.postToChat(gracz.x)

bloczek = block.AIR

for x in range(20):
    for y in range(20):
        for z in range(20):
            mc.setBlock(gracz.x+x,gracz.y+y,gracz.z+z, bloczek)


