def main():
    # Empty list, to store daily hours
    daily_hrs = []

    # Asking user for the amount of hours worked with a for variable for the sequence
    for day in range(1, 6):
        hours = float(input(f"Enter hours worked on Day #{day}: "))
        daily_hrs.append(hours)
    print("-----------------------------------------------------------------------------")
    # What are the hours
    max_hours = max(daily_hrs)
    max_hours_days = []
    for day in range(1, 6):
        if daily_hrs[day-1] == max_hours:
            max_hours_days.append(day)
    
    # Calculate total by dividiung total hours 
    hours_worked = sum(daily_hrs)
    avg_hours = max_hours / len(daily_hrs)

    under_7hrs = []
    for day in range(1, 6):
        if daily_hrs[day-1] < 7:
            under_7hrs.append(day)

    # Print outputs
    print("\nThe most hours worked was on:")
    for day in max_hours_days:
        print(f"Day #{day} when you worked {max_hours} hours")
    print("-----------------------------------------------------------------------------")
    print("\nThe total number of hours worked was:", hours_worked)
    print("The average number of hours worked each day was: {:.1f}".format(avg_hours))
    print("-----------------------------------------------------------------------------")
    print("Days you slacked off (i.e. worked less than 7 hours): ")
    for day in under_7hrs:
        print(f"Day #{day}: {daily_hrs[day-1]} hours")


if __name__ == "__main__":
    main()