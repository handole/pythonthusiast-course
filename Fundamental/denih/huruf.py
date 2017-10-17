def hitunghuruf(nama):
  huruf={}
  for h in nama:
    if huruf.get(h):
      huruf[h] += 1
    else:
      huruf[h] = 1

  return huruf


print(hitunghuruf('mejikuhibiniu'))
