x= int(input())
sumos = 0 #SUM Of Sequence

for i in range(x+1):
  if (i%3) == 0:
    sumos = sumos + i
    print("3-"+str(i))

  if (i%5) == 0:
    sumos = sumos + i
    print("5-"+str(i))

  if (i%3) == 0 and (i%5) == 0:
    sumos = sumos - i

print(sumos)
