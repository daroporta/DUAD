def sum_of_list(list_of_numbers):
    sum_of_numbers=0
    for num in list_of_numbers:
        sum_of_numbers= sum_of_numbers + num
    return sum_of_numbers                       #updated it, if the function returns a print, it will give you 
                                                # an assertion none result.



#-------------------------------------------------------------------

def return_string(word):
    space= " "
    for letter in range(-1, -len(word) -1, -1):
        space=space+word[letter]+" "
    return space.strip()


#-------------------------------------------------------------------

def upper_and_lower(your_string):
    upper_letter= 0
    lower_letter=0
    space=0
    for letter in your_string:
        if letter.isupper():
            upper_letter += 1
        elif letter.islower():
            lower_letter += 1
        else:
            space +=1
    return upper_letter, lower_letter




#-------------------------------------------------------------------

def order_words(list_of_words):
    words_split=list_of_words.split("-")
    words_split.sort()
    words_with_dash= "-".join(words_split)
    return words_with_dash


#-------------------------------------------------------------------

# def add_numbers(list_of_numbers):           #part of code that does nt really work for the test
#     # amount_of_numbers=int(input("How many numbers would you like to add to the list?: "))
#     # amount_number=1 

#     # while amount_number <= amount_of_numbers: 
#     #     numbers=int(input("Please type an integer number: "))
#     #     list_of_numbers.append(numbers)
#     #     amount_number += 1 

#     return list_of_numbers 


def get_prime(list_of_numbers):             
    prime_numbers=[]
    for number in list_of_numbers:  
        cont= 0 
        for each_number in range (1, number + 1): 
            if number % each_number==0: 
                cont+=1  

        if cont==2: 
            prime_numbers.append(number)

    return prime_numbers 


# list_of_numbers = []          #part of code that does nt really work for the test, for pytest it works better with returns than prints
# prime_numbers = []

# add_numbers() 
# print(get_prime())
