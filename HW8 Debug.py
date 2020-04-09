"""
Authors: Hank Lefkowicz, Jackson Sherrard
Last edit: 07/04/2020
 
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
        # This if statement is important because it gave me no end of grief. It protects agianst data being formatted with spaces
        # in between places. This way, it condenses the data so you don't have to worry about empty sublists.
                if element != ['']:
                    list_holder.append(element)
            
            return list_holder
    # Start of the error handling cascade
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

def matrix_create(list_holder):
    # Error handling support
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
Gives the length of the row had the matrix been transposed. It's a super small function, I know, but it helps me make sense
of all that's going on. Also, it supports error handling. 

"""

def matrix_transpose(matrix):
    
    # Error handling support
    if matrix == 0:
        return 0

    return len(matrix)

    """

Okay, so my matrix multiplication math is kinda weird, mostly because I threw out the idea of transposing the
matrix. The way I see it, when you transpose a matrix, you multiply the row of the non transposed one by the column of the
transposed one. However, because a transpostion is essesntially just turning the matrix sideways, the same effect can be achieved
with by just creating two loops, simmilar to the way that you would try to calculate all of the possible passwords of something.
It takes the first row of the matrix and multiplies it by all of the other rows in the matrix. Each row's values are put in their
own sublist, so that the matrix multiplication for each row has it's own list for easy summation. Then it moves on to
the second row of the matrix and does the same thing, so on and so forth until it's done all the math. 


"""

def dot_product(matrix_create, t_matrix):
   
    # Error handling support
    if matrix_create == 0:
        return 0
    # dot and dot_prod are placeholders to hold the ith -1 matrix multiplcation value (dot) and the current row's matrix
    # multiplication value up to that point (dot_prod).
    # dot_prod is appended to dot_prod_matrix when that row is finished. 
    dot = []
    dot_prod = []
    dot_prod_matrix = []
 
    # This creates a copy of the matrix so you can have two. 
    matrix_create_copy = matrix_create * 1

    for i in matrix_create:
        for j in matrix_create_copy:
            for x in range(len(matrix_create[0])):
                # dot_math holds the current value, which is then appended onto dot
                dot_math = (i[x] * j[x])
                dot.append(dot_math)
                # if the length of dot is equal to the length of the first sublist in the master matrix, you've reached the end
                # the current vector multiplcation cycle, and so you add them all up to get the number that will go in the
                # final matrix, and that's appended to dot_prod, and the next row is up. 
                if len(dot) == len(matrix_create[0]):
                    dot_prod.append(sum(dot))
                    # if the length of dot_prod is equal to the t_matrix, the length of the row had the matrix been transposed,
                    # then you're done with the ith row, and you can move onto the i + 1th row, so the row of vector calculations
                    # is appended to the master matrix and then the placeholder lists are cleared. 
                    if len(dot_prod) == t_matrix:
                        dot_prod_matrix.append(dot_prod)
                        dot_prod = []
                        
                    dot = []
    
    return dot_prod_matrix 


"""

This does the final conneciton analysis, adding up all of the rows in the multiplied matrix to find the largest,
then using the index of that row (plus one b/c dict's start at one for whatever reason), to find the person that row
originally belonged to using the index that was made at the very beginning. 

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
    most_connected = dictionary[ most_connected_index + 1]
    
    return most_connected

def main():
    
    file = 'testdata.txt'
    # This creates the dictonary
    dictionary = dict_create((fileio(file)))
    # This holds the unmultiplied matrix
    matrix_create_val = matrix_create((fileio(file)))
    # This returns the multipled matrix when given the original matrix
    dot_prod_matrix_val = dot_product(matrix_create_val,matrix_transpose(matrix_create_val))
    # This does the final connection analysis
    print(connection_analysis(dot_prod_matrix_val, dictionary))

if __name__ == '__main__':
    main()


