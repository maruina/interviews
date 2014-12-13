def pythonic_reverse(string):
    return string[::-1]


def built_in_reverse(string):
    result = ''
    for char in reversed(string):
        result += char
    return result


def xrange_reverse(string):
    result = ""
    for i in xrange(len(string) - 1, -1, -1):
        result += string[i]
    return result


def c_reverse(string):

    first_half = ''
    second_half = ''
    l = len(string)

    for i in xrange(0, l / 2):
        first_half += string[l - 1 - i]
        second_half += string[l / 2 - 1 - i]
    if l % 2 != 0:
        first_half += string[l / 2]
    return first_half + second_half


if __name__ == '__main__':

    while True:
        input_string = raw_input()
        if 'QUIT' in input_string:
            break
        print 'You wrote: {}'.format(input_string)
        print 'Pythonic reverse: {}'.format(pythonic_reverse(input_string))
        print 'Built-in reverse: {}'.format(built_in_reverse(input_string))
        print 'Xrange reverse: {}'.format(xrange_reverse(input_string))
        print 'C reverse: {}'.format(c_reverse(input_string))
