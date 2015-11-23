f = open("input.txt","r")
g = open("output.txt","w")

line = f.readline()

while line:
	line = line.strip()
	line = line.split()
	g.write(line[0]+"\n")	
	line = f.readline()

f.close()
g.close()
