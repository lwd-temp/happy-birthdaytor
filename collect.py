with open("name.txt","r") as nametxt:
    names=nametxt.readlines()
with open("id.txt","r") as idtxt:
    ids=idtxt.readlines()
count=len(names)
for i in range(0,count+1):
    with open("finalcollect.txt","a") as coll:
        birth=str(ids[i]).rstrip()
        birth=birth[6:14]
        collstr=str(names[i]).rstrip()+" "+birth+"\n"
        coll.write(collstr)
