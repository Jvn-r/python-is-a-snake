#to make a functional journal 
from datetime import datetime

print("WHelcome to The jpurNal")

with open("Journal.txt", 'a') as file:
    close = False

while(close == False):
    print("-------Menu-------")
    print("1.Write")
    print("2.read")
    print("3.Close")
    choice = int(input("Enter your choice: "))    

    if choice == 1:
        print("Enter what you want to Write")
        with open("Journal.txt",'a') as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = input()

            file.write(f"\n[{timestamp}]--\n{entry}")
            file.write("\n------- Journal -------\n")
            
    elif choice == 2:
        print("Journal contents:")
        with open("Journal.txt",'r') as file:
            content = file.read()
            print(content)
    elif choice == 3:
        print("Closing")
        close = True
        file.close()
    else :
        print("Invalid Choice")


    