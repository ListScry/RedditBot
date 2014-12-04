API_KEY = ''

import riotwatcher
rw = riotwatcher
w = rw.RiotWatcher(API_KEY)

idToName ={}


def getRankedStats(region, summ_id):
    w.get_ranked_stats(summ_id);
    

def mapSummonerNames(_region,_names):
    results = w.get_summoners(region=_region,names=_names)
    for result in results:
        print result
        #id = result['id']
        #idToName[id] = result

summ_list = ['lightscry','hiimislonkfrompa','hiimpetchfromtexas','bigduckyd','fun e n coo','zookycakes']

result = mapSummonerNames(rw.NORTH_AMERICA,summ_list)
print(idToName)