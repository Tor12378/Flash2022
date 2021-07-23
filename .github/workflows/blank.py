#простое 1 
kol=0
max_all=0
for x in range(15121,31001):
    if x%12==0 and x %14==0 and x%17!=0 and x%5!=0:
        kol+=1
        max_all=max(max_all,x)
print(max_all,kol)

#простое 2 
kol=0
min_all=100000000
for x in range(9999,28001):
    if x %4==2 and x %5==1 and x%10!=8 :
        kol+=1
        min_all=min(min_all,x)
print(kol,min_all)

# среднее 1 
def spisok_2(x1):
    kol1=0
    kol2=0
    for number in [17,19,29]:
        if x1%number==0:
            kol1=1
    for number in [31,37,41]:
        if x1 % number == 0:
            kol2 = 1
    if (kol1==1 and kol2==0) or (kol2==1 and kol1==0):
        return True
    else:
        return False

summ_numbers=0

kol=0
for x in range(6900,30001):
    if spisok_2(x):
        kol+=1
        summ_numbers+=x
print(summ_numbers//kol,kol)


#среднее 2
def spisok_2(x1):
    kol=0

    for number in [17,19,29,31]:
        if x1%number==0:
            kol+=1
    if kol==2:
        return True
    else:
        return False


kol=0
min_all=100000
for x in range(10000,36001):
    if x % 3==0 and x%7!=0 and x %2!=0 and spisok_2(x):
        kol+=1
        min_all=min(min_all,x)

print(kol,min_all)

#слолжное 1 
def sum_del(x):
    x1 = str(x)
    sum_del = int(x1[::2])
    del_numbers=0
    while sum_del>0:
        del_numbers+= sum_del%10
        sum_del=sum_del//10
    return del_numbers
kol=0
max_number=0
for i in range(11000,45001):
    p = sum_del(i)
    if i % p==0:
        kol+=1
        max_number=max(max_number,i)
print(kol,max_number)

#сложное 2 

def sum_del(x):
    del1=0
    del2=0
    while x>0:
        if (x%10)%2!=0:
            del1+= x%10
        else:
            del2+=x%10
        x=x//10
    return max(del1,del2)
kol=0
min_number=10000000
for i in range(24560,46790):
    p = sum_del(i)
    if i % p==0 and i%3==0 and i%17!=0:
        kol+=1
        min_number=min(min_number,i)

print(kol,min_number)
# дополнительное
kol=0
for x in range(729,16807):
    if x %7!=0 and x %11!=0 and x %13!=0 and x %17==0 and x %19==0 and x %23==0 and x%2==0:
        kol+=1
        print(x)
