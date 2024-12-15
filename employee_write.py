# Basic Level Printing Employee List by Python
employee_list = []
employee_how = int(input("Kac adet personelin ismini yazacaksin: "))
sinir = 1

while employee_how >= sinir:
    employee_name = input("Personel ad: ")
    employee_list.append(employee_name)
    file = open("/home/astatin/employee_list.txt","w")
    for employee in employee_list:
        file.write(employee)
        file.write("\n")
    file.close()
    employee_how -= 1

file = open("/home/astatin/employee_list.txt","r")
list_word = file.read()
print(list_word)
