import geocoder

print("hello")

def ask_location():
    """Prompts user to indicate a city and state they are in."""
    city = input("Enter the city you are in: ")
    state = input("Enter the state you are in (abbreviation, e.g., CA for California): ")
    location = f"{city}, {state}"
    return location

def get_live_location():
    """Reports live location while on the app."""
    g = geocoder.ip('me')
    if g.ok:
        return g.city, g.state
    else:
        return None, None

def jimmy(key_words, history):
    """
    Detect negative and inappropriate comments through sentiment analysis.
    If more than 70% of comments are negative, the user is flagged.

    key_words: A list of words that indicate negative sentiment.
    history: A list of user comments to analyze.
    
    Returns True if user history indicates trolling, otherwise False.
    """
    negative_count = 0
    total_comments = len(history)

    for comment in history:
        if any(word in comment.lower() for word in key_words):
            negative_count += 1

    if total_comments == 0:
        return False  # No comments to analyze

    negative_ratio = negative_count / total_comments
    return negative_ratio > 0.7  # Flag if more than 70% of comments are negative

# Example usage
if __name__ == "__main__":
    # Location example
    user_location = ask_location()
    print("You entered:", user_location)

    live_city, live_state = get_live_location()
    if live_city and live_state:
        print("Live location detected:", live_city, live_state)
    else:
        print("Could not detect live location.")

    # Troll detection example
    key_words = ["bad", "hate", "stupid", "useless", "idiot", "worst"]
    user_history = [
        "I hate this product",
        "This is the worst service ever",
        "I think this is stupid",
        "I love this!",
        "This is useless"
    ]

    is_troll = jimmy(key_words, user_history)
    print("Is the user a troll?", is_troll)