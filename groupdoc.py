import geocoder

#print "hello"
print("hello")

def ask_location():
    """prompts user to indicate a city and state they are in"""
    city = input("Enter the city you are in: ")
    state = input("Enter the state you are in (abbreviation, e.g., CA for California): ")
    location = f"{city}, {state}"
    return location

def get_live_location():
    """this function reports live location while on the app"""
    g = geocoder.ip('me')
    if g.ok:
        return g.city, g.state
    else:
        return None, None