from unit_test_for_week_6 import upper_and_lower
import pytest

def test_return_mixed_upper_and_lower_letters():
    #Arrange
    sentence= "This is a new line of Code. Hello USER"

    #Act
    case_1= upper_and_lower(sentence)

    #Assert
    assert case_1 == (7, 22)


#---------------------------------------------------------------

def test_return_upper_and_lower_only_with_upper_letters():
    #Arrange
    upper_sentence= "I AM TYPING ONLY UPPER LETTERS"

    #Act
    case_2= upper_and_lower(upper_sentence)

    #Assert
    assert case_2 == (25, 0)

#---------------------------------------------------------------

def test_return_upper_and_lower_with_different_type_of_writings_and_characters():
    #Arrange
    special_sentence= "I AM TYPING letters, in language ´Русский´. I hAvE 4 @s."

    #Act
    case_3= upper_and_lower(special_sentence)

    #Assert
    assert case_3 == (13, 26)