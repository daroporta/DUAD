from unit_test_for_week_6 import order_words
import pytest


def test_order_words_with_lower_and_upper_case():
    #Arrange
    upper_and_lower_words= "Python-python-variable-function-Future-computer-Laptop-monitor-MOney"

    #Act
    case_1= order_words(upper_and_lower_words)

    #Assert
    assert case_1 == "Future-Laptop-MOney-Python-computer-function-monitor-python-variable"

#------------------------------------------------------------------

def test_order_words_with_numbers():
    #Arrange
    words_with_numbers= "Apple-carrots-25bananas-1car-2People-0cereals-13bags"

    #Act
    case_2= order_words(words_with_numbers)

    #Assert
    assert case_2 == "0cereals-13bags-1car-25bananas-2People-Apple-carrots"  #first numbers, then  Upper, then Lower case


#------------------------------------------------------------------

def test_order_words_with_special_characters():
    #Arrange
    words_with_characters= "Generation-@sterisk- -/*/-P@sword-*******-n1c3-7om@7o-#umber-+ore"

    #Act
    case_3= order_words(words_with_characters)

    #Assert
    assert case_3 == " -#umber-*******-+ore-/*/-7om@7o-@sterisk-Generation-P@sword-n1c3" 

