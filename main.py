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
    if attribute in all:
        all.index
    print("Cannot find this attribute!")

def file_print(file):
    with open(file,encoding="utf8") as f:
        print()
        print(f.read())

def namespace_change(file):
    attribute = input("Enter attribute you want to change")


file = "file.txt"

def main():
    file = "file.txt"
    while True:
        print("Choose an option:")
        print("1. Add Person")
        print("2. Find by Attribute")
        print("3. Print File Info")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_name_space(file)
        elif choice == "2":
            attribute = input("Enter attribute you want to find: ")
            find_by(file, attribute)
        elif choice == "3":
            file_print(file)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()