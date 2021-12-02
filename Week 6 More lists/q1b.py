def merge_list(list1, list2):
    
    if len(list1) > len(list2):
        merge_list = []
        for i in range(len(list2)):
            merge_list.append(list1[i])
            merge_list.append(list2[i])
        
        merge_list += list1[len(list2):]

    if len(list1) < len(list2):
        merge_list = []
        for i in range(len(list1)):
            merge_list.append(list1[i])
            merge_list.append(list2[i])
    
        merge_list += list2[len(list1):]

    return merge_list

    
print(merge_list([1, 3, 10, 15, 4, 7, 12], [9, 5, 2])) 
print(merge_list([9, 5, 2], [1, 3, 10, 15, 4, 7, 12] )) 