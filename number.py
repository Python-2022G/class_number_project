class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.get_number() % 2 != 0

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return not self.is_odd()

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        if self.get_number() < 2: return False

        for i in range(self.get_number()):  
            if self.get_number() % i == 0: return False
        
        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        l = []
        for i in range(1, self.get_number() + 1):
            if self.get_number() % 2 == 0: l.append(i)

        return l

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.get_number()))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        return sum(self.get_digits())

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.get_number())[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return str(self.get_number()) == str(self.get_number())[::-1]

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        l = []
        for i in str(self.get_number()):
            l.append(int(i))

        return l

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(self.get_digits())

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(self.get_digits())

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return self.get_sum() / self.get_length()

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return [self.get_min(), self.get_max()]
    

# Create a new instance of Number
number = Number(34235423)

print(number.get_number())
print(number.is_odd())
print(number.is_even())
print(number.is_prime())
print(number.get_divisors())
print(number.get_length())
print(number.get_sum())
print(number.get_reverse())
print(number.is_palindrome())
print(number.get_digits())
print(number.get_max())
print(number.get_min())
print(number.get_average())
print(number.get_range())
