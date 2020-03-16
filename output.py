import datetime
nowtime=datetime.datetime.now()
nowm=nowtime.month
nowd=nowtime.day
namecoll=[]
print(nowtime,nowm,nowd)
print("Reading...")
with open("finalcollect.txt","r") as fileobj:
    namelist=fileobj.readlines()
print("Working...")
for every in namelist:
    perline=every.split()
    name=perline[0]
    print(name)
    them=str(perline[1])[4:6]
    them=int(them)
    print(them)
    thed=str(perline[1])[6:8]
    thed=int(thed)
    print(thed)
    if them==nowm:
        if thed==nowd:
            print(name)
            namecoll.append(name)
print("================================")
print(namecoll)