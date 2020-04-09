
def naive_transposition():
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
    # Aaaaaaaand I was right. I didn't. But this is also the naive approach to transposing a matrix made of a nested list
    # and I'll be damned if I have to make it agian when I did't need to. 