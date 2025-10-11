from task2 import process_borrowers
from task3 import calculate_average_books
from task4 import count_overdue
def main():
    while True:
        filename = input("Enter the name of the file: ")
        try:
            with open(filename,"r") as f:
                break
        except FileNotFoundError:
            continue
    current_date = "2025-10-04"
    print(process_borrowers(filename,current_date),"\n")
    print(calculate_average_books(filename),"\n")
    print(count_overdue(filename,current_date))

if __name__ == "__main__":
    main()