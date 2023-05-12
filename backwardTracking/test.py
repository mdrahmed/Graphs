#hbw = open('hbw.data','r')
hbw = open('../hbw-graph.txt','r')
i = 0
for line in hbw:
  if "Topicfrom" in line:
    print(line)
    i += 1
