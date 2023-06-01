student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
num = 0

for x in student_heights:
    total += x
    num += 1

avg = round(total / num)
# avg = round(sum(student_heights)/len(student_heights))
print(avg)