class LinearCongruentialGenerator:
    def __init__(self, seed=1, a=1103515245, c=12345, m=2** 31 - 1):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m


def random_from_list(lst, seed=None):
    if seed is not None:
        generator = LinearCongruentialGenerator(seed=seed)
    else:
        generator = LinearCongruentialGenerator()
    index = int(generator.random() * len(lst))
    return lst[index]


# Example usage:
my_list = [1, 2, 3, 4, 5]
print(random_from_list(my_list))  # Get a random value from the list
