from bubble_sort import bubble_sort

def test_bubble_sort_with_small_list():

#     #Arrange
    list_input=[1,5.2,-2,89,3]

#     #Act
    result= bubble_sort(list_input)

#     #Assert
    assert result == [-2, 1, 3, 5.2, 89]

def test_bubble_sort_with_big_list_100_elements():

#Arrange
    big_list_input=[-45.6, 78, -12.34, 0.5, 23.1, -99, 54, -0.75, 18.9, -4, 65.8, -23, 0, 12.56, -89, 
    34, 7.77, -10, 43, -56.8, 91, -3.14, 29.5, 66, -21.9, 0.001, -1, 99.99, 45, -88.2, -67, 9.8, 
    5.5, -4.2, 82, 17.6, -7, -25, 3.3, -30.9, 8, -18, 27.7, -2.8, 100, 15.4, -32, 60, -11.5, 4.04, 
    9.99, -20, 49, -91.4, 0.22, 11, -76, 84.6, 32.5, -50, 7, -9.99, 31, -46, 6.7, 21.3, -40, 
    19, 50.5, -15.6, 72, 3.14, -33, 88, -1.5, 70.2, -60, 25, -2, 44.4, 90, -12, 1.11, 38, 
    -81, 10.5, -3, 5, -14, 63.3, 22, -37, 41.9, -77, 16, 98.8, -26, 30, -49.9]

#Act
    result_2=bubble_sort(big_list_input)

#Assert
    assert result_2 == [-99, -91.4, -89, -88.2, -81, -77, -76, -67, -60, -56.8, -50, 
                    -49.9, -46, -45.6, -40, -37, -33, -32, -30.9, -26, -25, -23, 
                    -21.9, -20, -18, -15.6, -14, -12.34, -12, -11.5, -10, -9.99, 
                    -7, -4.2, -4, -3.14, -3, -2.8, -2, -1.5, -1, -0.75, 0, 0.001, 0.22, 
                    0.5, 1.11, 3.14, 3.3, 4.04, 5, 5.5, 6.7, 7, 7.77, 8, 9.8, 9.99, 10.5,
                    11, 12.56, 15.4, 16, 17.6, 18.9, 19, 21.3, 22, 23.1, 25, 27.7, 29.5, 30, 31, 32.5, 34, 
                    38, 41.9, 43, 44.4, 45, 49, 50.5, 54, 60, 
                    63.3, 65.8, 66, 70.2, 72, 78, 82, 84.6, 88, 90, 91, 98.8, 99.99, 100]

def test_bubble_sort_with_an_empty_list():


# #Arrange
    empty_list_input=[]

# #Act
    result_3=bubble_sort(empty_list_input)

# #Assert
    assert result_3 == []

def test_bubble_sort_with_non_list_parameters():


#Arrange
    non_list= {"name": "Patrick", "age": 34, "number": 78363947 }

#Act
    result_4=bubble_sort(non_list)

#Assert
    assert result_4
