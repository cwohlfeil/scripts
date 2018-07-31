from pyrsistent import PClass, pmap_field, field, pmap, pmap_field, pvector_field

class Thing(PClass):
    name = field(basestring)

class Location(PClass):
    name = field(basestring)
    description = field(basestring)
    exits = pmap_field(basestring, tuple)  # direction name -> (required thing, location name)
    items = pmap_field(basestring, Thing)

class GameState(PClass):
    location_name = field(basestring)
    world = pmap_field(basestring, Location)
    inventory = pvector_field(Thing)

    @property
    def location(self):
        return self.world[self.location_name]

ROOM_FORMAT = u"""
* {name} *
{description}

Exits:
{exits}

Items here: {items}
Your inventory: {inventory}
"""

def render(state):
    def render_exit(exit_name, key, destination):
        desc = u'* {} to {}'.format(exit_name, destination)
        return desc + (u' (locked)' if key is not None else '')

    exits = '\n'.join(render_exit(direction, key, destination)
                      for direction, (key, destination) in state.location.exits.items())
    items = ', '.join(state.location.items.keys())
    inventory = ', '.join(item.name for item in state.inventory)
    return ROOM_FORMAT.format(
        name=state.location.name,
        description=state.location.description,
        exits=exits,
        items=items,
        inventory=inventory,
    )

def move(state, exit_name):
    if exit_name not in state.location.exits:
        return None
    (key, location_name) = state.location.exits.get(exit_name)
    if key is not None and key not in state.inventory:
        return None
    #return GameState(location_name=location_name, world=state.world)
    return state.set(location_name=location_name)

def take(state, item_name):
    item = state.location.items.get(item_name)
    if item is None: return None
    return state.transform(
        ['world', state.location.name, 'items'], lambda items: items.remove(item_name),
        ['inventory'], lambda inv: inv.append(item),
    )

key = Thing(name='rusty key')
home = Location(name="Home", description="Home is where the heart is!",
                exits={'east': (None, 'Street'),
                       'down': (key, 'Basement')})
street = Location(name="Street", description="The street next to your house.",
                  exits={'west': (None, 'Home')},
                  items={key.name: key})
basement = Location(name="Basement", description="You found the basement!",
                    exits={'up': (None, 'Home')})
world = pmap({x.name: x for x in [home, street, basement]})
initial_state = GameState(location_name='Home', world=world)

# print(render(move(move(take(move(initial_state, 'east'), 'rusty key'), 'west'), 'down')))

def multimove(state, directions):
    return reduce(move, directions, state)

# print(render(multimove(take(move(initial_state, 'east'), 'rusty key'), ['west', 'down'])))

from toolz.functoolz import thread_first

# print(render(thread_first(
#     initial_state,
#     (move, 'east'),
#     (take, 'rusty key'),
#     (move, 'west'),
#     (move, 'down'))))
