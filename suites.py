import time

s1 = lambda n: sum([i for i in range(1,n+1)])
s2 = lambda n: sum([i**2 for i in range(1,n+1)])
s5 = lambda n: sum([i**5 for i in range(1,n+1)])

n = int(input())

d1 = time.time()
o1=s1(n)
e1 = time.time()
print("\nS1 =", o1, "\nRuning time:", e1-d1,"s")

d2 = time.time()
o2=s2(n)
e2 = time.time()
print("\nS2 =", o2, "\nRuning time:", e2-d2,"s")

d5 = time.time()
o5=s5(n)
e5 = time.time()
print("\nS5 =", o5, "\nRuning time:", e5-d5,"s")
