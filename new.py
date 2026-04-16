# ==============================
# 1. API REQUESTS
# ==============================
import requests

# GET request
get_resp = requests.get("https://jsonplaceholder.typicode.com/posts")
print("GET Status:", get_resp.status_code)

# PUT request (update)
put_resp = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"id": 1, "title": "updated", "body": "Hello", "userId": 1}
)
print("PUT Status:", put_resp.status_code)

# DELETE request
delete_resp = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print("DELETE Status:", delete_resp.status_code)

# HEAD request
head_resp = requests.head("https://jsonplaceholder.typicode.com/posts")
print("HEAD Headers:", head_resp.headers)


# ==============================
# 2. WEB SCRAPING
# ==============================
from bs4 import BeautifulSoup

res = requests.get("https://quotes.toscrape.com/tag/love")
soup = BeautifulSoup(res.content, "html.parser")

content = soup.find_all("span", class_="text")

print("\nQuotes:")
for quote in content:
    print(quote.text.strip())


# ==============================
# 3. IQR OUTLIER DETECTION
# ==============================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {"marks": [45, 50, 52, 48, 47, 90, 49, 61, 51, 44]}
df = pd.DataFrame(data)

# Boxplot
sns.boxplot(y=df["marks"])
plt.title("Boxplot for Outlier Detection")
plt.show()

