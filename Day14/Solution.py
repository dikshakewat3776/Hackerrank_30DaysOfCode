class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        self.min_element = 101
        self.max_element = 0

    def computeDifference(self):
        for element in self.__elements:
            if element < self.min_element:
                self.min_element = element
            if element > self.max_element:
                self.max_element = element

        self.maximumDifference = self.max_element - self.min_element

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)