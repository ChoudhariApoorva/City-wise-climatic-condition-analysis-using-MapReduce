from random import *

def gen_data(input_file):
	f_in = open(input_file,"r")
	
	city_list = []

	line = f_in.readline()
	
	while(line):
		line = line.strip() #trim white spaces on both ends
		line = line.split() #split based on space
		if(line):
			city_list.append((line[0]).lower())
		
		line = f_in.readline()

	f_in.close()

	return city_list

def write_to_file(city_list,f_out,c_range,appendingChar):
	
	for city in city_list:
		val = str(round(randrange(c_range[0],c_range[1]) + random() , 2))
		f_out.write(city+"\t"+val+appendingChar+"\n")


def generate_climate_param(city_list,c_param,c_range,output_file):
	f_out = open(output_file,"a")


	if(c_param == "temperature"):
		appendingChar = 'T'
	elif(c_param == "pressure"):
		appendingChar = 'P'
	elif(c_param == "wind"):
		appendingChar = 'W'
	elif(c_param == "humidity"):
		appendingChar = 'H'
	elif(c_param == "rainfall"):
		appendingChar = 'R'
	elif(c_param == "visibility"):
		appendingChar = 'V'

	write_to_file(city_list,f_out,c_range,appendingChar)
	f_out.close()



city_list = gen_data("bigdata_input.txt")	

output_file_list = ["January 1.txt","January 2.txt","January 3.txt","January 4.txt","January 5.txt","January 6.txt","January 7.txt","January 8.txt","January 9.txt","January 10.txt"]

for output_file in output_file_list:
	generate_climate_param(city_list,"temperature",(10,40),output_file) #degree celsius
	generate_climate_param(city_list,"pressure",(980,1050),output_file) #millibars
	generate_climate_param(city_list,"wind",(100,350),output_file) #kmph
	generate_climate_param(city_list,"humidity",(20,85),output_file) #percentage
	generate_climate_param(city_list,"rainfall",(500,12000),output_file) #mm
	generate_climate_param(city_list,"visibility",(1,15),output_file) #kms

