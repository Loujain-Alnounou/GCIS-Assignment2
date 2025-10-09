from task1 import calculate_fine
def main():
    print(count_overdue("borrowers.csv","2025-10-04"))

def count_overdue(filename,current_date):
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

if __name__ == "__main__":
    main()