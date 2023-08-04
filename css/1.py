penduduk = 1
for hari in range(50):
    if hari == 0:
         pass
     elif (hari+1) % 3 == 0:
         if penduduk % 2 == 1:
             penduduk = (penduduk-1)/2
         else:
             penduduk = penduduk / 2
     else:
         penduduk = penduduk * 3
print(int(penduduk))