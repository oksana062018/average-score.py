grades = [[2,4,3,5,3], [5,5,5,3,3,4], [4,4,3,4,5,2], [3,5,5,5,4,5]]
students = {'Maria', 'Artem', 'Nikolai', 'Sofia'}

grades_n = (sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]))
students_sort = sorted(students)

dict1 = dict(zip(students_sort, grades_n))
print(dict1)
