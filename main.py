import random
from collections import Counter
from math import sqrt
import numpy as np

def rastgele():
    min_value=float(input("Alt sınır nedir ? "))
    max_value=float(input("Üst sınır nedir ? "))
    

    rang=int(input("Kaç değer üretilecek ?"))

    rand_list=[]

    for _ in range(rang):
        if (max_value-min_value)==1:
            while len(rand_list)!=rang:
                r=random.uniform(min_value,max_value)
                if r not in rand_list:
                    rand_list.append(r)

        elif ((max_value-min_value)+1 >= rang):
            while len(rand_list)!=rang:
                r=random.randint(min_value,max_value)
                if r not in rand_list:
                    rand_list.append(r)
        else:
            r=random.randint(min_value,max_value)
            rand_list.append(r)
            
    print(rand_list)

def sistematikRandom():
    N=int(input("Lütfen N tamsayı değerini giriniz :"))
    n=int(input("Lütfen n tamsayı değerini giriniz :"))
    k=int(N/n)
    print("\nK değeri : ",k)
    r=random.randint(0,k)
    print("Üretilen rastgele sayı : ",r)

    listofnumber=[]
    listofnumber.append(r)

    for _ in range(n-1):
        new_r=r+k
        r=new_r
        listofnumber.append(new_r)

    print(listofnumber)

def sırala():
    a=int(input("Kaç tane veri gireceksiniz? : "))
    
    value_list=[]
    for _ in range(a):
        value=int(input("Değeri giriniz : "))
        value_list.append(value)
    
    value_list=sorted(value_list)
    
    print(value_list)

global warning
warning="Veri girişini sonlandırmak için -1 tuşlayınız."

def frekansSerisi():
    print(warning)
    
    frekansSeri=[]
    
    while True:   
        value=str(input("Veri giriniz : "))
        if value=='-1':
            break
        else:
            frekansSeri.append(value)
    testListDict = {}

    for item in frekansSeri:
        try:
            testListDict[item] += 1
        except:
            testListDict[item] = 1
    print(testListDict)
    
##frekans tablosu 

def frekansTable():
    print(warning)
    frekansTablosu=[]
    while True:   
        value=int(input("Veri giriniz : "))
        if value==-1:
            break
        else:
            frekansTablosu.append(value)
    frekansTablosu=sorted(frekansTablosu)
    n=len(frekansTablosu)
    L=max(frekansTablosu)
    S=min(frekansTablosu)
    R=L-S
    k=int(sqrt(n))
    K=sqrt(n)
    if K!=k:
        k=k+1

    h=int(R/k)
    H=R/k
    if H!=h:
        h=h+1

    altSınır=[]
    ustSınır=[]

    altSınır.append(S)
    for i in range(1,k):
        added=altSınır[i-1]+h
        altSınır.append(added)

    ustSınır.append(altSınır[1]-1)
    for i in range(1,k):
        added=ustSınır[i-1]+h
        ustSınır.append(added)
    
    #sınıf sınırı 
    degişenDeger=(altSınır[1]+ustSınır[0])/2
    chAltSınır=[]
    chUstSınır=[]

    firstValue=degişenDeger-h
    chAltSınır.append(firstValue)
    for i in range(1,k):
        added2=chAltSınır[i-1]+h
        chAltSınır.append(added2)
    chUstSınır.append(degişenDeger)
    for i in range(1,k):
        added2=chUstSınır[i-1]+h
        chUstSınır.append(added2)

##sınıf frekans
    
    freq=[]
    for j in range(0,k):
        freq.append(0)

    for i in frekansTablosu:
        for j in range(0,k):
            if i<=chUstSınır[j] and i>=chAltSınır[j]:
                freq[j]+=1
##sınıf orta noktası
    mid_point=(altSınır[0]+ustSınır[0])/2

##eklenik frekans
    eklenikFreq=[]
    for j in range(0,k):
        eklenikFreq.append(0)
    
    eklenikFreq[0]=freq[0]
    for i in range(1,k):
        eklenikFreq[i]=freq[i]+eklenikFreq[i-1]

##oransal freq
    oransalFreq=[]
    for j in range(0,k):
        oransalFreq.append(0)
    
    for i in range(0,k):
        oransalFreq[i]=freq[i]/n

##eklenik oransal
    eklenikOransalFreq=[]
    for j in range(0,k):
        eklenikOransalFreq.append(0)
    for i in range(0,k):
        eklenikOransalFreq[i]=eklenikFreq[i]/n    

    ##yazdırma
    print("\nSınıf Alt Sınır :",altSınır,"\nSınıf Üst Sınır : ",ustSınır)
    print("\nSınıf Alt Limit : ",chAltSınır,"\nSınıf Üst Limit : ",chUstSınır)
    print("\nFrekans Değerleri : ",freq)
    print("\nSınıf Orta Noktası : ",mid_point)
    print("\nEklenik Frekans : ",eklenikFreq,"\nOransal Frekans : ",oransalFreq,"\nEklenik Oransal Frekans :",eklenikOransalFreq)

def merkeziEgilim():

    warning="Veri girişini sonlandırmak için -1 tuşlayınız."
    print(warning)
    listofvalue=[]
    
    while True:   
        value=int(input("Veri giriniz : "))
        if value==-1:
            break
        else:
            listofvalue.append(value)

    rang=len(listofvalue)
    
    toplam=sum(listofvalue)

    aritmat=f"\nAritmetik deger : {toplam/rang}"
    print(aritmat)

    listofvalue.sort()
    if(rang%2==1):
        medyan_deger=int(rang/2)
        
        result=f"Medyan değeri : {(listofvalue[medyan_deger-1])}"
        print(result)

    else:
        medyan_deger=int(rang/2)
        result=f"Medyan değeri : {(((listofvalue[medyan_deger-1]+listofvalue[(medyan_deger)])/2))}"
        print(result)   
        
    c = Counter(listofvalue)
    mod_value=f"Mod değeri : {[k for k, v in c.items() if v == c.most_common(1)[0][1]]}"
    print(mod_value)
    

