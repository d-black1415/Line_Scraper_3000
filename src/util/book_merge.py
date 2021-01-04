from src.orchestration.orchestrator import Orchestrator
from src.sportsbooks.betfast_nfl_scrape import BetFastAction
from src.sportsbooks.play365_nfl_scrape import Play365
from src.sportsbooks.dog_nfl_scrape import Dog
from src.sportsbooks.falcon_nfl_scrape import Falcon
from src.sportsbooks.bmarket_nfl_scrape import BookieMarket
from src.sportsbooks.all_games_nfl_scrape import AllGames
from src.sportsbooks.legal_books_nfl_scrape import LegalBooks
from fuzzywuzzy import process
import pandas as pd
import numpy as np
import pdb 

orch = Orchestrator([BetFastAction(), AllGames(), Dog(), Falcon(), BookieMarket(), Play365(), LegalBooks('Bet_Rivers_IL'), LegalBooks('Draftkings'), LegalBooks('Fanduel'), LegalBooks('Pointsbet')])
orch.orchestrate(_print = False)
frames = orch.get_book_frames()
non_labeled_frames = []
unique_ids = []
team_list = []

for counter, dict_pair in enumerate(frames.items()):
    if counter == 0:
        unique_ids.extend(dict_pair[1]['Team_ID'].astype(str).unique())
    
    else:
        ids = dict_pair[1]['Team_ID'].astype(str).unique()
        unique_ids.extend([team_id for team_id in ids if team_id not in unique_ids and team_id != 'nan'])
unique_ids = sorted(unique_ids)
base_frame = pd.DataFrame(unique_ids, columns = ['Team_ID'])

for counter, dict_pair in enumerate(frames.items()):
    if dict_pair[1]['Team_ID'].isna().sum():
        non_labeled_frames.append(dict_pair)
        
    else:
        temp_name = dict_pair[0]
        temp_frame = dict_pair[1]
        temp_frame = temp_frame.astype({'Team_ID':'str'})
            
        if counter == 0:
            temp_merged_frame = base_frame.merge(temp_frame.add_suffix(f'_{temp_name}'), how = 'outer', left_on = 'Team_ID', right_on = f'Team_ID_{temp_name}')
            first_name = temp_name
        else:
            temp_merged_frame = temp_merged_frame.merge(temp_frame.add_suffix(f'_{temp_name}'), how = 'outer', left_on = 'Team_ID', right_on = f'Team_ID_{temp_name}')
        
        if counter > 0:
            if f'Team_ID_{temp_name}' in temp_merged_frame.columns:
                temp_merged_frame = temp_merged_frame.drop([col + f'_{temp_name}' for col in ['Month','Day','Internal_ID', 'Team_ID']], axis = 1)
            
            else:
                temp_merged_frame = temp_merged_frame.drop([col + f'_{temp_name}' for col in ['Month','Day','Internal_ID']], axis = 1)

        if f'Team_{temp_name}' in temp_merged_frame: 
            team_list.extend([(index,row) for index,row in temp_merged_frame.loc[~temp_merged_frame[f'Team_{temp_name}'].isna(), f'Team_{temp_name}'].iteritems()])

        else:
            team_list.extend([(index,row) for index,row in temp_merged_frame.loc[~temp_merged_frame['Team'].isna(), 'Team'].iteritems()])
            

team_cols = [col for col in temp_merged_frame.columns if 'Team_' in col and col != 'Team_ID']
for index, row in temp_merged_frame.iterrows():
    if row[f'Team_{first_name}'] is np.nan:
        for team in team_cols:
            if row[team] is not np.nan:
                temp_merged_frame.at[index, f'Team_{first_name}'] = row[team]
                break
            
total_team_list = temp_merged_frame[f'Team_{first_name}'].tolist()
for name, frame in non_labeled_frames:
    team_match_dict = dict()
    for team in frame['Team'].tolist():
        team_match_dict[team] = process.extractOne(team, total_team_list)[0]
    
    frame['Team'] = frame['Team'].replace(team_match_dict)
    temp_merged_frame = temp_merged_frame.merge(frame.add_suffix(f'_{name}'), left_on = f'Team_{first_name}', right_on = f'Team_{name}',)
    temp_merged_frame = temp_merged_frame.drop([col + f'_{name}' for col in ['Month', 'Day', 'Internal_ID', 'Team_ID']], axis = 1)

team_cols = [col for col in temp_merged_frame.columns if 'Team_' in col and col not in ['Team_ID', f'Team_{first_name}']]
merged_frame = temp_merged_frame.drop(team_cols, axis = 1)
merged_frame = merged_frame.drop([f'Internal_ID_{first_name}'], axis = 1)
column_rename = {
    f'Month_{first_name}' : 'Month',
    f'Day_{first_name}' : 'Day',
    f'Team_{first_name}' : 'Team',
    }
merged_frame = merged_frame.rename(columns = column_rename)
for index, row in merged_frame.iterrows():
    if row['Month'] is np.nan:
        merged_frame.at[index, 'Month'] = merged_frame.at[index - 1, 'Month']
        merged_frame.at[index, 'Day'] = merged_frame.at[index - 1, 'Day']

merged_frame = merged_frame.replace({np.nan:'Not Found'})

