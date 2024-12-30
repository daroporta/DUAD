from unit_test_for_week_6 import return_string
import pytest

def test_reversed_long_string():
    #Arrange
    string="The list of items for christmas is 4 toppers, 1 Christmas Tree, and 2 set of baubles"

    #Act
    case_1= return_string(string)

    #Assert
    assert case_1 == 's e l b u a b   f o   t e s   2   d n a   , e e r T   s a m t s i r h C   1   , s r e p p o t   4   s i   s a m t s i r h c   r o f   s m e t i   f o   t s i l   e h T'

#--------------------------------------------------------------

def test_reversed_string_with_special_characters():
    #Arrange
    special_characters="!#$&/()=@"

    #Act
    case_2=return_string(special_characters)


    #Assert
    assert case_2 == "@ = ) ( / & $ # !"

#--------------------------------------------------------------

def test_reversed_with_different_data_types():
    #Arrange
    dictionary= {"name":"John",
                "age":33, 
                "ID":123456}

    #Act & Assert
    with pytest.raises(KeyError):
        return_string(dictionary)




