def bubble_sort(list):
    for amount_run in range(len(list)):
        Sorted=True
        for current_position in range(len(list)-amount_run-1):
            if list[current_position] > list[current_position+1]:
                list[current_position], list[ current_position+1]=list[current_position+1], list[current_position]
                Sorted= False
        if Sorted:
            break
    
    return list




