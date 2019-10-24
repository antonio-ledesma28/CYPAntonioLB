PRI = 0
SEG = 1
for I in range(3,181,1):
    SIG = PRI + SEG
    PRI = SEG
    SEG = SIG
print("SIG es", SIG)
