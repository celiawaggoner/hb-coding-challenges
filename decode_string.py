def decode(s):
    """Decode a string."""

    #initialize empty string as ouput word
    word = ""

    index = 0

    while index < len(s):

        skip_num = int(s[index])

        index += skip_num + 1

        word += s[index]

        index +=1

    return word

print decode("0h1ae2bcy")