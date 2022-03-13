# Read file
with open("clean_data.csv") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

# Count total real students
total_students = []

for i in range(len(students)):
	students[i] = students[i].split(",")
	if len(students[i]) > 2:
		total_students.append(students[i])

	# print(len(total_students))
	# print(total_students[0])

header = header.split(",")
subjects = header[5:]


# Filter numbers of students (Not taking exam & Having 10 points), in each subject
not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]
	# points_10 = [0,0,0,0,0,0,0,0,0,0,0]

for student in total_students:
	for i in range(5,16):
		if student[i] == "-1":
			not_take_exam[i-5] += 1
		# if student[i] == "10.00":
		# 	points_10[i-5] += 1

print(not_take_exam)
	# print(points_10)

# Calculate percentage over total_students
not_take_exam_percent = [0,0,0,0,0,0,0,0,0,0,0]
	# points_10_percent = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,11):
	not_take_exam_percent[i] = round(not_take_exam[i]*100/len(total_students), 2)
	# points_10_percent[i] = round(points_10[i]*100/len(total_students), 2) 

	# print(not_take_exam_percent)
	# print(points_10_percent)


# PLOT BARCHART

import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()

y_pos = np.arange(len(subjects))

plt.bar(y_pos, not_take_exam_percent, align='center', alpha=0.5)
plt.xticks(y_pos, subjects)

# Set limit to Oy axis
axis.set_ylim(0,100)

plt.ylabel('Phần trăm')
plt.title('Số học sinh không thi mỗi môn')

# Make some labels.
rects = axis.patches

for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

plt.show()

# 10 cases of numbers of exams each student took (except for KHTN & KHXH)
exams_num = [0,0,0,0,0,0,0,0,0,0]

for s in total_students:
	count = 0
	for i in range(11):
		if s[i+5] != "-1":
			count += 1
	# Remove 1 subject: KHTN / KHXH
	for i in range(2):
		if s[i+8] != "-1":	
			count = count - 1

	exams_num[count] += 1

	# Print special students
	# if count == 1:
	# 	print(s)


print(exams_num)
print(sum(exams_num))
print(len(total_students))


# PLOT PIE CHART, where the slices will be ordered and plotted counter-clockwise:

labels = '0 môn', '1 môn','2 môn','3 môn','4 môn','5 môn','6 môn', '7 môn','8 môn','9 môn'
sizes = exams_num
# explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()









