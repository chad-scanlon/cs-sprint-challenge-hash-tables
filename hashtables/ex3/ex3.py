def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for item in arrays:
        for num in item:
            # check if it's in dict
            if num in cache:
                cache[num] = cache[num] + 1
            else:
                # add it to dict
                cache[num] = 1
    
    # initialize list of shared values 
    vals = list(filter(lambda x: x[1] == len(arrays), cache.items()))
    for item in vals:
        result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
