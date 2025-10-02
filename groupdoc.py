#print "hello"
print("hello")
def jimmy(key_words, history):
    """
    Detect negative and inappropriate comments through sentiment analysis. If more than 70% of their comments are negative, the user is flagged for

    key_words: A list of words that indicate negative sentiment.
    history: A list of user comments to analyze
    
    returns a flag whether the user history indicates troll or not.


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