# Python Access to the Online Encylopedia of Integer Sequences

This module uses requests to access the OEIS, and then parses a minimal
subset of the information contained there. 

If you want to search for the 5 best matches for the sequence [1,2,3,4,5],
you could do something like:

>>> import oeis
>>> sequences = oeis.query([1, 2, 3, 4, 5], 5)
>>> for seq in sequences:
>>>    print seq.id
>>>    print seq.name
>>>    print seq.formula
>>>    print seq.sequence
>>>    print seq.comments

I'm happy to add a bigger subset of the OEIS format if anyone is interested
