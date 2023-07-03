#hbw = open('hbw.data','r')
hbw = open('../hbw-graph2.txt','r')
i = 0
for line in hbw:
  if "Calling:" in line and "Function:" in line:
    #print(line)
    i += 1
print("total: ",i)
