def saddle_points(matrix):

    if len(matrix) == 0:
        return []

    if not is_matrix_ok(matrix):
        raise ValueError("Matrix non acceptable")




    print(matrix)
    founded_saddles = []

    # extracting columns
    columns = [[col[row] for col in matrix] for row in range(len(matrix[0]))]

    for row in range(len(matrix)):
        row_candidate, col_indexes = find_candidate(matrix[row], "max")
        for col_index in col_indexes:
            col_candidate, row_index =  find_candidate(columns[col_index], "min")

            if row_candidate == col_candidate:

                founded_saddles.append({"row": row+1, "column": col_index+1})

    print(founded_saddles)
    return founded_saddles

def find_candidate(number_list, max_or_min):
    """

    :param row: a list of numbers
    :return: all max(row) numbers and their index in the list
    """
    local_number_list = number_list[:]

    if max_or_min == "max":
        candidate = max(local_number_list)
    elif max_or_min == "min":
        candidate = min(local_number_list)
    else:
        raise TypeError("Function not recognized")

    candidate_index_list = []

    while local_number_list.count(candidate) > 0:
        candidate_index = local_number_list.index(candidate)
        candidate_index_list.append(candidate_index)
        local_number_list[candidate_index] = ""
    return candidate, candidate_index_list

def is_matrix_ok(matrix):

    len_row = len(matrix[0])
    for row in matrix:
        for elem in row:
            if not str(elem).isnumeric():
                return False
        if len(row) != len_row:
            return False
    return True



matrix = [[3, 2, 1], [0, 1], [2, 1, 0]]

print(is_matrix_ok(matrix))