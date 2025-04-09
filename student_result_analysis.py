import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Dipti', 'Aarav', 'Neha', 'Ravi', 'Megha'],
    'Math': [88, 92, 79, 85, 90],
    'Science': [90, 85, 80, 88, 92],
    'English': [84, 87, 78, 82, 88]
}

df = pd.DataFrame(data)

df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average'] = df['Total'] / 3

def grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Average'].apply(grade)

top_students = df.sort_values(by='Total', ascending=False).head(3)

plt.figure(figsize=(8,5))
plt.bar(df['Name'], df['Total'], color='skyblue')
plt.title('Total Scores of Students')
plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.tight_layout()
plt.savefig("student_scores.png")
plt.show()

df.to_csv('student_results.csv', index=False)
print("Student Result Analysis Done. Check CSV and PNG files.")
