x = (input('Masukkan Detik: '))

def process(a):
    hh = a // 3600
    mm = a % 3600 // 60
    ss = a % 3600 % 60 // 1
    hh1 = hh
    mm1 = mm
    ss1 = ss
    if hh < 10:
        hh1 = '0'+str(hh)
        if mm < 10:
            mm1 = '0'+str(mm)
            if ss <10:
                ss1 = '0'+str(ss)
    print(hh1+':'+mm1+':'+ss1)
  
try:
    if type(eval(x)) == float:
        print(" Invalid Input!")
    elif type(eval(x)) == int:
        xx = int(x)
        if xx >359999 or xx <0:
            print(" Invalid Input!")
        else:
            process(xx)    
    elif type(eval(x)) == bool:
        print(" Invalid Input!")      
except:
    print(" Invalid Input!")
