API_KEY = '5e31d841-243d-477c-b9c2-d0515c1a158b'

import riotwatcher
rw = riotwatcher
w = rw.RiotWatcher(API_KEY)

idToName = []


def getRankedStats(region, summ_id):
    w.get_ranked_stats(summ_id);
    

def mapSummonerNames(_region,_names):
    results = w.get_summoners(region=_region,names=_names)
    for result in results:
        idToName[result.name] = result

summ_list = ['lightscry','hiimislonkfrompa','hiimpetchfromtexas','bigduckyd','fun e n coo','zookycakes']

result = getSummonersList(rw.NORTH_AMERICA,summ_list)
print(result)