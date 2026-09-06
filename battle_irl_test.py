from hidden import USERNAME, PASSWORD

# This file was originally written by Claude.

import asyncio
from player_monte_carlo import monte_carlo_bot
from poke_env import AccountConfiguration

async def main():
    bot = monte_carlo_bot(battle_format="gen9randombattle", log_level=20, account_configuration=AccountConfiguration(USERNAME, PASSWORD))
    print("bot username:", bot.username)
    await bot.accept_challenges(None, 1)   # None = accept from anyone

asyncio.run(main())