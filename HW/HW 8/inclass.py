def my_sum(n):
    #build base case
    if n == 0:
        return
    else:
        return n + my_sum(n-1)
    
def main():