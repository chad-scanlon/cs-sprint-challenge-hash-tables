def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in range(length):
        item = weights[i]
        value = limit - item
        diff = limit - value
        if diff in cache:
            return (i, cache[diff])
        else:
            cache[value] = i

    return None

   
