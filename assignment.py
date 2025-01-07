t = ['a', 'b', 'c', 'd', 'e', 'f']
reversed_list = t[::-1]
print(reversed_list)

t = ['a', 'b', 'c', 'd', 'e', 'f']
slice_1 = t[1:4]  # ['b', 'c', 'd']
print(slice_1)

# Taking input for marks in three subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

# Calculating the average
average = (subject1 + subject2 + subject3) / 3

# Determining the grade based on the average
if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:4])
print(t[:3])
print(t[2:])
print(t[1:5:2])
print(t[::2])
print(t[::-1])
print(t[2:6])
print(t[-3:])