# Titanic-analysis
📊 Step 1: Understanding the Dataset
Started by assessing and describing each column in the dataset.
Identified data types:
Numerical columns
Categorical columns
Understood the purpose of each feature before making any changes.

🧹 Step 2: Initial Decisions
PassengerId was NOT dropped, as it may still be useful for tracking records.
Name column was processed:
Extracted surname from full names for better feature understanding.

📈 Step 3: Univariate Analysis (Numerical Columns)
Identified numerical columns.
For each numerical feature:
Used statistical summaries (describe())
Visualized distributions using Seaborn
Identified:
Skewness
Outliers
✔️ Observations
Observations were written after each step.
Issues were clearly documented.

⚠️ Step 4: Handling Issues in Numerical Data
Addressed:
Skewness (when necessary)
Outliers (only when reasonable)
Avoided unnecessary data distortion.

New features like :
lone_traveller
family_size
surnames
fare_per_person
Were added according to need

📊 Step 5: Categorical Analysis
Used .value_counts() to understand category frequencies.
Described each categorical column.
📉 Visualization
Visualized category distributions using Seaborn plots.

🔗 Step 6: Bivariate Analysis
🔢 Numerical vs Numerical
Age vs Fare
Explored relationship between passenger age and ticket fare using scatter plots.

🔀 Numerical vs Categorical
Survived vs Age
Lone Traveler vs Age
Sex vs Age
Pclass vs Age

Used:
Box plots
Violin plots

🔠 Categorical vs Categorical
Survived vs Sex
Survived vs Pclass
Survived vs Lone Traveler
Embarked vs Pclass

Used:
Count plots
Crosstab analysis

Also :
Survived vs Pclass vs Age (multi-variable analysis)

ML work 
Used Linear Regresion model on Age column 
also 
SgdRegressor has been used with proper scalling 

The workflow was like 
1. imports
2. Feature and Target
3. Train Test split
4. Built pipeline
5. Train Model 
6. Predict 
7. Evaluate

