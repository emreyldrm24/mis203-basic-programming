tickets_sold = 0
total_revenue = 0
free_tickets = 0

while True:
    customer_name = input("Customer name (or q to quit): ")
    if customer_name.lower() == "q":
        break

    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day = input("Day (weekday/weekend): ").lower()
    if day != "weekday" and day != "weekend":
        print("Invalid day.")
        continue

    student = input("Student (yes/no): ").lower()
    if student != "yes" and student != "no":
        print("Please answer yes or no.")
        continue

    if day == "weekday":
        base_price = 200
    else:
        base_price = 250

    if age < 6:
        ticket_price = 0
        ticket_type = "Free"
    elif age >= 65:
        ticket_price = base_price * 0.50
        ticket_type = "Senior"
    elif age <= 12:
        ticket_price = base_price * 0.60
        ticket_type = "Child"
    elif student == "yes" and age <= 25:
        ticket_price = base_price * 0.70
        ticket_type = "Student"
    else:
        ticket_price = base_price
        ticket_type = "Standard"

    print(f"{customer_name}: {ticket_price:.2f} TRY ({ticket_type})")

    tickets_sold = tickets_sold + 1
    total_revenue = total_revenue + ticket_price
    if ticket_type == "Free":
        free_tickets = free_tickets + 1

if tickets_sold == 0:
    print("No tickets sold.")
else:
    average_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {average_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
