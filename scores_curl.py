import subprocess

start = 2000001
end = 2074719

file = open("raw_data.txt", "w")

for sbd in range(start,end):
	command = 'curl -F "SoBaoDanh=0' + str(sbd) + '" diemthi.hcm.edu.vn/Home/Show'
	result = subprocess.check_output(command, shell=True)
	file.write(str(result) + "\n")



# 	file.write(str(result))

# for i in range(10):
# 	file.write(str(i+1) + "\n")

