class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.__elements = sorted(self.__elements)
        self.maximumDifference = self.__elements[len(self.__elements)-1] - self.__elements[0]

_ = input() # the size of the elements array
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference) #maximumDifference is the instance variable in computeDifference