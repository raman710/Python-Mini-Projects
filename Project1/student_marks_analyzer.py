# --------------------------------------------
# Student Marks Analyzer Using Pandas
# --------------------------------------------

import pandas as pd

print("=" * 50)
print("       STUDENT MARKS ANALYZER")
print("=" * 50)

try:
    # Read the CSV file
    df = pd.read_csv("student_marks.csv")

    # Display student records
    print("\nStudent Records:\n")
    print(df)

    # Calculate Total Marks
    df["Total"] = df["Math"] + df["Science"] + df["English"]

    # Calculate Percentage
    df["Percentage"] = (df["Total"] / 300) * 100

    # Function to assign grades
    def calculate_grade(percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "Fail"

    # Add Grade column
    df["Grade"] = df["Percentage"].apply(calculate_grade)

    # Display Final Result
    print("\nFinal Result:\n")
    print(df)

    # Find Topper
    topper = df.loc[df["Percentage"].idxmax()]

    print("\n" + "=" * 50)
    print("TOPPER DETAILS")
    print("=" * 50)
    print("Name       :", topper["Name"])
    print("Total      :", topper["Total"])
    print("Percentage :", round(topper["Percentage"], 2), "%")
    print("Grade      :", topper["Grade"])

    # Class Statistics
    print("\n" + "=" * 50)
    print("CLASS STATISTICS")
    print("=" * 50)

    print("Highest Percentage :", round(df["Percentage"].max(), 2), "%")
    print("Lowest Percentage  :", round(df["Percentage"].min(), 2), "%")
    print("Average Percentage :", round(df["Percentage"].mean(), 2), "%")

    # Save result to CSV
    df.to_csv("result.csv", index=False)

    print("\nResult saved successfully as 'result.csv'")

except FileNotFoundError:
    print("Error: student_marks.csv file not found!")

except Exception as e:
    print("An error occurred:", e)