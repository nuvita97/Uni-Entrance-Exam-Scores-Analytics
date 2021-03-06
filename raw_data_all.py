import html
import csv

file = open("raw_data_DLLT.txt", "r")

datas = file.read().split("\n")								# READLINE: only read first	line

with open("clean_data.csv", "w") as file_csv:				# Create CSV file
	
	header = ["SBD", "Họ và Tên", "DD", "MM", "YY", "Toán", "Ngữ văn", "Tiếng Anh", "KHTN", "KHXH", "Vật lí", "Hóa học", "Sinh học", "Lịch sử", "Địa lí", "GDCD"]
	writer = csv.writer(file_csv)
	writer.writerow(header)


sbd = 2000000

for data in datas:

	try:										# TRY - EXCEPT: identify no info cases

		# Add sbd
		sbd += 1
		sbd_str = "0" + str(sbd)

		# SPLIT: change to a list

		data = data.split("\\n")						

		# Remove \r & \t

		for i in range(len(data)):					
			data[i] = data[i].replace("\\r", "")
			data[i] = data[i].replace("\\t", "")

		# Remove <tag>

		for i in range(len(data)):

			tags = []

			for j in range(len(data[i])):	
				if	data[i][j] == "<":
					begin = j
				if	data[i][j] == ">":
					end = j
					tags.append(data[i][begin:end+1])
			
			for tag in tags: 
			 	data[i] = data[i].replace(tag,"")

		# Remove white space & empty lines

		unempty_lines = []

		for i in range(len(data)):

			data[i] = data[i].strip()

			if data[i] != "":
				unempty_lines.append(data[i])

		data = unempty_lines

		# Choose information

		name = data[7]
		dob = data[8]
		scores = data [9]

		# Decode special characters (Unicode utf8)

		chars = []
		codes = []

		code_file = open("unicode.txt","r")
			
		code_data = code_file.read().split("\n")
			
		for code in code_data:
			x = code.split(" ")
			chars.append(x[0])
			codes.append(x[1])

		for i in range(len(chars)):
			name = name.replace(codes[i], chars[i])
			scores = scores.replace(codes[i], chars[i])

		# Decode special characters in name & scores (chr á - unescape ') 

		for i in range(len(name)):
			if name[i:i+2] == "&#" :
				# name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]
				name = html.unescape(name)


		for i in range(len(scores)):
			if scores[i:i+2] == "&#" :
				scores = scores[:i] + chr(int(scores[i+2:i+5])) + scores[i+6:]

		# Adjust name; Split dob

		name = name.title()

		dob_list = dob.split("/")
		dd = str(dob_list[0])
		mm = str(dob_list[1])
		yy = str(dob_list[2])

		# Process scores

		scores = scores.replace(":", "")
		scores = scores.replace("KHXH ", "KHXH   ")
		scores = scores.replace("KHTN ", "KHTN   ")
		scores = scores.replace("  10", "   10")

		scores_list = scores.split("   ")

		data = [sbd_str, name, dd, mm, yy]


		# Add scores to data respectively

		for subject in ["Toán", "Ngữ văn", "Tiếng Anh", "KHTN", "KHXH", "Vật lí", "Hóa học", "Sinh học", "Lịch sử", "Địa lí", "GDCD"]:
			if subject in scores_list:
				index_subject = scores_list.index(subject)
				data.append(scores_list[index_subject + 1])
			else:
				data.append("-1")


		# Write to file (text or CSV)

		# file = open("test2.txt", "a")
		# for i in range(len(data)):
		# 	file.write(data[i] + ",")
		# file.write("\n")

		with open("clean_data.csv", "a") as file_csv:
			writer = csv.writer(file_csv)
			writer.writerow(data)

	except:

		# file = open("test2.txt", "a")
		# data = sbd_str
		# file.write(data + "\n")

		with open("clean_data.csv", "a") as file_csv:
			data = [sbd_str]
			writer = csv.writer(file_csv)
			writer.writerow(data)





# # Test Print

# for i in range(len(data)):
# 	print(data[i])™



# tags = []

# for i in range(len(s)):	
# 	if s[i] == "<":
# 		begin = i
# 	if s[i] == ">":
# 		end = i
# 		tags.append(s[begin:end+1])
	
# for tag in tags: 
# 	s = s.replace(tag,"")

# print(tags)
# print(s)






