# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a + b

def find_maximum(a, b, c):
    lst = list(a,b,c)
    return(max(lst))

def is_palindrome(string):
    if string[::-1] == string:    
        return True

def count_word_occurrences(text, word):
    count = 0
    for x in text:
        if word in x:
            count += 1
    return count

def read_file_lines(filepath):
    pass

def factorial(n):
    pass

def is_prime(n):
    pass

def sort_numbers(numbers):
    pass

def factorial(n):
    pass

def fibonacci(n):
    pass

def tower_of_hanoi(n, source, auxiliary, target):
    
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    pass

class Person:
    def __init__(self, name, age):
        pass


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g