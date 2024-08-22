#calculating a fixed income investment with Python
#formule : m=c(1+i)**n
#m= value c= initial capital n= time (month) i=rate
c = int(input("write the investment initial:"))
i = int(input("write the interest rate:"))
n = int(input("write the time (in the month):"))

j = i/100             
a= (1+j)**n           
b= c*a
l= b *0.1448


print(f'value liquid: {b:.2f}')
print(f'value of govern receive(tax): {l:.2f}')

