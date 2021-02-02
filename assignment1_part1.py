def listDivide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    return len([n for n in numbers if n % divide == 0])


class ListDivideException(Exception):
    """"
    Indicates exception that was caused by the listDivide function
    """


def testListDivide():
    """
    Test listDivide
    """
    try:
        assert listDivide([1, 2, 3, 4, 5]) == 2
        assert listDivide([2, 4, 6, 8, 10]) == 5
        assert listDivide([30, 54, 63, 98, 100], divide=10) == 2
        assert listDivide([]) == 0
        assert listDivide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError:
        raise ListDivideException


if __name__ == "__main__":
    testListDivide()
