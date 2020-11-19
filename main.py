from src.orchestration.orchestrator import Orchestrator
from src.sportsbooks.betfast_nfl_scrape import BetFastAction
from src.sportsbooks.pgw_nfl_scrape import PGW


def main():
    orch = Orchestrator([BetFastAction(), PGW()])
    orch.orchestrate()


if __name__ == "__main__":
    main()
