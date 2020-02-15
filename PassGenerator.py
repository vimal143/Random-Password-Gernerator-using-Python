# Random password gernerator
import string
import  random
content=string.ascii_letters+string.digits
password=''
len=int(input('Enter the length of Password'))
for i in range(1,len):
    get=random.choice(content)
    password=password+get
spcl='@#$%&*'
password=password+random.choice(spcl)
password=list(password)
random.shuffle(password)
actual_password= (''.join(password))
print(actual_password)
