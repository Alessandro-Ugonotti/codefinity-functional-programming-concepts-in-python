global_var = 10

def modify_global():
    global global_var
    global_var += 5
    return(global_var)

print("Modified global variable:", modify_global())
