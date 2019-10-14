#%%
def fact(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
    else:
        return n * fact(n - 1)

fact(-10)
#%%


#%%
