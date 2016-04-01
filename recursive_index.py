def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion.
    """

    def _recursive_index(needle, haystack, start):

        if start == len(haystack):
            return None

        if haystack[start] == needle:
            return start

        return _recursive_index(needle, haystack, start + 1)


    return _recursive_index(needle, haystack, 0)