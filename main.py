def add_name_space(file):
    info = []
    space = ["Имя ", "Фамилия ", "Отчество ", "Номер "]
    for i in range(4):
        info.append(input(space[i]) + " ")
    with open(file,"a", encoding="utf8") as f:
        f.write("\n")
        for i in range(4):
            f.write(info[i])

def find_by(file, attribute):
    all = []
    with open(file, "r", encoding="utf8") as f:
        all = f.readlines()

    for i, elem in enumerate(all):
            if attribute in elem:
                index = i
                print(elem)
                return index
    print("Cannot find this attribute!")

def file_print(file):
    with open(file,encoding="utf8") as f:
        print()
        print(f.read())

def namespace_change(file):
    file_print(file)

    attribute = input("Enter attribute you want to change ")
    index = find_by(file, attribute)

    if index == None:
        print("Wrong attribute!!!")
        return

    with open(file, "r", encoding="utf8") as f:
        all_lines = f.readlines()

    print("Enter new Имя Фамилия Отчество Номер ")
    new = input()
    all_lines[index] = new + "\n"

    with open(file, "w", encoding="utf8") as f:
        f.writelines(all_lines)

    file_print(file)

def remove_line(file):
    file_print(file)

    attribute = input("Enter attribute you want to remove ")
    index = find_by(file, attribute)

    if index == None:
        print("Wrong attribute!!!")
        return

    with open(file, "r", encoding="utf8") as f:
        all_lines = f.readlines()

    del all_lines[index]

    with open(file, "w", encoding="utf8") as f:
        f.writelines(all_lines)

    file_print(file)  



file = "file.txt"

def main():
    file = "file.txt"
    while True:
        print()
        print("Choose an option:")
        print("1. Add Person")
        print("2. Find by Attribute")
        print("3. Print File Info")
        print("4. Change Line Info")
        print("5. Remove Line Info")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_name_space(file)
        elif choice == "2":
            attribute = input("Enter attribute you want to find: ")
            find_by(file, attribute)
        elif choice == "3":
            file_print(file)
        elif choice == "4":
            namespace_change(file)
        elif choice == "5":
            remove_line(file)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
