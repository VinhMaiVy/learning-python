#!/bin/python3

def timeInWords(h, m):
    hours = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve')
    minutes =  ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five','twenty six',
                 'twenty seven','twenty eight','twenty nine')

    if m == 0:
        print(hours[h-1] + ' o\' clock')
    elif m>30:
        if m == 45:
            print('quarter to ' + hours[h])
        else:
            if m == 1:
                m_to = ' minute to '
            else:
                m_to = ' minutes to '
            print(minutes[59-m] + m_to + hours[h])
    else:
        if m == 30:
            print('half past ' + hours[h - 1])
        elif m ==15:
            print('quarter past ' + hours[h - 1])
        else:
            if m == 1:
                m_past = ' minute past '
            else:
                m_past = ' minutes past '
            print(minutes[m-1] + m_past + hours[h - 1])

if __name__ == '__main__':
    h = int(input())
    m = int(input())
    result = timeInWords(h, m)

