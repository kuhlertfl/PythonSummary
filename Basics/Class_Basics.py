# Python Classes and Object-Oriented Programming (OOP) Detailed Data Sheet

# =============================================================================
# Basic Class Definition
# =============================================================================

# Defining a class named Person with a constructor (__init__) and a method (say_hello).
# - __init__: Initializes the attribute 'name' when a new object is created.
# - say_hello: Prints a greeting using the attribute 'name'.
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hello, {self.name}!")

# Creating an instance of the class Person and calling its say_hello method.
# The __init__ method is called automatically when a new object is created.
person1 = Person("Alice")
person1.say_hello()  # Output: "Hello, Alice!"

# -----------------------------------------------------------------------------

# =============================================================================
# Inheritance
# =============================================================================

# The Student class inherits from the Person class.
# - __init__: Initializes attributes 'name' and 'subject' for a Student object.
# - say_hello: Overrides the say_hello method to include the 'subject' attribute.
class Student(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the parent class constructor to set the 'name' attribute
        self.subject = subject  # Initializing the 'subject' attribute
    
    def say_hello(self):
        print(f"Hello, {self.name}! You are studying {self.subject}.")

# Creating an instance of the Student class and calling its say_hello method.
# The say_hello method in the Student class overrides the one in the Person class.
student1 = Student("Bob", "Math")
student1.say_hello()  # Output: "Hello, Bob! You are studying Math."

# -----------------------------------------------------------------------------

# =============================================================================
# Encapsulation
# =============================================================================

# Defining a class named BankAccount with private attributes.
# - __init__: Initializes a private attribute '__balance'.
# - deposit: Adds amount to the balance.
# - withdraw: Subtracts amount from the balance if sufficient.
# - get_balance: Returns the current balance.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Initializing private attribute '__balance'

    def deposit(self, amount):
        self.__balance += amount  # Adding to the private attribute '__balance'

    def withdraw(self, amount):
        if amount <= self.__balance:  # Checking if enough balance exists
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance  # Returning the value of private attribute '__balance'

# Creating an instance of the BankAccount class and using its methods.
# The deposit and withdraw methods manipulate the private attribute '__balance'.
account1 = BankAccount(100)
account1.deposit(50)  # Deposits $50
print(account1.get_balance())  # Output: 150 (100 original balance + 50 deposit)

# -----------------------------------------------------------------------------

# =============================================================================
# Polymorphism
# =============================================================================

# Defining classes Dog and Cat both with a method named sound.
# - sound: Returns the sound the animal makes.
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# A function to demonstrate polymorphism.
# Takes an animal object and prints its sound.
def animal_sound(animal):
    print(animal.sound())

# Creating instances of Dog and Cat classes and calling the animal_sound function.
# The function works for both classes, demonstrating polymorphism.
dog1 = Dog()
cat1 = Cat()
animal_sound(dog1)  # Output: "Woof!"
animal_sound(cat1)  # Output: "Meow!"

# -----------------------------------------------------------------------------

# =============================================================================
# Special Methods
# =============================================================================

# Defining a class named ComplexNumber with special methods for various operations.
# - __str__: For the string representation.
# - __add__: For addition using '+'.
# - __len__: For the 'length' (magnitude) of the complex number using len() function.
# - __eq__: For equality check using '=='.
# - __lt__: For less-than comparison using '<'.
# =============================================================================
# Special Methods (Magic Methods, Dunder Methods)
# =============================================================================

# Extended ComplexNumber class with additional special methods
# - __sub__: For subtraction using '-'.
# - __mul__: For multiplication using '*'.
# - __truediv__: For division using '/'.
# - __floordiv__: For floor division using '//'.
# - __mod__: For modulo operation using '%'.
# - __abs__: For the absolute value using abs() function.
# - __pow__: For power using '**'.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.imag * other.real + self.real * other.imag
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real_part, imag_part)

    def __floordiv__(self, other):
        result = self.__truediv__(other)
        return ComplexNumber(int(result.real), int(result.imag))

    def __mod__(self, other):
        # For simplicity, let's define it as the remainder of the division of their magnitudes
        len_self = self.__abs__()
        len_other = other.__abs__()
        return len_self % len_other

    def __abs__(self):
        import math
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __pow__(self, power):
        import cmath
        result = cmath.polar(complex(self.real, self.imag))
        r, theta = result[0] ** power, result[1] * power
        return ComplexNumber(r * cmath.cos(theta), r * cmath.sin(theta))

# Test cases to demonstrate additional special methods
num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 4)
num3 = ComplexNumber(2, 0)

# __sub__ example
print("Subtraction:", num1 - num2)

# __mul__ example
print("Multiplication:", num1 * num2)

# __truediv__ example
print("Division:", num1 / num2)

# __floordiv__ example
print("Floor Division:", num1 // num2)

# __mod__ example
print("Modulo:", num1 % num3)

# __abs__ example
print("Absolute Value:", abs(num1))

# __pow__ example
print("Power:", num1 ** 2)

# =============================================================================
# Object Initialization
# =============================================================================
class MyClass:
    def __init__(self):
        print("MyClass instance created.")

    def __del__(self):
        print("MyClass instance destroyed.")


# =============================================================================
# String Representation
# =============================================================================
class Represent:
    def __str__(self):
        return "This is the __str__ method."

    def __repr__(self):
        return "This is the __repr__ method."


# =============================================================================
# Arithmetic Operations
# =============================================================================
class Arithmetic:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __floordiv__(self, other):
        return self.value // other.value

    def __mod__(self, other):
        return self.value % other.value

    def __pow__(self, power):
        return self.value ** power


# =============================================================================
# Comparison Operations
# =============================================================================
class Comparison:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


# =============================================================================
# Container Operations
# =============================================================================
class Container:
    def __init__(self, my_list):
        self.my_list = my_list

    def __len__(self):
        return len(self.my_list)

    def __getitem__(self, index):
        return self.my_list[index]

    def __setitem__(self, index, value):
        self.my_list[index] = value

    def __delitem__(self, index):
        del self.my_list[index]

    def __contains__(self, item):
        return item in self.my_list

    def __iter__(self):
        return iter(self.my_list)


# =============================================================================
# Context Managers
# =============================================================================
class ContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


# =============================================================================
# Other Common Special Methods
# =============================================================================
class OtherSpecialMethods:
    def __call__(self, *args, **kwargs):
        print("Instance is called")

    def __hash__(self):
        return id(self)


# =============================================================================
# Test Cases to Demonstrate Special Methods
# =============================================================================
# Object Initialization
my_class = MyClass()
del my_class

# String Representation
r = Represent()
print(str(r))
print(repr(r))

# Arithmetic Operations
a = Arithmetic(5)
b = Arithmetic(2)
print(a + b)

# Comparison Operations
c1 = Comparison(10)
c2 = Comparison(20)
print(c1 < c2)

# Container Operations
container = Container([1, 2, 3])
print(len(container))
print(2 in container)

# Context Managers
with ContextManager():
    print("Inside the context")

# Other Special Methods
other = OtherSpecialMethods()
other()
print(hash(other))
