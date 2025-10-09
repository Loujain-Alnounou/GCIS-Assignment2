#task 3

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
        except (ValueError,ZeroDivisionError):
            continue
            
    except FileNotFoundError:
        print("Error: File " + filename + " not found.")
    except Exception as e:
        print("Error: " + e)
    finally:
        borrowers.close()
        return total_books/valid_count


def main(): #calling the main function
    print(calculate_average_books("borrowers.csv"))


if __name__ == "__main__":
    main()