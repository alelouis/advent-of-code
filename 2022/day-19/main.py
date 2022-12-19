import re, math
from copy import copy

def can_buy(botty, bpid, costs, res): return all((res[name]-costs[bpid][botty][name]) >= 0 for name in order)
def get_maximums(costs, bpid): return {name : max(costs[bpid][r][name] for r in order) for name in order}
def get_geode_bound(mmax, minute, robots, res): return (int(((mmax-minute)*(mmax-minute+1))/2) + robots['geo'] * (mmax-minute) + res['geo'])
def buy_robot(botty, bpid, costs, res, robots): return dict(res={name : res[name] - costs[bpid][botty][name] for name in order}, robots={k:v + int(botty==k) for k,v in robots.items()})
    
def buy_all_the_bots(res, robots, minute, bpid, memo, maximums, mmax):
    key = f'{res}_{robots}_{minute}'
    if minute == mmax:
        memo['max'] = max(memo['max'], res['geo'])
        return res['geo']
    if get_geode_bound(mmax, minute, robots, res) < memo['max']: return res['geo']
    if key in memo: return memo[key]
    else:
        if can_buy('geo', bpid, costs, res): 
            states = [buy_robot('geo', bpid, costs, copy(res), copy(robots))]
        else:
            states = [buy_robot(buy, bpid, costs, copy(res), copy(robots)) for buy in [bot for bot in order if can_buy(bot, bpid, costs, res) and robots[bot] < maximums[bot]]]
            if res['ore'] < 5: # hmmmmmmmmmmmmmmm
                states.append({'res':res, 'robots':robots}) 
        for state in states: state['res'] = {name: state['res'][name] + robots[name] for name in order}
        memo[key] = max([buy_all_the_bots(s['res'], s['robots'], minute+1, bpid, memo, maximums, mmax) for s in states])
    return memo[key]

blueprints = open('input').readlines()
costs, order = {}, ['ore', 'clay', 'obs', 'geo']
init_res, init_bot = dict(ore=0, clay=0, obs=0, geo=0), dict(ore=1, clay=0, obs=0, geo=0)

for blueprint in blueprints:
    numbers = list(map(int, re.findall(r'\d+', blueprint)))
    costs[numbers[0]] = dict(ore=dict(ore=numbers[1], clay=0, obs=0, geo=0), clay=dict(ore=numbers[2], clay=0, obs=0, geo=0), obs=dict(ore=numbers[3], clay=numbers[4], obs=0, geo=0), geo=dict(ore=numbers[5], clay=0, obs=numbers[6], geo=0))

print(sum([bpid * buy_all_the_bots(init_res, init_bot, 0, bpid, {'max':0}, get_maximums(costs, bpid), 24) for bpid in costs]))
print(math.prod([buy_all_the_bots(init_res, init_bot, 0, bpid, {'max':0}, get_maximums(costs, bpid), 32) for bpid in {1:costs[1], 2:costs[2], 3:costs[3]}]))