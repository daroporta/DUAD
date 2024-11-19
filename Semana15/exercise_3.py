#Analysis using Big O notation

def bubble_sort(list):   # O(1)
    for amount_run in range(len(list)):    # O(N)
        Sorted=True                        # O(1)
        for current_position in range(len(list)-amount_run-1):  # O(n^2)
            if list[current_position] > list[current_position+1]:   # O(1)
                list[current_position], list[ current_position+1]=list[current_position+1], list[current_position]   # O(1)
                Sorted= False   # O(1)
        if Sorted:   # O(1)
            break    # O(1)
    return list      # O(1)

list=[2,5,6,8,2,9,11,-78,23.6, 3, 12.5]   # O(1)
print(bubble_sort(list))                  # O(1)

#BIG O NOTATION WORST SCENARIO  O(n^2)
#Best scenario  O(1)