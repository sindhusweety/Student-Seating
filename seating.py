def SeatingStudents(arr):
  if len(arr) >1:
    list1= [ i for i in range(1,arr[0]+1)]
    nested  =[]
    for i in list1:
      if len(nested) !=0:
        if i %2!=0:
          nested.append([i])
        else:
          nested[len(nested)-1].append(i)
      else:
        nested.append([i])
    odd_list_seq= [ i  for i in range(1,arr[0]+1) if((i)% 2) !=0]
    odd_repetition_list=[i for i in zip(odd_list_seq[0:-1],odd_list_seq[1:])]
    
    even_list_seq = [ i  for i in range(1,arr[0]+1) if((i)% 2) ==0]
    even_repetition_list=[i for i in zip(even_list_seq[0:-1],even_list_seq[1:])]
    
    nested.extend(odd_repetition_list)
    nested.extend(even_repetition_list)
    
    result = [] 
    for i in nested:
      if i[0] in arr[1:] or i[1] in arr[1:]:
        pass
      else:
        result.append(i)
    return len(result)
    

      
  else:
    total_non_rep = arr[0]//2
    odd_rep = total_non_rep - 1
    even_rep = total_non_rep - 1
    return total_non_rep+odd_rep+even_rep 
  
  

# keep this function call here 
print(SeatingStudents(input()))
