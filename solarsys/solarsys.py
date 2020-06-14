<<<<<<< HEAD
from solarsys.celestialbody import earth, jupiter, mars, mercury, neptune, saturn, uranus, venus
=======
from solarsys.celbody_planets import earth, jupiter, mars, mercury, neptune, saturn, uranus, venus
>>>>>>> master
import collections

def make(planet): 
    if planet == 'Earth' or planet == 'earth':
        data = earth.make()
    elif planet == 'Jupiter' or planet == 'jupiter':
        data = jupiter.make()
    elif planet == 'Mars' or planet == 'mars':
        data = mars.make()
    elif planet == 'Mercury' or planet == 'mercury':
        data = mercury.make()
    elif planet == 'Neptune' or planet == 'neptune':
        data = neptune.make()
    elif planet == 'Saturn' or planet == 'saturn':
        data = saturn.make()
    elif planet == 'Uranus' or planet == 'uranus':
        data = uranus.make()
    elif planet == 'Venus' or planet == 'venus':
        data = venus.make()
    else:
        data = None
        print('Planet not found!  \n\t\tAvoid all capitial letters.')
        
    return data

def listize_string(planet):
    if type(planet) == list:
        pass
    if type(planet) == str:
        planet = [planet, ]
        
    return planet
        
def make_bodies(planet):
    bodies = listize_string(planet)
    body_data = {}
    
    for b in bodies:
        temp = make(b)
        body_data.update(temp)
        
    return body_data

def get(planet):
    """Obtain details regarding a specific planet in the libray.
    Parameters
    ----------
    planet : string or list of strings
        name of planet in the solar system
        
    Return
    ----------
    data :  dictionary of various facts specifc to the planet
    """
    
    data = make_bodies(planet)
    
    return data

def get_all_sorted(sort='alphabetical', cb_type='planet'):
    """Lists celesital bodies in our solar system by a specified sorting parameter.
    Parameters
    ----------
    sort : string 
        specified order: 'alphabetical' or 'positional' (increasing distance from Sun)
    cb_type : string 
        celestial body type in our solar system: 'planet' 
        - only planets are supported at this time
    
        
    """
    if cb_type == 'planet':
        pass
    elif cb_type == 'drawf planet':
        print(f'Feature not yet available for {cb_type}!!\n')
        raise
    else:
        print('Invalid argument for cb_type')

    if sort == 'positional' or sort == 'alphabetical':
        print(f'{cb_type} in {sort} order:\n\n')
    else:
        print('Invalid argument for sort')

            
    
    all_cb = ['venus', 'uranus', 'saturn', 'neptune', 'mercury', 'mars', 'jupiter','earth'] #TODO this is a bad practice, do best to get possible modules
    bodies = get(all_cb)

    temp_dict = {}

    for body in bodies:
        temp_type = bodies[body]['type']
        if sort == 'alphabetical':
            temp = {body : bodies[body]['order']}
        if sort == 'from sun':
            temp = {bodies[body]['order']:body }
            #print(temp)
        temp_dict.update(temp)
        
    od = collections.OrderedDict(sorted(temp_dict.items()))
    
    for k, v in od.items(): 
        print(f'{k:<8}:\t{v}')

    
    
    
<<<<<<< HEAD
    
=======
    
>>>>>>> master
