def levenshtein_distance(word1, word2, insert_cost, delete_cost, replace_cost):
    # Determine the number of rows and columns for the matrix based on input words
    rows = len(word1) + 1
    cols = len(word2) + 1

    # Initialize a matrix with zeros
    matrix = [[0] * cols for _ in range(rows)]

    # Fill the first row (corresponding to the cost of inserting characters)
    for j in range(1, cols):
        matrix[0][j] = j * insert_cost

    # Fill the first column (corresponding to the cost of deleting characters)
    for i in range(1, rows):
        matrix[i][0] = i * delete_cost

    # Main loop to calculate the costs for transforming word1 into word2
    for i in range(1, rows):
        for j in range(1, cols):
            # If characters are the same, no replacement cost; otherwise, use replace_cost
            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = replace_cost

            # Compute the minimum cost among insertion, deletion, and replacement
            matrix[i][j] = min(
                matrix[i - 1][j] + delete_cost,    # Deletion (moving up)
                matrix[i][j - 1] + insert_cost,    # Insertion (moving left)
                matrix[i - 1][j - 1] + cost        # Replacement (moving diagonally)
            )

    # Return the optimal cost from the bottom-right corner of the matrix
    return matrix[-1][-1]

# Example usage
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
insert_cost, delete_cost, replace_cost = map(int, input("Enter the costs for insertion, deletion, and replacement: ").split())

optimal_cost = levenshtein_distance(word1, word2, insert_cost, delete_cost, replace_cost)
print(f"Optimal cost: {optimal_cost}")
