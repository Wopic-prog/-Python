def find_common_participants(group1, group2, delimiter=","):
    """
    Finds common participants in two groups.

    Args:
        group1 (str): A string of participants in the first group separated by the given delimiter.
        group2 (str): A string of participants in the second group separated by the given delimiter.
        delimiter (str): The delimiter used to separate participants in the strings. Defaults to ','.

    Returns:
        list: A sorted list of common participants.
    """
    # Split the input strings into sets
    set1 = set(group1.split(delimiter))
    set2 = set(group2.split(delimiter))

    # Find the intersection of both sets
    common_participants = sorted(set1 & set2)

    return common_participants

# Example usage
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# Using default delimiter (comma)
common = find_common_participants(participants_first_group, participants_second_group)
print("Common participants:", common)

# Testing with a different delimiter
test_group1 = "Иванов|Петров|Сидоров"
test_group2 = "Петров|Сидоров|Смирнов"
common = find_common_participants(test_group1, test_group2, delimiter="|")
print("Common participants with '|':", common)
