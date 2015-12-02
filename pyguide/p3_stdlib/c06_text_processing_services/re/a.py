import random 

p = list()
for i in range(12):
    p.append(random.randint(1000, 1500))
total = sum(p)
p = [i * 1.0 / total for i in p]

max_p = max(p)
ind = p.index(max_p)

r = 0.1
res = r * max_p / (1.0 / 12)
print(res)