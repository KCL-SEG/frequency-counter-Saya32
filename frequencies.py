"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    #traverse over the items
    for i in items: 
        i=str(i)
        if i in frequencies.keys(): #increment the value if it's present in dictionary
            frequencies[i]+=1
        else:
            frequencies[i]=1 #otherwise, assign the key
    return frequencies
