import e32
import telephone

f=open('e:\\QDial.txt','r')
number = f.readline().decode('utf-8')
telephone.dial(number)

