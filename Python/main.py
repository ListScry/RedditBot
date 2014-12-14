from time import sleep
API_KEY = ''

import riotwatcher
rw = riotwatcher
w = rw.RiotWatcher(API_KEY)

map_nameToId = {}
map_idToSumm ={}

#class Summoner:
#    def __init__(self):
#        self.base_loaded = False
#        self.stats_loaded = False
    
#    def initBase():
#        #DEFINE THIS

class Cache:
    def __init__(self):
        self.map_nameToId = {}
        self.map_idToSumm = {}
    
    def storeSummonerBase(self,_name,_data):
        summ_id = _data[_name]['id']
        self.map_nameToId[_name] = summ_id
        self.map_idToSumm[summ_id] = _data[_name]
    
    def lookupSummonerBase(self,_name):
        summ_id = self.map_nameToId[_name]
        return self.map_idToSumm[summ_id]
        
#Create instance of Cache
cache = Cache()

def getRankedStats(_region, _summ_id):
    w.get_ranked_stats(summ_id,_region)

def loadSummonerBase(_region,_names):
    results = w.get_summoners(region=_region,names=_names)
    for summ_name in results:
        cache.storeSummonerBase(summ_name,results)
        

"""
summ_list = ['lightscry','hiimislonkfrompa','hiimpetchfromtexas','bigduckyd','fun e n coo','zookycakes']
loadSummonerBase(rw.NORTH_AMERICA,summ_list)
print(cache.lookupSummonerBase('lightscry'))
"""



#GAMES LOOKUP

TEST_ID = 25145748

recent_games = w.get_recent_games(TEST_ID,rw.NORTH_AMERICA)['games']
match_ids = []
match_datas = []

# Extract recent games from a single Summoner's profile
for game in recent_games:
    match_ids.append(game['gameId'])

# Lookup each match individually
for match_id in match_ids:
    print "Loading " + str(match_id) + "..."
    match = w.get_match(match_id,rw.NORTH_AMERICA)
    print match
    sleep(2)

print match_data
