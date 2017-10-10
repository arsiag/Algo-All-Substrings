def lstSubStrings(s):
    # when s is empty return the empty string
    if(len(s) is 0):
        return [s]
    substrs = []
    # a string is a substring of itself
    substrs.append(s)
    # extend the list of substrings by all substrings with the first character cut out
    substrs.extend(lstSubStrings(s[1:]))
    # extend the list of substrings by all substrings with the last character cut out
    substrs.extend(lstSubStrings(s[:-1]))
    # convert the list to `set`, removing all duplicates, and convert back to a list
    substrs = list(set(substrs))

    return substrs

print lstSubStrings("Hey") # ['', 'y', 'H', 'Hey', 'He', 'e', 'ey']