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
    fibo: int
    next_fibo: int
    max_iterations: int

    def __init__(self, max_iterations):
        self.max_iterations = max_iterations

    def __iter__(self):
        self.fibo = 0
        self.next_fibo = 1
        return self

    # 0, 1, 1, 2, 3, 5
    def __next__(self):
        x = self.fibo
        if self.max_iterations < 0:
            raise StopIteration
        else:
            self.fibo = self.next_fibo
            self.next_fibo += x
            self.max_iterations -= 1
        return x


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
