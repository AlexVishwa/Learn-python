setA={'Cricket','Football','Badminton','Tennis','Golf'}
setB={'Chess','Checkers','Carrom'}

setC=setA.union(setB)
print(setC)

setD=setA.intersection(setB)
print(setD)

setE=setA.difference(setD)
print(setE)

print(setA.isdisjoint(setB))

print(setA.symmetric_difference(setB))