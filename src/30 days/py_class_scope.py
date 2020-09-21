class Difference:
    def __init__(self, a):
        self.__st_elements = sorted(a)
        self.__nb_elements = len(a)
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = abs(self.__st_elements[self.__nb_elements - 1] - \
                                 self.__st_elements[0])
        # self.maximumDifference = abs(max(self.__elements) - min(self.__elements)

if __name__ == '__main__':
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)