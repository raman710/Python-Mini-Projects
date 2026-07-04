import numpy as np

print("=" * 45)
print("      NUMPY STATISTICS DASHBOARD")
print("=" * 45)

# Take input from user
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

# Convert list into NumPy array
data = np.array(numbers)

while True:

    print("\n----- MENU -----")
    print("1. Display Data")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Maximum")
    print("6. Minimum")
    print("7. Sum")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nData:", data)

    elif choice == "2":
        print("Mean =", np.mean(data))

    elif choice == "3":
        print("Median =", np.median(data))

    elif choice == "4":
        print("Standard Deviation =", np.std(data))

    elif choice == "5":
        print("Maximum =", np.max(data))

    elif choice == "6":
        print("Minimum =", np.min(data))

    elif choice == "7":
        print("Sum =", np.sum(data))

    elif choice == "8":
        print("\nThank you for using NumPy Statistics Dashboard!")
        break

    else:
        print("Invalid Choice! Please try again.")