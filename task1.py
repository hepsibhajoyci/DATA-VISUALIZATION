import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# -------------------------------
# BAR CHART - Gender Distribution
# -------------------------------

gender_count = df['Sex'].value_counts()

plt.figure(figsize=(6,4))
sns.barplot(
    x=gender_count.index,
    y=gender_count.values
)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.show()

# -------------------------------
# HISTOGRAM - Age Distribution
# -------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df['Age'].dropna(),
    bins=10
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()