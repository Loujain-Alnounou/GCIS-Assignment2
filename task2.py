#task 2
from task1 import calculate_fine
def main():
    print(process_borrowers("borrowers.csv","2025-10-4"))

def process_borrowers(filename,current_date):
    try:
        borrowers =  open(filename, 'r')
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
                        ledger += parts[0]+": Fine: $"+{fine}+"\n"
                    else:
                        ledger += parts[0]+": No dues\n"

            except Exception as e:
                ledger += "Error reading line: "+ {e}+"\n"

    except FileNotFoundError:
        print("Error: File " + filename + " not found.")
    finally:
        borrowers.close()
        return ledger
if __name__ == "__main__":
    main()