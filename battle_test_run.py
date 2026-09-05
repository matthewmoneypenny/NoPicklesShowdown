import asyncio
from player_monte_carlo import monte_carlo_bot

# To run server:
# (in powershell)
# cd C:\Users\matth\Desktop\Projects\NoPicklesPKSD\pokemon-showdown
# node pokemon-showdown start --no-security

from poke_env.player import RandomPlayer
from poke_env.player import MaxBasePowerPlayer


async def main():
    player_1 = monte_carlo_bot(max_concurrent_battles=1)
    player_2 = MaxBasePowerPlayer(max_concurrent_battles=1)

    await player_1.battle_against(player_2, n_battles=1000)

    print(f"Finished battles: {player_1.n_finished_battles}")
    print(f"Player 1 wins: {player_1.n_won_battles}")


if __name__ == "__main__":
    asyncio.run(main())