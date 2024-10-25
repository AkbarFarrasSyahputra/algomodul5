p = 0 #seluruh nilai
v = 0 #total nilai

while True:
    Nilai = input("Input: ")
    Nilai = Nilai.upper()
    if Nilai =='A':
        print ('A = 4.00')
        p = p + 4.00
        v = v + 1
    elif Nilai == 'B+' :
        print('B+ = 3.75')
        p = p + 3.75
        v = v + 1
    elif Nilai == 'B' :
        print ('B = 3.00')
        p = p + 3.00
        v = v + 1
    elif Nilai == 'B-' :
        print ('B- = 2.75')
        p =  p + 2.75
        v = v + 1
    elif Nilai == 'C+'  :
        print ('C + 2.50')
        p = p + 2.50
        v = v + 1
    elif Nilai == 'C' : 
        print ('C = 2.00')
        p = p + 2.00
        v = v + 1
    elif Nilai == 'C-' :
        print ('C- = 1.75')
        p = p + 1.75
        v = v + 1
    elif Nilai == 'D' :
        print ('D= 1.50')
        p = p + 1.50
        v = v + 1
    elif Nilai == 'E' : 
        print ('E = 1.25')
        p = p + 1.25
        v = v + 1
    else :
        print("selamat")
        rata_rata = p / v #seluruh nilai / jumlah nilai
        print(f"Rata-rata nilai adalah: {rata_rata}")
        break

