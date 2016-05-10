def insertion_sort(lst):
    """Sort a list using insertion sort"""

    for i in range(1, len(lst)):
        j = i - 1

        while j >= 0 and lst[j] > lst[i]:
            j -= 1

        j += 1

        if j != i:
            lst[j:i + 1] = lst[i:i + 1] + lst[j:i]

    return lst