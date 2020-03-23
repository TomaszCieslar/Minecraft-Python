from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pozycja = mc.player.getPos()
mc.postToChat(pozycja)

x = pozycja.x
y = pozycja.y
z = pozycja.z

typ_bloczka = mc.getBlock(x,y,z)
mc.postToChat(typ_bloczka == 9)


