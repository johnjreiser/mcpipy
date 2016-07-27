#!/usr/bin/env python3

bt = 4   # block type, default cobblestone = 4

import sys
if len(sys.argv) > 1:
    bt = sys.argv[1]   

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()

for x in range( pos.x - 2, pos.x + 3):
    for z in range( pos.z - 2, pos.z + 3):
        if not (pos.x == x and pos.z == z):
             mc.setBlock(float(x), float(pos.y), float(z), float(bt))
