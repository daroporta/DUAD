from unit_test_for_week_6 import sum_of_list
import pytest
import math

def test_sum_list_of_mixed_numbers():
#Arrange
    numbers= [23,-85,78,45.7,90.3567,math.pi]

#Act
    case_1= sum_of_list(numbers)

#Assert
    assert case_1 == 155.1982926535898 

#---------------------------------------------------------------

def test_sum_empty_list():
#Arrange
    numbers= []

#Act
    case_2= sum_of_list(numbers)

#Assert
    assert case_2 == 0

#---------------------------------------------------------------

def test_sum_list_of_strings():
#Arrange
    numbers= ["pineapple", "apple", "carrot", "bleacher", "pork meat", "rice", "cookies"]

#Act #Assert
    with pytest.raises(TypeError):
        sum_of_list(numbers)

