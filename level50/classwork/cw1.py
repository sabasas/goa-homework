# The function is not returning the correct values. Can you figure out why?

# Example (Input --> Output ):

# 3 --> "Earth"

def get_planet_name(id):
    planets = {
        1: "mercury",
        2: "venus", 
        3: "earth",
        4: "mars",
        5: "jupiter",
        6: "saturn", 
        7: "uranus",
        8: "neptune"
    }
    
    return planets[id].capitalize()