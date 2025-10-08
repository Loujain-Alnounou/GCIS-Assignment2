def main():
    print(calculate_fine(2,"2025-10-01","2025-10-04"))


def calculate_fine(books, due_date, current_date):
    if int(books) < 0:
        return 0

    if due_date[4]!="-" or due_date[7]!="-" or current_date[4]!="-" or current_date[7]!="-":
        return "Error: Invalid date"

    current_split = current_date.split("-")
    due_split = due_date.split("-")

    for i in range(3):
        due_split[i] = int(due_split[i])
        current_split[i] = int(current_split[i])
    for i in range(3):
        if current_split[i]<due_split[i]:
            return 0
        if current_split[i]>due_split[i]:
            days_late = (current_split[0]-due_split[0])*365+(current_split[1]-due_split[1])*30+(current_split[2]-due_split[2])
            fine = days_late*int(books)*2
            return fine
    else:
        return 0

if __name__ == "__main__":
    main()