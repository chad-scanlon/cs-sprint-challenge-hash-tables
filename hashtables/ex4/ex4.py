def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    pos_nums = []
    neg_nums = []

    for num in a:
        if num > 0:
            pos_nums.append(num)
        elif num < 0:
            neg_nums.append(num)
        # print(pos_nums)
        # print(neg_nums)
    pos_num_dict = dict()
    for num in pos_nums:
        pos_num_dict[num] = False

    for num in neg_nums:
        pos_num_dict[abs(num)] = True

    # print(pos_num_dict)
    result = [num[0]
              for num in list(pos_num_dict.items()) if num[1]]
    # print(result)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
