"""

Authors: Hank Lefkowicz, Jackson Sherrard
Last edit: 05/04/2020
Will to live: Gone. 


"""

    
"""

This block reads in the file and splits the file up by the newline delimiter. Each element in the list is then something like
''name', '1', '2', '3'', which is way too much string, so it then runs through the thing and splits up each element (the large
nested string) by commas and appends those elemends to another list. Those number will have to be turned into integers
eventually, but right now we still need the strings to make a dictionary (more on that in the next function) so it just returns
the list.

It also has error handling, so if you input a file name that doesn't exist/is mispelled, it returns 0 to start the error cascade.


"""

def fileio(file):
    
    list_holder = []
    
    try:
        with open(file,'r') as f:
            file = f.read()
            file = file.split('\n')
            for element in file:
                element = element.split(',')
                list_holder.append(element)
            
            return list_holder
        
    except:
        return 0

   
"""
This function takes the list and takes the names of the individuals and puts them in a dictionary, because we're getting rid
of any non-integer data later, because we can't do math with it. However, we'll need those names later when we've finished the
calculation, so they're stored. 
"""

def dict_create(list_holder):
   
    # Error handling cascade returns zero if the file name is wrong.  
    if list_holder == 0:
        return 0
   
    # Creates an dict in case we need those values for the names later, but for right now, they need to get gone because they
    # make the dot producting hard and stupid. 
    names_dict = {i:list_holder[i][0] for i in range(1, len(list_holder))}
        
    return names_dict 


"""

This function removes all of the names and converts the rest of the elements into integers. 

"""

# split lists up into matrix

def matrix_create(list_holder):
    
    if list_holder == 0:
        return 0
    
    # Removes the names and labels of all for transposing. The for loop removes the names, the delete statement removes the
    # whole first row, because you don't need it for the calculation, or even for the later analysis (I think).
    for row in list_holder:
        del(row[0])
    del list_holder[0]
    
    # Turns all of the strings into integers, so we can finally, finally, do some matrix multipling. 
    for row in list_holder:
        for element in range(len(row)):
            row[element] = int(row[element])
    
    matrix = list_holder
    return matrix 

"""
Transposes Matrix

"""

def matrix_transpose(list_holder):
    
    # HA! Just kidding. We have to transpose a copy of the matrix we just made. 
    temp = []
    t_matrix = []
    for i in range(len(list_holder[0])):
        for line in list_holder:
            temp.append(line[i])
            if len(temp) == len(list_holder):
                t_matrix.append(temp)
                temp = []
                
    return t_matrix
    # I'm almost 1000% percent sure I didn't need to do this. 

"""


"""

def dot_product(matrix_create, t_matrix):
    # Okay, NOW we can do some matrix math
    
    if matrix_create == 0:
        return 0
    
    dot = []
    dot_prod = []
    dot_prod_matrix = []
 
    matrix_create_copy = matrix_create

    for i in range(len(matrix_create)-1):
        for j in range(len(matrix_create_copy)-1):
            for x in range(len(matrix_create[0])):
#                print(matrix_create[i][x],'X', matrix_create_copy[j][x])
                dot_math = (matrix_create[i][x] * matrix_create_copy[j][x])
                dot.append(dot_math)
                if len(dot) == len(matrix_create[0]):
                    dot_prod.append(sum(dot))
                    if len(dot_prod) == t_matrix:
                        dot_prod_matrix.append(dot_prod)
                        dot_prod = []
                    dot = []
    print(dot_prod_matrix)
    
    
    dot = []
    dot_prod = []
    dot_prod_matrix = []
    
    print(matrix_create)
    print(matrix_create.pop())
    print(matrix_create)
    
    for i in matrix_create:
        for j in matrix_create_copy:
            for x in range(len(matrix_create[0])):
#                print(matrix_create[i][x],'X', matrix_create_copy[j][x])
                dot_math = (i[x] * j[x])
                dot.append(dot_math)
                if len(dot) == len(matrix_create[0]):
                    dot_prod.append(sum(dot))
                    if len(dot_prod) == t_matrix:
                        dot_prod_matrix.append(dot_prod)
                        dot_prod = []
                    dot = []

    return dot_prod_matrix 

## adds up all the rows to find most connected

"""



"""

def connection_analysis(dot_prod_matrix, dictionary):
    
    if dot_prod_matrix == 0:
        return 0
    
    if dictionary == 0:
        return 0
    
    connected = []
    
    for i in dot_prod_matrix:
        connected.append(sum(i))
                   
    most_connected_val = max(connected)
    most_connected_index = connected.index(most_connected_val)
    most_connected = dictionary[ most_connected_index +1 ]
    
    return most_connected

"""



"""
def main():
    
    dictionary = dict_create((fileio('testdata.txt')))
    matrix_create_val = matrix_create((fileio('testdata.txt')))
    #matrix_transpose_val =  matrix_transpose(matrix_create((fileio('revolutionaries.txt'))))
    matrix_transpose_val = len(matrix_create_val)
    
    dot_prod_matrix_val = dot_product(matrix_create_val,matrix_transpose_val)
    print()
    print("Most connected is: ",connection_analysis(dot_prod_matrix_val, dictionary))

if __name__ == '__main__':
    main()

