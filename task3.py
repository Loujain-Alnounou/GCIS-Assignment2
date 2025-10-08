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
        borrowers.seek(28,0)

        for line in borrowers:
            line = line.strip()
            parts = line.split(',')
            if len(parts) == 3 and int(parts[1])>=0 and len(parts[2])==10 and parts[2][4]==parts[2][7]=="-":
                try:
                    books = int(parts[1].strip())

                    total_books += books
                    valid_count += 1
                except ValueError:
                    continue
            
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except Exception as e:
        print(f"Error reading line: {e}")
    borrowers.close()
    return total_books/valid_count


def main(): #calling the main function
    print(calculate_average_books("borrowers.csv"))


if __name__ == "__main__":
    main()