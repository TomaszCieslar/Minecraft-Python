from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pozycja = mc.player.getTilePos()

x = pozycja.x
y = pozycja.y
z = pozycja.z

zagrodaX = 10
zagrodaY = 10
zagrodaZ = 10

jestem_w_srodku = zagrodaX < x and zagrodaY < y and zagrodaZ < z
mc.postToChat('czy jestem w srodku?' +str(jestem_w_srodku))
