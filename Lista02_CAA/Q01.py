def decompor(S, p, r, piv):
    q1 = p - 1
    q2 = r + 1
    i = p
    
    while i < q2:
        if S[i] < piv:
            q1 += 1
            S[q1], S[i] = S[i], S[q1]
            i += 1
        elif S[i] == piv:
            i += 1
        else:
            q2 -= 1
            S[q2], S[i] = S[i], S[q2]
    
    return q1, q2

S = [4, 2, 7, 1, 9, 5, 3]
p = 1
r = len(S) - 1
piv = 4

q1, q2 = decompor(S, p, r, piv)
print("q1:", q1)
print("q2:", q2)
print("Vetor rearrumado:", S)