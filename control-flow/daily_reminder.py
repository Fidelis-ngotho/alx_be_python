# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate reminder based on priority and time sensitivity
def task_reminder(task, priority, time_bound):
    reminder = "Reminder: "

    # Check for priority level using Match Case
    match priority:
        case "high":
            reminder += f"'{task}' is a high priority task"
        case "medium":
            reminder += f"'{task}' is a medium priority task"
        case "low":
            reminder += f"'{task}' is a low priority task"
        case _:
            reminder = "Invalid priority level."

    # Add time sensitivity using an if statement
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder = "Invalid input for time-bound status."

    return reminder

# Print customized reminder
print(task_reminder(task, priority, time_bound))

