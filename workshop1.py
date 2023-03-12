students = ["Hakan"]

# student ekleme
nameSoy = input("Adınızı ve Soyadınızı giriniz: ")
students.append(nameSoy)
 
# student silme
students.pop(3)
print(students)

#birden fazla student ekleme
students.extend(nameSoy)
print(students)

# tek tek ekrana yazdırma
for i in range(len(students)):
    print(students[i])

# İndex öğrenme
print(students.index("Hakan"))