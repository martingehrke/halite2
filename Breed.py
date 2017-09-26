"""
Welcome to your first Halite-II bot!

This bot's name is Settler. It's purpose is simple (don't expect it to win complex games :) ):
1. Initialize game
2. If a ship is not docked and there are unowned planets
2.a. Try to Dock in the planet if close enough
2.b If not, go towards the planet

Note: Please do not place print statements here as they are used to communicate with the Halite engine. If you need
to log anything use the logging module.
"""
# Let's start by importing the Halite Starter Kit so we can interface with the Halite engine
import hlt
import logging


logging.basicConfig(filename='log', level=logging.INFO)

# GAME START
# Here we define the bot's name as Settler and initialize the game, including communication with the Halite engine.
game = hlt.Game("Breed")

def closest_planet(thing):
    entities = game_map.nearby_entities_by_distance(thing)

    ekeys = sorted(entities.keys())

    #for ekey in ekeys:
        #logging.info(type(entities[ekey]))
        #logging.info(ekey)
        #logging.info(entities[ekey])
        #if type(entities[ekey]) == Planet and not entities[ekey].is_owned():

    logging.info(type(entities[ekeys[0]]))
    return entities[ekeys[0]][0]

while True:
    # TURN START
    # Update the map for the new turn and get the latest version
    game_map = game.update_map()

    # Here we define the set of commands to be sent to the Halite engine at the end of the turn
    command_queue = []
    # For every ship that I control
    for ship in game_map.get_me().all_ships():
        # If the ship is undocked
        if ship.docking_status != ship.DockingStatus.UNDOCKED:
            # Skip this ship
            continue
        
        planet = closest_planet(ship)
        logging.info(planet)

        if ship.can_dock(planet):
            command_queue.append(ship.dock(planet))

        else:
            navigate_command = ship.navigate(ship.closest_point_to(planet), game_map, speed=hlt.constants.MAX_SPEED, ignore_ships=True)
            if navigate_command:
                command_queue.append(navigate_command)


    # TURN END
# GAME END
