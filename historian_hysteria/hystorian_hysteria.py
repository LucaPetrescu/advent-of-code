def hystorian_histeria():
    inputs = open_inputs_file("__tests__/inputs.txt")

    left_list, second_list = group_numbers_in_columns(inputs)


    left_list.sort() 
    second_list.sort()

    distance = 0

    for i in range(len(left_list)):
        distance += abs(left_list[i] - second_list[i])
    
    print(distance)

    return distance

def open_inputs_file(file_name):
    read_lines = []
    f = open(file_name, "r")
    lines = f.readlines()
    for line in lines:
        read_lines.append(line.split())
    f.close()
    return read_lines

def group_numbers_in_columns(inputs):
    first_column = []
    second_column = []
    
    for input_row in inputs:
        if len(input_row) >= 2:  # Make sure we have at least 2 elements
            first_column.append(int(input_row[0]))
            second_column.append(int(input_row[1]))
    
    return first_column, second_column

def main():
    hystorian_histeria()

if __name__ == "__main__":
    main()