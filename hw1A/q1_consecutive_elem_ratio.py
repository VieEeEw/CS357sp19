def consecutive_elem_ratio(seq):
    for i in reversed(range(1,len(seq))):
        seq[i] = seq[i]/seq[i-1]
    del seq[0]
fibonnaci_seq = [1, 1, 2, 3, 5, 8, 13, 21]
consecutive_elem_ratio(fibonnaci_seq)
print(fibonnaci_seq)