Q1 = df["marks"].quantile(0.25)
Q3 = df["marks"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_iqr_clean = df[(df["marks"] >= lower) & (df["marks"] <= upper)]
print("\nIQR Clean Data:\n", df_iqr_clean)


# ==============================
# 4. Z-SCORE METHOD
# ==============================
import numpy as np
from scipy import stats

data = {"values": [12, 15, 14, 10, 9, 100, 8, 13, 10, 14, 11, 10]}
df = pd.DataFrame(data)

df["z_score"] = np.abs(stats.zscore(df["values"]))
df_z_clean = df[df["z_score"] <= 2]

print("\nZ-score Clean Data:\n", df_z_clean)


# ==============================
# 5. MULTIVARIATE Z-SCORE
# ==============================
data = {
    "x": [10, 12, 11, 13, 12, 50],
    "y": [20, 22, 21, 23, 22, 100]
}
df = pd.DataFrame(data)

from scipy.stats import zscore

df["z_x"] = zscore(df["x"])
df["z_y"] = zscore(df["y"])

df_multi_clean = df[(abs(df["z_x"]) <= 2) & (abs(df["z_y"]) <= 2)]

plt.scatter(df_multi_clean["x"], df_multi_clean["y"])
plt.title("Cleaned Scatter Plot")
plt.show()


# ==============================
# 6. GRUBBS TEST
# ==============================
from outliers_utils import smirnov_grubbs as grubbs

data = np.array([15, 14, 15, 16, 14, 19, 17, 6, 25, 22, 8, 21, 28, 11, 9, 29, 40])
max_outlier = grubbs.max_test(data, alpha=0.05)

print("\nGrubbs Test Outlier:", max_outlier)


# ==============================
# 7. MAHALANOBIS DISTANCE
# ==============================
from scipy.spatial.distance import mahalanobis

data = {
    "Feature1": [10, 12, 10, 14, 10, 20, 100],
    "Feature2": [20, 24, 20, 28, 22, 50, 110]
}

df = pd.DataFrame(data)

mean = df.mean().values
cov = np.cov(df.values.T)
inv_cov = np.linalg.pinv(cov)

distances = []

for row in df.values:
    dist = mahalanobis(row, mean, inv_cov)
    distances.append(dist)

df["Mahalanobis"] = distances

threshold = np.percentile(distances, 95)
df["Outlier"] = df["Mahalanobis"] > threshold

print("\nMahalanobis Results:\n", df)


# ==============================
# 8. LOCAL OUTLIER FACTOR
# ==============================
from sklearn.neighbors import LocalOutlierFactor

X = df[["Feature1", "Feature2"]]

lof = LocalOutlierFactor(n_neighbors=2, contamination=0.2)
labels = lof.fit_predict(X)

df["LOF_Outlier"] = labels
print("\nLOF Results:\n", df)


# ==============================
# 9. ONE-CLASS SVM
# ==============================
from sklearn.svm import OneClassSVM

model = OneClassSVM(nu=0.1, kernel="rbf", gamma="scale")
model.fit(X)

svm_labels = model.predict(X)
df["SVM_Outlier"] = svm_labels

print("\nSVM Results:\n", df)


# ==============================
# 10. EDA (DATA ANALYSIS)
# ==============================

# Load dataset (make sure EDA.csv exists)
try:
    data = pd.read_csv("EDA.csv")

    print("\nHead:\n", data.head())
    print("\nShape:", data.shape)

    categorical_cols = data.select_dtypes(include=["object"]).columns
    numerical_cols = data.select_dtypes(include=["int64", "float64"]).columns

    print("\nCategorical Columns:", categorical_cols)
    print("Numerical Columns:", numerical_cols)

    # Check duplicates
    print("Duplicate IDs:", data.duplicated().sum())

    # Convert to numeric
    if "TotalCharges" in data.columns:
        data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")

        # Fill missing values
        data["TotalCharges"].fillna(data["TotalCharges"].median(), inplace=True)

    # Histogram
    if "tenure" in data.columns:
        plt.hist(data["tenure"], bins=10)
        plt.title("Distribution of Tenure")
        plt.xlabel("Tenure")
        plt.ylabel("Frequency")
        plt.show()

    # Countplot
    if "churn" in data.columns:
        sns.countplot(x="churn", data=data)
        plt.title("Churn Count")
        plt.show()

except FileNotFoundError:
    print("\nEDA.csv file not found. Skipping EDA section.")


# ==============================
# END OF SCRIPT
# ==============================

import requests
import pandas as pd
import matplotlib.pyplot as plt

res = requests.get("https://jsonplaceholder.typicode.com/posts")
data = res.json()

df = pd.DataFrame(data)

# Visualization
plt.hist(df["userId"], bins=10)
plt.title("Distribution of Posts per User")
plt.xlabel("User ID")
plt.ylabel("Frequency")
plt.show()

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

res = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(res.text, "html.parser")

quotes = [q.text for q in soup.find_all("span", class_="text")]

lengths = [len(q) for q in quotes]

plt.hist(lengths, bins=5)
plt.title("Quote Length Distribution")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {"marks": [45, 50, np.nan, 48, 47, np.nan, 49]}
df = pd.DataFrame(data)

# Fill missing
df["marks"].fillna(df["marks"].mean(), inplace=True)

plt.plot(df["marks"], marker='o')
plt.title("Marks After Filling Missing Values")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 40000, 45000]
})

grouped = df.groupby("Department")["Salary"].mean()
print(grouped)

grouped.plot(kind="bar")
plt.title("Average Salary by Department")
plt.show()


import seaborn as sns

data = {"marks": [45, 50, 52, 48, 47, 90, 49]}
df = pd.DataFrame(data)

sns.boxplot(y=df["marks"])
plt.show()


from scipy.stats import zscore

df["z"] = zscore(df["marks"])
df_clean = df[abs(df["z"]) < 2]

print(df_clean)



from scipy.spatial.distance import mahalanobis
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[10,20],[12,22],[11,21],[50,100]])

mean = data.mean(axis=0)
cov = np.cov(data.T)
inv_cov = np.linalg.inv(cov)

distances = [mahalanobis(x, mean, inv_cov) for x in data]

print(distances)


from sklearn.neighbors import LocalOutlierFactor

X = [[10,20],[12,22],[11,21],[50,100]]

lof = LocalOutlierFactor(n_neighbors=2)
labels = lof.fit_predict(X)

print(labels)


import seaborn as sns

df = sns.load_dataset("tips")

sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Bill vs Tip")
plt.show()



