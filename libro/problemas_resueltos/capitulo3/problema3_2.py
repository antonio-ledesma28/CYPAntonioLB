BAND = True
SUMSER = 0
I = 2
while (I<= 1800):
    SUMSER += 1
    print (I)
    if BAND == True:
        BAND = False
        I += 3
    else:
        BAND =True
        I += 2
print(f"SUMSER {SUMSER}")
