PRI = 0
SEG = 1
I = 3
for I in range(1,181,I+3):
    SIG = PRI + SEG
    PRI = SEG
    SEG = SIG
print("SIG es", SIG)
