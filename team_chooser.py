players = ['athena', 'zeus', 'persephone', 'heracles', 'poseidon', 'hades',
'artemis', 'hephaestus', 'hera', 'aphrodite', 'medusa']

teams = ['pegasus', 'cerberus', 'chiron', 'orouborous']

from random import choice

team_a = []
team_b = []

team_a_name = choice(teams)
teams.remove(team_a_name)

team_b_name = choice(teams)

while len(players) > 0:
    player_a = choice(players)
    team_a.append(player_a)
    players.remove(player_a)
    #print "Players left:", players

    if players == []:
        break

    player_b = choice(players)
    team_b.append(player_b)
    players.remove(player_b)
    #print "Players left:", players

#print players
#print teams
#print player_a
#print players
print team_a_name, ":", team_a
print team_b_name, ":", team_b
