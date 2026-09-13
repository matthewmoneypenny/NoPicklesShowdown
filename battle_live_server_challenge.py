# This file was originally written by Claude.

from hidden import USERNAME, PASSWORD
import os
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


import asyncio
from poke_env import AccountConfiguration, ShowdownServerConfiguration
from player_monte_carlo import monte_carlo_bot

async def main():
    bot = monte_carlo_bot(
        account_configuration=AccountConfiguration(USERNAME, PASSWORD),
        server_configuration=ShowdownServerConfiguration,
        battle_format="gen9randombattle",
        start_timer_on_battle_start=False,
    )
    await bot.accept_challenges(None, 10)   # 10 battles before finishing

asyncio.run(main())