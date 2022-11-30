import


MAIN_URL = 'http://www.espn.com/nfl/'
PLAYER_LIST_URL = 'http://www.espn.com/nfl/players'
PLAYERS_ID_URL = 'https://www.espn.com/nfl/player/_/id/[ID]/[player]'
PLAYERS_GAMELOG_URL = 'https://www.espn.com/nfl/player/gamelog/_/id/[ID]/[player]'

class 
  
class NFLQuarterbackStats(NFLStats):  
    def keys(): 
        return [ 'id', 'player_id', 'GP', 'CMP', 'ATT', 'YDS', 'TDS', 'INT', 'RTG', 'QBR']
class NFLRunningBackStats(NFLStats):
    def keys(): 
        return [ 'id', 'player_id', 'ATT', 'YDS', 'AVG', 'REC', 'YDS', 'AVG', 'TDS', 'LNG', 'FUM', 'LST']
class NFLRecievingStats(NFLStats):
    def keys(): 
        return ['id', 'player_id', 'REC', 'TGTS', 'YDS', 'AVG', 'TD', 'LNG', 'FD', 'FUM', 'LST']
class NFLDefensiveStats(NFLStats):  
    def keys(): 
        return [ 'id', 'player_id', 'TOT', 'SOLO', 'AST', 'SACK', 'FF', 'FR', 'YDS', 'INT', 'YDS', 'AVG', 'TD', 'LNG', 'PD']
