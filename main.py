from src.orchestration.orchestrator import Orchestrator
from src.sportsbooks.betfast_nfl_scrape import BetFastAction
# from src.sportsbooks.pgw_nfl_scrape import PGW
from src.sportsbooks.dog_nfl_scrape import Dog
from src.sportsbooks.falcon_nfl_scrape import Falcon
from src.sportsbooks.bmarket_nfl_scrape import BookieMarket
from src.sportsbooks.all_games_nfl_scrape import AllGames

def main():
    orch = Orchestrator([BetFastAction(), AllGames(), Dog(), Falcon(), BookieMarket()])
    orch.orchestrate()


if __name__ == "__main__":
    main()
