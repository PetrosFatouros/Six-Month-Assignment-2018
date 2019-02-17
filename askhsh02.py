#ASKHSH 2

number=input("Give the number.-->")

#apo8hkeuei tous paragontes sth lista "factors"
i = 2
factors = []
while i * i <= number:
    if number % i:
        i += 1
    else:
        number //= i
        factors.append(i)
if number > 1:
    factors.append(number)

#emfanizei tous paragontes sthn o8onh me ton tropo ths ekfwnhshs
counters=[]
clean=[]
k=0
previous=factors[0]
clean.append(previous)
for item in factors:
    if item==previous:
        k=k+1
    else:
        counters.append(k)
        clean.append(item)
        k=1
    previous=item
counters.append(k)
result=""
x=len(clean)
for j in range(x):
    if counters[j]==1:
        result=result+"("+str(clean[j])+")"
    else:
        result=result+"("+str(clean[j])+"**"+str(counters[j])+")"
print result
