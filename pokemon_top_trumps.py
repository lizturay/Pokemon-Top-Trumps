import random
import requests

limit = int(input("To end the game, how many points should be reached?: "))
print(
    "Select a pokemon and compare stats or fight. Whoever reaches {} points first wins. It is 100 points to win and a draw is at 50 points".format(limit))

#The first and main functions that draws information from the API.
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    stats_key = pokemon['stats']
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base experience': pokemon['base_experience'],
        'hp': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defend': pokemon['stats'][2]['base_stat']
    }


my_score = 0
opponent_score = 0

#Prompts to create loops for selected variables.
def game(my_score, opponent_score):
    global my_pokemon
    my_pokemon = random_pokemon()
    global opponent_pokemon
    opponent_pokemon = random_pokemon()
    print("You got: {}".format(my_pokemon['name']))
    player_or_computer = input("Would you like to choose the stat or let the opponent? me/opponent: ")
    if player_or_computer == 'me':
        stat_choice = input(
            "Which stat would you like to use id, height, weight, base experience or hp? would you like to attack your opponent or defend yourself from their attack?: ")
    else:
        number = random.randint(1, 7)
        if number == 1:
            stat_choice = 'id'
            print("Stat choice is {}".format(stat_choice))
        elif number == 2:
            stat_choice = 'height'
            print("Stat choice is {}".format(stat_choice))
        elif number == 3:
            stat_choice = 'weight'
            print("Stat choice is {}".format(stat_choice))
        elif number == 4:
            stat_choice = 'base_experience'
            print("Stat choice is {}".format(stat_choice))
        elif number == 5:
            stat_choice = 'hp'
            print("Stat choice is {}".format(stat_choice))
        elif number == 6:
            stat_choice = 'attack'
            print("Stat choice is {}".format(stat_choice))
        else:
            stat_choice = 'defend'
            print("Stat choice is {}".format(stat_choice))

#Depending on the randomised choice the results for the chosen play is shown.
    global opponent_stat
    opponent_stat = opponent_pokemon[stat_choice]
    global my_stat
    my_stat = my_pokemon[stat_choice]
    print("Opponent chose: {}".format(opponent_pokemon['name']))
    global mypokemonname
    mypokemonname = my_pokemon['name']
    global opponentpokemonname
    opponentpokemonname = opponent_pokemon['name']

    the_score = fight(stat_choice)

    my_points = the_score['my_scored']
    opponent_points = the_score['opponent_scored']
    my_score += my_points
    opponent_score += opponent_points
    print("Your points: " + str(my_score))
    print("Opponents points: " + str(opponent_score))

    return {'my_score': my_score, 'opponent_score': opponent_score}

#Based on the chosen variable, the play will be confirmed with either of these prints
def stats(my_stat, opponent_stat):
    if my_stat > opponent_stat:
        print('You win!')
        my_scored = 100
        opponent_scored = 0
    elif my_stat < opponent_stat:
        print('Opponent wins!')
        my_scored = 0
        opponent_scored = 100
    else:
        print('Draw!')
        my_scored = 50
        opponent_scored = 50
    return {'my_scored': my_scored, 'opponent_scored': opponent_scored}

#Based on the chosen variable, the play will be confirmed with either of these outcomes
def fight(stat_choice):
    if stat_choice == 'attack':
        the_score = stats(my_pokemon['attack'], opponent_pokemon['defend'])
        print("{} is attacking {}".format(mypokemonname, opponentpokemonname))
    elif stat_choice == 'defense':
        the_score = stats(my_pokemon['defense'], opponent_pokemon['attack'])
        print("{} is attacking {}".format(opponentpokemonname, mypokemonname))
    else:
        the_score = stats(my_stat, opponent_stat)
    return the_score

#Results of what each player got.
while True:
    game_play = game(my_score, opponent_score)
    my_score = game_play['my_score']
    opponent_score = game_play['opponent_score']
    if (my_score or opponent_score) >= limit:
        break
