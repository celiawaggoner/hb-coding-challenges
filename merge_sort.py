def merge_sort(lst):
    """Reduce given list to lists of 0 or 1 items, and then recombine."""

    if len(lst) > 1:
        mid = len(lst) / 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        new_index = 0

        # compare items in both lists and assign into new list accordingly

        while left_index < len(left) and right_index <len(right):
            if left[left_index] < right[right_index]:
                lst[new_index] = left[left_index]
                left_index += 1
            else:
                lst[new_index] = right[right_index]
                right_index += 1
            new_index += 1

        # if there is any remainder, add it to the longer list

        while left_index < len[left]:
            lst[new_index] = left[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right):
            lst[new_index] = right[right_index]
            right_index += 1
            new_index += 1