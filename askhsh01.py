#ASKHSH 1

def sumIntervals(list):
    print list
    record=[]
    final=[]
    for sublist in list:
        record.append(range(sublist[0],sublist[1]))
    for subrecord in record:
        for item in subrecord:
            final.append(item)
    final.sort()
    counter=-1
    previous=final[0]
    for number in final:
        if number==previous:
            counter=counter+1
        previous=number
    print "result:",len(final)-counter

#Akolouthei paradeigma listas
sumIntervals([[1,5],[10,20],[1,6],[16,19],[5,11]])
