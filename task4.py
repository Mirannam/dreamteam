uniq = []
seen =set()
sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
for x in sequence_0 :
	if x not in seen:
	uniq.append(x)
	seen.add(x)
