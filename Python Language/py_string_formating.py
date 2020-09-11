def print_formatted(number):
    n_bin_len = str(len("{0:b}".format(number)))
    print_format = '{0:' + n_bin_len + 'd} '
    print_format = print_format + '{0:' + n_bin_len + 'o} '
    print_format = print_format + '{0:' + n_bin_len + 'X} '
    print_format = print_format + '{0:>' + n_bin_len + 'b}'
    # print(print_format)
    for n in range(1, number + 1):
        print(print_format.format(n, n, n, n))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