# ============================================
# EXPLORATORY DATA ANALYSIS - FULL SOLUTION FILE
# Covers: API, Scraping, Cleaning, EDA, Outliers
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# ============================================
# 1. API DATA FETCHING + VISUALIZATION
# ============================================
print("\n--- API DATA FETCHING ---")
res = requests.get("https://jsonplaceholder.typicode.com/posts")
data = res.json()

df_api = pd.DataFrame(data)
print(df_api.head())

# Visualization
plt.hist(df_api["userId"], bins=10)
plt.title("Posts per User")
plt.xlabel("User ID")
plt.ylabel("Frequency")
plt.show()


# ============================================
# 2. WEB SCRAPING
# ============================================
print("\n--- WEB SCRAPING ---")
from bs4 import BeautifulSoup

res = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(res.text, "html.parser")

quotes = [q.text for q in soup.find_all("span", class_="text")]
print("Sample Quotes:", quotes[:5])

# Quote length visualization
lengths = [len(q) for q in quotes]
plt.hist(lengths, bins=5)
plt.title("Quote Length Distribution")
plt.show()


# ============================================
# 3. MISSING VALUE HANDLING
# ============================================
print("\n--- MISSING VALUES ---")
data = {"marks": [45, 50, np.nan, 48, 47, np.nan, 49]}
df = pd.DataFrame(data)

print("Before:\n", df)

df["marks"].fillna(df["marks"].mean(), inplace=True)

print("After:\n", df)

plt.plot(df["marks"], marker='o')
plt.title("After Filling Missing Values")
plt.show()


# ============================================
# 4. DATA WRANGLING (GROUPBY)
# ============================================
print("\n--- DATA WRANGLING ---")
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 40000, 45000]
})

grouped = df.groupby("Department")["Salary"].mean()
print(grouped)

grouped.plot(kind="bar")
plt.title("Average Salary")
plt.show()


# ============================================
# 5. IQR OUTLIER DETECTION
# ============================================
print("\n--- IQR OUTLIERS ---")
data = {"marks": [45, 50, 52, 48, 47, 90, 49]}
df = pd.DataFrame(data)

sns.boxplot(y=df["marks"])
plt.title("Boxplot")
plt.show()

Q1 = df["marks"].quantile(0.25)
Q3 = df["marks"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_iqr = df[(df["marks"] >= lower) & (df["marks"] <= upper)]
print("IQR Cleaned:\n", df_iqr)


# ============================================
# 6. Z-SCORE OUTLIER DETECTION
# ============================================
print("\n--- Z-SCORE ---")
from scipy.stats import zscore

df["z"] = zscore(df["marks"])
df_z = df[abs(df["z"]) < 2]

print(df_z)


# ============================================
# 7. MAHALANOBIS DISTANCE
# ============================================
print("\n--- MAHALANOBIS ---")
from scipy.spatial.distance import mahalanobis

data = np.array([[10, 20], [12, 22], [11, 21], [50, 100]])

mean = data.mean(axis=0)
cov = np.cov(data.T)
inv_cov = np.linalg.inv(cov)

distances = [mahalanobis(x, mean, inv_cov) for x in data]
print("Distances:", distances)


# ============================================
# 8. LOCAL OUTLIER FACTOR
# ============================================
print("\n--- LOF ---")
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors=2)
labels = lof.fit_predict(data)

print("LOF Labels:", labels)


# ============================================
# 9. ONE CLASS SVM
# ============================================
print("\n--- ONE CLASS SVM ---")
from sklearn.svm import OneClassSVM

model = OneClassSVM(nu=0.1)
model.fit(data)

svm_labels = model.predict(data)
print("SVM Labels:", svm_labels)


# ============================================
# 10. EDA (BUILT-IN DATASET)
# ============================================
print("\n--- EDA ---")
df = sns.load_dataset("tips")

print(df.head())
print("Shape:", df.shape)

# Scatterplot
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Bill vs Tip")
plt.show()

# Histogram
plt.hist(df["total_bill"], bins=10)
plt.title("Total Bill Distribution")
plt.show()

# Countplot
sns.countplot(x="day", data=df)
plt.title("Count by Day")
plt.show()


# ============================================
# END
# ============================================
