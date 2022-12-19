

# Developed: 19/12/2022
# This program is my take on a function that permutates through a given list of items without repetitions and outputs a list of all the possible n-size combinations
# of those items. It's approximately 46 times slower than the itertools.permutations function so its not very well optimized but regardless designing this script was a 
# very fun puzzle to solve.


#imports 
import itertools
import copy 
import time 



items = range(5) #random list of items,can be any list 
n = 3 # size of 1 permutation (the program gets wonky around size 1) 
 
print("My Implementation:")

def myPermutationImplementation(list_of_items,n_of_permutators): # main function 
 master_output_list = []
 


 reserved_indexes = []
 new_list = []
 recur_lvl = [0]
 def iterator():
   for i in range(len(list_of_items)):
    if recur_lvl[0] != n_of_permutators - 2:
     if i not in reserved_indexes:
      new_list.append(list_of_items[i])
      reserved_indexes.append(i)
      recur_lvl[0] += 1
      iterator()
     
     
    else:
     #print("Bottom of Recursion!",i)
     if i not in reserved_indexes:
      new_list.append(list_of_items[i])
      reserved_indexes.append(i)

      for j in range(0,len(list_of_items)):
       if j not in reserved_indexes:
        new_list.append(list_of_items[j])
        master_output_list.append(copy.deepcopy(new_list))
        new_list.pop()
      
      new_list.pop()
      reserved_indexes.pop()

 
   recur_lvl[0] -= 1 
   try:
    new_list.pop()
    reserved_indexes.pop()
   except IndexError:
    pass 
   

 
 
 iterator()
 return master_output_list
  
  
  
  
 
  
  
 
start_time = time.time()
perm_iter = myPermutationImplementation(items,n)
#print("--- %s seconds ---" % (time.time() - start_time))
input()
start_time = time.time()
perm_mine = list(itertools.permutations(items,n))
#print("--- %s seconds ---" % (time.time() - start_time))
for i in range(0,len(perm_iter)-1):
 print(perm_iter[i],perm_mine[i])
input()
