import asyncio
import random
import math

import ewo


bot = ewo.Player()
bot.wandering = True

@bot.event
async def on_connect():
    print("connect")
    while True:
        if bot.wandering:
            await bot.move(random.choice([ewo.UP, ewo.LEFT]))
        else:
            await asyncio.sleep(0.1)

@bot.event
async def on_state_change(state):
    for entity in state.entities:
        if entity.pos != (0, 0):
            axe, dir = max(enumerate(entity.pos), key=lambda x: abs(x[1]))
            dir = int(math.copysign(1, dir))
            await bot.move([ewo.LEFT, ewo.RIGHT, ewo.UP, ewo.DOWN][axe * 2 + (dir + 1) // 2])
            bot.wandering = False
            break
    else:
        bot.wandering = True

    if all(x is not None and x > -3 for x in state.walls):
        bot.wandering = False

bot.run("Bot")
