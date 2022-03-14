#convert claim to uppercase
claim = "Pluto is a planet!"
claim_in_upper = claim.upper()
print(claim_in_upper)

#convert claim to lower
claim_in_lower = claim.lower()
print(claim_in_lower)

# Use a function that checks whether `claim` starts with the substring 'Pluto'
def start_string(claim = "Pluto is a planet!") :
    return claim.startswith("Pluto")

# Use a function that checks whether `claim` ends with the substring 'Test'
def end_string(claim = "Pluto is a planet!") :
    return claim.endswith("Test")

# Dict comprehensions!
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Create a dictionary that maps every name to its first letter
dict = {'Mercury' : 'M', 'Venus' : 'V', 'Earth' : 'E', 'Mars' : 'M', 
        'Jupiter' : 'J', 'Saturn' : 'S', 'Uranus' : 'U', 'Neptune' : 'N'}

# Check if a value is in the dictionary. For example, check if Earth is a planet
def check_elem_in_dict(dict, element):
    for elem in dict.keys() :
        if elem == element : 
            return True
    
numbers = {'one':1, 'two':2, 'three':3}
# Loop over the `numbers` dictionary so as to get both the key and value at each step.
# Try to get the same output that is in the previous step
def print_dict(dict) :
    pass