def aritmetik(listofvalue):
    rang=len(listofvalue)
    toplam=sum(listofvalue)
    aritmetik_deger=toplam/rang
    return aritmetik_deger

def median(median_numbers):
    #return np.median(median_numbers) # will work if numpy import is allowed
    middle = len(median_numbers) // 2  # floor division
    if (len(median_numbers) % 2 == 0):  # even or odd
        return (median_numbers[middle-1] + median_numbers[middle]) / 2
    else:
        return median_numbers[middle]

def dagılımOlculeri():
    sd = 0.0 # standart sapma
    aratop=0
    sonuc=0
    
    print(warning)
    listofvalue=[]
    
    while True:   
        value=float(input("Veri giriniz : "))
        if value==-1:
            break
        else:
            listofvalue.append(value)

    for num in range(1,len(listofvalue)+1):
        aratop2=listofvalue[num-1]
        aratop=aratop+((aratop2-aritmetik(listofvalue))**2) 
    aratop=aratop/(len(listofvalue)-1)                
 
    sonuc=sqrt(aratop)
    
    ##değişim katsayısı

    dk=(sonuc/aritmetik(listofvalue))*100
    print("\nDeğişim Katsayısı : ","%",dk)
    
    ##ortalama sapma bölümü
    
    listoffvalue2=[]
    for item in listofvalue:
        deger=item-aritmetik(listofvalue)
        if deger<0:
            deger=aritmetik(listofvalue)-item
            listoffvalue2.append(deger)
        else:
            listoffvalue2.append(deger)
    
    total=sum(listoffvalue2)/len(listofvalue)
    print("Ortalama Mutlak Sapma : ",total)

    ##find the q1 and q3
    """
    q1=np.quantile(listofvalue, .25)
    q3=np.quantile(listofvalue, .75)
    """
    
    mid=len(listofvalue) //2
    if (len(listofvalue) % 2 == 0):    # even or not
        Q1 = median(listofvalue[:mid])
        Q3 = median(listofvalue[mid:])
    else:
        # if odd set of numbers
        Q1 = median(listofvalue[:mid])
        Q3 = median(listofvalue[mid+1:])
    print("Q1 Değeri : ",Q1,"\nQ3 Değeri : ",Q3)

    return sonuc

def varyans(ass):
    return ass*ass


def factorial(f):
    result = 1 
    if f < 0: 
        print ("Negatif sayılar için faktöriyel bulunmaz.")
    elif f == 0: 
        print ("O ın faktöriyel 1 dir.")
    else:
        for i in range(1,f + 1): 
            result = result*i 
    return result


def permKomb():
    n=int(input("Lütfen n değerini giriniz :"))
    r=int(input("Lütfen r değerini giriniz :"))
    resultp = 0
    if (r>n):
        resultp = resultp
    else:
        resultp = f"Permütasyon sonucu: {factorial(n)/factorial(n-r)}" 
    
    print(resultp)

    if (n<r):
        print("1. Sayının 2. Sayıdan büyük ya da eşit olması gerekli. Verdiğiniz sayıların çözümü yoktur!")
   
    elif(n==r):
        print("1")
    
    elif(n>r):
        
        s=1
        s= factorial(n) #n faktöriyel
        
        l=1
        l= factorial(r) #m faktöriyel
        
        f=1
        f= factorial(n-r) #n-m faktöriyel
        
        w=f"Kombinasyon değeri: {s/(l*f)}"
        print(w)
    


def main(seçilen):
    
    if seçilen=='1':
        rastgele()
    elif seçilen=='2':
        sistematikRandom()
    elif seçilen=='3':
        sırala()
    elif seçilen=='4':
        frekansSerisi()
    elif seçilen=='5':
        frekansTable()
    elif seçilen=='6':
        merkeziEgilim()
    elif seçilen=='7':

        s_deger=dagılımOlculeri()
        v_deger=varyans(s_deger)
        print("Standart Sapma : ", s_deger, "\nVaryans Degeri : ", v_deger)
        
    elif seçilen=='8':
        permKomb()
    else:
        print("Hatalı giriş tuşladınız, lütfen tekrar deneyiniz.")

print("""
        1-Rastgele Sayı Oluşturma
        2-Rastgele Örnekleme
        3-Basit Seri
        4-Frekans Serisi
        5-Frekans Tablosu
        6-Merkezi Eğilim Ölçüleri(Aritmetik Ortalama, Mod, Medyan)
        7-Dağılım Ölçüleri(Varyans, Standart Sapma, OMS, Q1, Q3, Değişim Katsayısı)
        8-Permütasyon ve Kombinasyon

        DİKKAT: Programı sonlandırmak için yapılacak işlem bölümüne -1 tuşlayınız.
        DİKKAT: Ondalıklı sayı girişlerini nokta araclığı ile gerçekleştiriniz bkz: '1.2'
    """)

def tekrarSecim():
    
    while True:
        seçilen=input("\nYapılacak işlemi seçiniz : ")
        if seçilen=='-1':
            print("Görüşmek üzere..")
            break
        elif seçilen==False:
            print("Görüşmek üzere..")
            break
        else:
            main(seçilen)

tekrarSecim()


