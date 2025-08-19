def hystorian_histeria(left_list, second_list):

    left_list.sort()
    second_list.sort()

    distance = 0

    for i in range(len(left_list)):
        distance += abs(left_list[i] - second_list[i])
    
    print(distance)

    return distance