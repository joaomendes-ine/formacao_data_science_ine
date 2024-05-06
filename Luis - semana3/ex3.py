def um_to_n(n):
    if n == 1:
        return '1'
    else:
        return um_to_n(n - 1) + ' ' + str(n)
    
    
um_to_n(5)