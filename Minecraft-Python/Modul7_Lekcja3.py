from mcpi.minecraft import Minecraft
mc = Minecraft.create()

niezmienny_swiat = False

mc.setting('world_immutable', niezmienny_swiat)

print('obecny swiat ma stan immutable: '+ str(niezmienny_swiat))


