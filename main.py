from src.orchestration.orchestrator import Orchestrator
from src.sportsbooks.betfast_nfl_scrape import BetFastAction
from src.sportsbooks.play365_nfl_scrape import Play365
from src.sportsbooks.dog_nfl_scrape import Dog
from src.sportsbooks.falcon_nfl_scrape import Falcon
from src.sportsbooks.bmarket_nfl_scrape import BookieMarket
from src.sportsbooks.all_games_nfl_scrape import AllGames
from src.sportsbooks.rivers_nfl_scrape import Rivers
from src.sportsbooks.draftkings_nfl_scrape import DraftKings
from src.sportsbooks.fanduel_nfl_scrape import Fanduel
from src.sportsbooks.pointsbet_nfl_scrape import PointsBet

def main():
    orch = Orchestrator([BetFastAction(), AllGames(), Dog(), Falcon(), BookieMarket(), Play365(), Rivers(), DraftKings(), Fanduel(), PointsBet()])
    orch.orchestrate()


if __name__ == "__main__":
    main()
