def missing_number_sort(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing."""

    # 2nd solution: if we can't create another data structure
    #               sort and scan for missing number

    all_nums_in_range = range(1, max_num + 1)
    nums.append(max_num + 1)
    nums.sort()
    last = 0

    for i in nums:
        if i != last + 1:
            return last + 1
        last += 1

    raise Exception("None are missing!")