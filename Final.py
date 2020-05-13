#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IS210 Gabriel Santos 5/13/2020
#CUNY SPS


def matchmaking(players, teams=3, min_team=1, max_team=None):
    """This function produces a list of players, segregated into the teams.
    Args:
        players(a list): a list of tuples of usernames and connection strength
        for each users.
        teams(int): the number of teams to build for this game, defaults to 3.
        min_team(int, optional): the minimum numbe of players per team, default to 1.
        max_team(int, optional): the maxium number of players per team, default to None.
        
    Returns: 
        a list of players, segregated into the teams.
    
    Examples:
        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)] 
        >>> matchmaking(players, teams=1, min_team=1, max_team=1)
        
        [['a']]
    """
    players_list = filter_players(players, teams=3, max_team=None)
    possible_team = (len(players_list)-(len(players_list)) % teams)/teams
    #From the tip.Initializing our game and (empty) teams using a list comprehension 
    
    game = [[] for i in range(teams)]
    if (max_team is not None and max_team >= possible_team >= min_team)        or (max_team is None and possible_team >= min_team):
        players_number = teams * possible_team
        actual_players = players_list[0:players_number]
        for player in actual_players:
            i = (actual_players.index(player)) % teams
            game[i].append(player)
        return game
    
    elif max_team is not None and possible_team > max_team:
        players_number = teams * max_team
        actual_players = players_list[0:players_number]
        for player in actual_players:
            i = (actual_players.index(player)) % teams
            game[i].append(player)
        return game
    
    else:
        return False
    
    
def filter_players(players, teams=3, max_team=None):
    """This function filters out players and produces a lists of players.
    Args:
        players(a list): a list of tuples of usernames and connection strength
        for each users.
        teams(int): the number of teams to build for this game, defaults to 3.
        max_team(int, optional): the maxium number of players per team, default to None.
        
    Returns:
        list of filtered players.
    
    Examples:
        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)] 
        >>> filter_players(players, teams=1, min_team=1)
        
        [['a', 'c', 'd', 'e', 'f']]
    """
    players_list = []
    for player in players:
        if max_team is not None and player[1] is 1:
            while len(players_list) <= teams * max_team:
                players_list.append(player[0])
                
        elif max_team is None and player[1] is 1:
            players_list.append(player[0])
            
    return players_list

