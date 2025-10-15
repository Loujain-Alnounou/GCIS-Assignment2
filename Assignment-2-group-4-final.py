"""
Assignment 2 Group 4
Yashovardhan Patil, ID: 425002732

Mohammed Yassin, 

Loujain Alnounou, 433000002
"""



def calculate_fine(books, due_date, current_date):
    """ Calculates the library fine for overdue books based on the number of books
    and the difference between the due date and the current date.

    Parameters:
        books (str or int): The number of borrowed books.
        due_date (str): The due date in "YYYY-MM-DD" format.
        current_date (str): The current date in "YYYY-MM-DD" format.

    Returns:
        integer: The calculated fine amount if dates and input are valid.
        string: An error message if an invalid date format or value is detected."""
    try:
        if int(books) < 0:
            return 0

        if due_date[4]!="-" or due_date[7]!="-" or current_date[4]!="-" or current_date[7]!="-":
            return "Error: Invalid date"

        current_split = current_date.split("-")
        due_split = due_date.split("-")

        for i in range(3):
            due_split[i] = int(due_split[i])
            current_split[i] = int(current_split[i])
        
        if 1>due_split[1]>12 or 1>current_split[1]>12 or 1>due_split[2]>31 or 1>current_split[2]>31:
            return "Error: Invalid date"
        
        for i in range(3):
            if current_split[i]<due_split[i]:
                return 0
            if current_split[i]>due_split[i]:
                days_late = (current_split[0]-due_split[0])*365+(current_split[1]-due_split[1])*30+(current_split[2]-due_split[2])
                fine = days_late*int(books)*2
                return fine
        else:
            return 0
    except (ValueError,IndexError) as e:
        return "Error: "+{e}


def process_borrowers(filename,current_date):
    '''Reads borrower data from a CSV file and calculates fines for overdue books
    using the `calculate_fine` function.
    Parameters:
        filename (str): The name of the CSV file containing borrower data.
        current_date (str): The current date in "YYYY-MM-DD"
        
        Returns: str: A record string listing the borrowers and their fine or dues status.'''

    try:
        borrowers =  open(filename, 'r')
        borrowers.seek(0)
        borrowers.readline()
        ledger = ""
        fine = 0

        for record in borrowers:
            record = record.strip()
            parts = record.split(",")
            try:
                if int(parts[1])>=0 and parts[2][4]==parts[2][7]=="-":
                    fine = calculate_fine(int(parts[1]),parts[2],current_date)
                    fine = int(fine)
                    if fine > 0:
                        ledger += f"{parts[0]}: Fine: ${fine}\n"
                    else:
                        ledger += f"{parts[0]}: No dues\n"

            except Exception as e:
                ledger += f"Error reading line: {e}+\n"

    except FileNotFoundError:
        print("Error: File " + filename + " not found.")
    finally:
        borrowers.close()
        return ledger


def calculate_average_books(filename):
    """
    To calculate the average number of books borrowed.
    
    Args:
        filename: Path to the file containing book borrowing data
    
    Returns:
        the average numbers of books borrowed. 
    """
    try:
        borrowers = open(filename, 'r')
        
        total_books = 0
        valid_count = 0
        borrowers.readline()

        try:
            for line in borrowers:
                line = line.strip()
                parts = line.split(',')
                if len(parts) == 3 and int(parts[1])>=0 and len(parts[2])==10 and parts[2][4]==parts[2][7]=="-":
                        books = int(parts[1].strip())

                        total_books += books
                        valid_count += 1
            total_books/valid_count
        except (ValueError,ZeroDivisionError, IndexError) as e:
            print("Error: " + e)
            
    except FileNotFoundError:
        print("Error: File " + filename + " not found.")
    except Exception as e:
        print("Error: " + e)
    finally:
        borrowers.close()
        return total_books/valid_count

def count_overdue(filename,current_date):
    ''' Counts the number of borrowers with overdue books
    Parameters:
        filename (str): The name of the CSV file containing borrower data.
        current_date (str): The current date in "YYYY-MM-DD"

     Returns: int: The count of borrowers with overdue books.'''

    with open(filename, "r") as filename:
        filename.readline()
        counter = 0
        for record in filename:
            record = record.strip()
            parts = record.split(",")
            try:
                if int(parts[1])>=0 and parts[2][4]==parts[2][7]=="-":
                    if calculate_fine(int(parts[1]),parts[2],current_date) > 0:
                        counter += 1
            except:
                continue
    return counter

def main():
    ''' Main function that serves as the entry point for the program.
     It prompts the user for a filename, then calls functions from tasks 2, 3, and 4 
     to process borrower data, calculate average books borrowed, and count overdue borrowers.
     Finally, it prints the results of these operations.'''
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