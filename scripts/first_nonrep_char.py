def find_first_nonrep(string):
    '''
    Create a hash table for all the char in string.
    Then compare each char to find the first non repeated.
    Complexity O(n)
    '''
    char_dict = {}

    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for char in string:
        if char_dict[char] == 1:
            return char


if __name__ == '__main__':

    test_string = 'mammarata'
    print find_first_nonrep(test_string)
