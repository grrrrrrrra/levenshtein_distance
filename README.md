# Levenshtein Distance with Custom Costs

This script calculates the Levenshtein distance between two strings, allowing the user to specify custom costs for insertion, deletion, and replacement operations.

## Description

The Levenshtein distance is a metric for measuring the difference between two sequences. It is defined as the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other. In this implementation, the user can define specific costs for each type of operation, making the metric more flexible for various use cases.

## Why

The Levenshtein distance is a powerful tool for various applications, including:

- Spell Checking: Identifying and correcting spelling errors in text.
- DNA Sequencing: Comparing genetic sequences to identify mutations or similarities.
- Natural Language Processing: Measuring the similarity between words or phrases for tasks like text classification and machine translation.
- Data Cleaning: Detecting and correcting errors in datasets, such as typos in names or addresses.

By allowing custom costs for different operations, this script provides greater flexibility and can be tailored to specific use cases where certain types of edits are more or less likely or costly.

### Example

Enter the first word: kitten
Enter the second word: sitting
Enter the costs for insertion, deletion, and replacement: 1 1 2
Optimal cost: 5

In this example:

    The insertion cost is 1.
    The deletion cost is 1.
    The replacement cost is 2.

The optimal cost of 5 represents the minimal number of operations needed to transform "kitten" into "sitting" with the specified costs.

## Installation

This script does not require any additional dependencies and runs on standard Python 3.x.

## Usage

1. Run the script.
2. Input two words you want to compare.
3. Specify the costs for insertion, deletion, and replacement operations.

### Input Format
- **First Word**: The first string to compare.
- **Second Word**: The second string to compare.
- **Costs**: Three integers specifying the costs for insertion, deletion, and replacement.

### Output
- The optimal cost of transforming the first word into the second word.

## Code Structure

- \`levenshtein_distance\`: The main function that calculates the Levenshtein distance.
  - **Parameters**:
    - \`word1\`: The first word (string).
    - \`word2\`: The second word (string).
    - \`insert_cost\`: Cost of inserting a character.
    - \`delete_cost\`: Cost of deleting a character.
    - \`replace_cost\`: Cost of replacing a character.
  - **Returns**: The optimal cost of transforming \`word1\` into \`word2\`.
