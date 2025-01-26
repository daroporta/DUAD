from unit_test_for_week_6 import get_prime
import pytest

def test_get_prime_numbers_of_a_long_list():
    #Arrange
    list_of_numbers= [ number for number in range(0, 99)]

    #Act
    case_1= get_prime(list_of_numbers)

    #Assert
    assert case_1 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


#------------------------------------------------------------------

def test_get_prime_numbers_of_a_negative_list():
    #Arrange
    list_of_negative_numbers= [ number for number in range(-99, 0)]

    #Act
    case_2= get_prime(list_of_negative_numbers)

    #Assert
    assert case_2 == []               # pytest test_prime_numbers.py -vv to get more details of the test


#------------------------------------------------------------------

def test_get_prime_of_composite_list():
    #Arrange
    list_of_composite_numbers= [number for number in range(0, 99) if number % 2 == 0]  

    #Act
    case_3= get_prime(list_of_composite_numbers)

    #Assert
    assert case_3 == [2]  #from composite list, 2 is the only prime
