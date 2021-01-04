import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import src.orchestration.orchestrator

from src.orchestration.orchestrator import Orchestrator
from src.sportsbooks.betfast_nfl_scrape import BetFastAction
from src.sportsbooks.play365_nfl_scrape import Play365
from src.sportsbooks.dog_nfl_scrape import Dog
from src.sportsbooks.falcon_nfl_scrape import Falcon
from src.sportsbooks.bmarket_nfl_scrape import BookieMarket
from src.sportsbooks.all_games_nfl_scrape import AllGames
from src.sportsbooks.legal_books_nfl_scrape import LegalBooks

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

orch = Orchestrator([BetFastAction(), AllGames(), Dog(), Falcon(), BookieMarket(), Play365(), LegalBooks('Bet_Rivers_IL'), LegalBooks('Draftkings'), LegalBooks('Fanduel'), LegalBooks('Pointsbet')])
orch.orchestrate(_print = False)

nfl_frame = orch.get_merged_book_frames()

app.layout = dash_table.DataTable(
    id = 'lines',
    columns = [{'name': i, 'id': i} for i in nfl_frame.columns],
    data = nfl_frame.to_dict('records')
)

if __name__ == '__main__':
    app.run_server(debug = True)