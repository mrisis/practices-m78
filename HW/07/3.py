import pickle
from operator import itemgetter
class User :
    def __init__(self,id,first_name,last_name,phone):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone

    def __repr__(self):
        return f"{self.id}:{self.first_name} {self.last_name} {self.phone}"
    def fullName(self):
        return f"{self.name} {self.last_name}"

infile=open("users.pickled","rb")
new=pickle.load(infile)

infile.close()
new=list(map(str,new))
new_dict={}
for i in new :
    k,v=i.split(":")
    new_dict[int(k)]=v

result=sorted(new_dict.items(),key=itemgetter(0))

with open("output-q-3-1.txt","w") as f:
    print(result,file=f)









