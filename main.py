from abc import abstractmethod, ABC

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
print("\nTask 2. \n")


def fibo_gen():
    fibo = 0
    next_fibo = 1
    for fib in range(11):
        yield fibo
        x = fibo
        fibo = next_fibo
        next_fibo += x


fibo_list = fibo_gen()
for lst in fibo_list:
    print(lst)

# 3. Write generator expression that returns square numbers of integers from 0 to 10
#
print("\nTask 3. \n")


def square_int():
    for n in range(11):
        yield n ** 2


square_list = square_int()
for lst in square_list:
    print(lst)

# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
#
print("\nTask 4. \n")


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    __screen: str
    __keyboard: str
    __touchpad: bool
    __webcam: bool
    __ports: list
    __dynamics: bool

    def __init__(self, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.__screen = screen
        self.__keyboard = keyboard
        self.__touchpad = touchpad
        self.__webcam = webcam
        self.__ports = ports
        self.__dynamics = dynamics

    def screen(self):
        print(f"HP laptop screen resolution is: {self.__screen} inches.")

    def keyboard(self):
        print(f"HP laptops have a {self.__keyboard} keyboard.")

    def touchpad(self):
        if self.__touchpad:
            print("HP laptops have a touchpad.")
        else:
            print("HP laptops don't have a touchpad.")

    def webcam(self):
        if self.__webcam:
            print("HP laptops have a webcam.")
        else:
            print("HP laptops don't have a webcam.")

    def ports(self):
        print(f"HP laptops have the following ports: {self.__ports}")

    def dynamics(self):
        if self.__dynamics:
            print("HP laptops have dynamics.")
        else:
            print("HP laptops don't have dynamics.")


ports = ['USB', 'HDMI', 'VGA']
hp = HPLaptop("15.6", "us", True, False, ports, True)
hp.screen()
hp.keyboard()
hp.touchpad()
hp.webcam()
hp.ports()
hp.dynamics()

# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.


print("\nTask 5. \n")


class Car(ABC):
    def drive(self):
        print("Driving.")

    def stop(self):
        print("Stopping.")

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError


class ford(Car):
    def open_door(self):
        print("Door open.")

    def close_door(self):
        print("Door closed.")

    def turn_on_light(self):
        print("Lights on.")

    def turn_off_light(self):
        print("Lights off.")

    def enable_radio(self):
        print("Radio on.")

    def disable_radio(self):
        print("Radio off.")


f = ford()
f.drive()
f.stop()
f.open_door()
f.close_door()
f.turn_on_light()
f.turn_off_light()
f.enable_radio()
f.disable_radio()
