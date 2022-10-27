# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
# Example:
#
# for i in FibonacciNumbers(10):
#     print(i)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

print("Task 1. \n")


class FibonacciNumbers:
    n1 = 1
    n2 = 1
    iteration = 0
    max_iterations = 0

    def __init__(self, max_iterations):
        self.max_iterations = max_iterations

    def __iter__(self):
        self.n1 = 1
        self.n2 = 1
        return self

    def __next__(self):
        if self.iteration < self.max_iterations:
            x = self.n1 + self.n2
            self.n1 = self.n2
            self.n2 = x
            self.iteration += 1
            return x
        else:
            raise StopIteration


# 1, 1, 2, 3, 5
for i in FibonacciNumbers(10):
    print(i)
#
# 2.* Implement generator for Fibonacci numbers
#
# 3. Write generator expression that returns square numbers of integers from 0 to 10
#
# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
#
# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.
