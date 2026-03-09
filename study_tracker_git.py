
log = []
while True:
    subject = input("Subject studied (type 'done' to finish): ")
    if subject.lower() == "done":
        print("------------------------")
        break
    hours = float(input("How many hours did you study this subject?"))
    log.append((subject, hours))
    print("Today you studied:", subject, "for", hours, "hours today!")
    print("------------------------")

print("Here is your study log for today:") # Header
print("Subject         | Hours")  
print("--------------------------")
for entry in log:
    print(f"{entry[0]:<15} | {entry[1]}")

total_hours = 0
for entry in log:
    hours = entry[1]
    total_hours += hours
    break
print("--------------------------")
print(f"Total hours studied today: {total_hours:.2f}")
