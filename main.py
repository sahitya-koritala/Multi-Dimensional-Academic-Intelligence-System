import random
import pandas as pd
import numpy as np
import math

def create_students(num):
    records = []

    for i in range(1, num + 1):
        m = random.randint(0, 100)
        att = random.randint(0, 100)
        assign = random.randint(0, 50)

        perf = (m * 0.6 + assign * 0.4) * math.log(att + 1)

        records.append((i, m, att, assign, perf))

    return records

def student_category(data):
    result = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for s in data:
        sid, m, att, assign, perf = s

        if m < 40 or att < 50:
            result["At Risk"].append(sid)
        elif 40 <= m <= 70:
            result["Average"].append(sid)
        elif 71 <= m <= 90:
            result["Good"].append(sid)
        elif m > 90 and att > 80:
            result["Top Performer"].append(sid)

    return result

def stats_analysis(df):
    marks = df["Marks"].values

    avg = sum(marks) / len(marks)

    median_val = np.median(marks)
    std_val = np.std(marks)

    corr_val = np.corrcoef(df["Marks"], df["Attendance"])[0][1]

    mn = np.min(marks)
    mx = np.max(marks)
    df["Norm Marks"] = [(x - mn) / (mx - mn) for x in marks]

    tup = (avg, std_val, mx)

    return avg, median_val, std_val, corr_val, tup

roll = int(input("Enter roll number: "))
n = roll % 10

if n == 0:
    n = 10

data = create_students(n)

df = pd.DataFrame(data, columns=[
    "ID", "Marks", "Attendance", "Assignment", "Perf Index"
])

df["Result"] = ["Pass" if m >= 40 else "Fail" for m in df["Marks"]]

categories = student_category(data)

mean_v, median_v, std_v, corr_v, tup_v = stats_analysis(df)

consistency = "Consistent" if std_v < 15 else "Inconsistent"
low_att = len([a for a in df["Attendance"] if a < 50]) > 3
top_count = len(categories["Top Performer"]) >= 2

if consistency == "Consistent" and not low_att:
    final_msg = "Stable Academic System"
elif top_count:
    final_msg = "Moderate Performance"
else:
    final_msg = "Critical Attention Required"

print("\nStudent Data:\n", df)

print("\nCategories:\n", categories)

print("\nStatistics:")
print("Mean =", mean_v)
print("Median =", median_v)
print("Std Dev =", std_v)
print("Correlation =", corr_v)

print("\nTuple Output:", tup_v)

print("\nFinal System Insight:", final_msg)
