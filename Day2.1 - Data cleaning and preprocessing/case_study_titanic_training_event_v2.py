# -*- coding: utf-8 -*-
"""Case_study_titanic_training_event_v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-eAJc5ThzHMvsy2qacUX0ALPEZjSEdGX

**Case Study - Impact of Data Cleaning and Preprocessing Techniques on a Real-World Dataset**

Let's walk through a case study using the Titanic dataset from Kaggle. We'll observe the impact of data cleaning and preprocessing on a logistic regression model that predicts survival on the Titanic.

This notebook presents a simple machine learning model to predict the survival of passengers on the Titanic. It involves data cleaning, feature engineering, and application of logistic regression. The dataset is obtained from the Data Science Dojo's repository.

## Titanic Dataset Description

The Titanic dataset is a classic dataset used in data science and machine learning. It consists of demographic and traveling information for 1,309 passengers of the Titanic, and the goal is to predict the survival of these passengers. The data is a mix of textual, Boolean, continuous, and categorical variables, making it a rich database for data transformations. The dataset exhibits interesting characteristics such as missing values, outliers, and text variables ripe for text mining.

Here is a brief summary of the 14 attributes:

1. `pclass`: Passenger class (1 = 1st; 2 = 2nd; 3 = 3rd)
2. `survived`: A Boolean indicating whether the passenger survived or not (0 = No; 1 = Yes); this is our target
3. `name`: A field rich in information as it contains title and family names
4. `sex`: male/female
5. `age`: Age, a significant portion of values are missing
6. `sibsp`: Number of siblings/spouses aboard
7. `parch`: Number of parents/children aboard
8. `ticket`: Ticket number
9. `fare`: Passenger fare (British Pound)
10. `cabin`: Does the location of the cabin influence chances of survival?
11. `embarked`: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
12. `boat`: Lifeboat, many missing values
13. `body`: Body Identification Number
14. `home.dest`: Home/destination&#8203;`oaicite:{"index":1,"metadata":{"title":"hub.packtpub.com","url":"https://hub.packtpub.com/introduction-titanic-datasets/","text":"pclass: Passenger class (1 = 1st; 2 = 2nd; 3 = 3rd)\n  * survival: A Boolean indicating whether the passenger survived or not (0 = No; 1 = Yes); this is our target\n  * name: A field rich in information as it contains title and family names\n  * sex: male/female\n  * age: Age, asignificant portion of values aremissing\n  * sibsp: Number of siblings/spouses aboard\n  * parch: Number of parents/children aboard\n  * ticket: Ticket number.\n  * fare: Passenger fare (British Pound).\n  * cabin: Doesthe location of the cabin influence chances of survival?\n  * embarked: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)\n  * boat: Lifeboat, many missing values\n  * body: Body Identification Number\n  * home.dest: Home/destination\n\nTake a look at http://campus.lakeforest.edu/frank/FILES/MLFfiles/Bio150/Titanic/TitanicMETA.pdf for more details on these variables","pub_date":null}}`&#8203;.

Among the 14 attributes, we have 1,309 records. However, three of the attributes - `home.dest`, `boat`, and `body` - will typically be discarded due to too few existing values or because their presence is highly correlated with survival&#8203;`oaicite:{"index":2,"metadata":{"title":"hub.packtpub.com","url":"https://hub.packtpub.com/introduction-titanic-datasets/","text":"We have 1,309 records and 14 attributes, three of which we will discard. The home.dest attribute hastoo few existing values, the boat attribute is only present for passengers who have survived, and thebody attributeis only for passengers who have not survived. We will discard these three columnslater on while using the data schema","pub_date":null}}`&#8203;.

## Data Sample

| pclass | survived | name | sex | age | sibsp | parch | ticket | fare | cabin | embarked | boat | body | home.dest |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

In this section, we import necessary Python libraries such as pandas for data manipulation, sklearn for machine learning model building, and metrics for model evaluation.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler

"""Here we load the Titanic dataset which is hosted on the Data Science Dojo's GitHub repository. The data is in CSV format.

"""

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

"""Initial data cleaning involves dropping unnecessary columns that will not contribute to our machine learning model. For our baseline model, we drop columns such as 'Name', 'Age', 'Sex', 'Ticket', 'Cabin', and 'Embarked'.

"""

# Drop columns with missing or incomplete sets
df = df.drop(['Name','Age','Sex','Ticket','Cabin','Embarked'], axis=1)

"""In this section, we separate the dataset into features (X) and target (y). The 'Survived' column is our target variable.

"""

X = df.drop('Survived', axis=1)
y = df['Survived']

"""We split our data into training and testing sets. The training set is used to train our machine learning model, and the testing set is used to evaluate the model's performance.

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""In this section, we begin our journey into machine learning by building an initial model. Our choice of model is Logistic Regression, a fundamental and widely used classification algorithm. 

Logistic Regression is used when the dependent variable (target) is categorical. In our case, the target is 'Survived', which is binary (0 or 1, indicating if a passenger survived or not). 

We chose Logistic Regression because of its simplicity and because it serves as a good baseline model. It's straightforward to implement and interpret, and it performs well on linearly separable classes. 

We initialize the Logistic Regression model with a maximum iteration parameter of 1000. This parameter dictates the maximum number of iterations for the solver (the algorithm used for optimization problem) to converge. If our model does not converge (i.e., reach the optimal solution) before hitting this limit, the algorithm will stop and return the best solution found so far. 

After initializing our model, we train it using the `fit` method, which is where the learning happens. The `fit` method adjusts the model's parameters to minimize the cost function. In this case, we have to handle the missing values in our training data. We use the mean of the non-missing values in the training set to fill in these gaps. 

This completes the building of our initial model. We will evaluate this model's performance in the next section.

"""

model = LogisticRegression(max_iter=1000)
model.fit(X_train.fillna(X_train.mean()), y_train)

"""We evaluate the performance of our baseline model by predicting the target variable for our test set and comparing the predictions with the actual values. The metric used here is accuracy.

"""

y_pred = model.predict(X_test.fillna(X_test.mean()))
print(f'Baseline Accuracy: {accuracy_score(y_test, y_pred)}')

"""In this section, we perform more detailed data cleaning and preprocessing to further prepare our data for the machine learning model. Here are the steps we take:

1. **Reload the Dataset**: We start by reloading the original dataset to get back the columns we initially dropped.

2. **Drop Unnecessary Columns**: We drop the 'Name' and 'Ticket' columns. The 'Name' column is unique for almost every passenger and thus does not provide useful information for our model. The 'Ticket' column is also dropped as it contains a high number of unique values and would be difficult to encode.

3. **Fill Missing Values**: The 'Age' column contains missing values. We fill these missing values with the median age. The median is chosen over the mean to avoid being affected by any outliers in ages.

4. **Convert Categorical Variables to Numerical**: We convert the 'Cabin' column to binary by marking the absence of a cabin as 1 and the presence as 0. We also perform label encoding on the 'Sex' column by mapping 'male' to 0 and 'female' to 1.

5. **One-Hot Encoding**: For the 'Embarked' column, we perform one-hot encoding. This method of encoding converts each category value into a new column and assigns a 1 or 0 to the column. We use pandas' `get_dummies` function to do this.

6. **Create New Features**: We create a new 'FamilySize' feature by adding the number of siblings/spouses ('SibSp') and the number of parents/children ('Parch') for each passenger plus 1 (the passenger themself). We also create an 'IsAlone' feature that denotes whether a passenger is traveling alone, which is the case when the 'FamilySize' is 1.

7. **Standard Scaling**: Finally, we apply standard scaling to the 'Age' and 'Fare' columns to standardize their values to have a mean of 0 and a standard deviation of 1. Standard scaling is important for many machine learning models as they can perform poorly if the features are not on similar scales. This is particularly true for models that use distance measures, like k-nearest neighbors (KNN), and models that use regularization, like logistic regression and support vector machines (SVMs).

"""

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Drop 'Name' and 'Ticket' columns
df = df.drop(['Name', 'Ticket'], axis=1)

# Fill missing values in Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Convert Cabin to binary
df['Cabin'] = df['Cabin'].isnull().astype(int)

# Label encoding for 'Sex'
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# One-hot encoding for 'Embarked'
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Creating 'FamilySize' feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Creating 'IsAlone' feature
df['IsAlone'] = 0
df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1

# Apply Standard Scaling to 'Age' and 'Fare'
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

"""With our cleaned data, we again separate the dataset into features (X) and target (y). The 'Survived' column is our target variable.

"""

X = df.drop('Survived', axis=1)
y = df['Survived']

"""We again split our cleaned data into training and testing sets.

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""We build a Logistic Regression model using the cleaned data.

"""

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

"""We evaluate the performance of our model by predicting the target variable for our test set and comparing the predictions with the actual values. The metrics used here are accuracy, precision, recall, and F1 score.

"""

y_pred = model.predict(X_test)
print(f'Final Accuracy: {accuracy_score(y_test, y_pred)}')
print(f'Precision: {precision_score(y_test, y_pred)}')
print(f'Recall: {recall_score(y_test, y_pred)}')
print(f'F1 Score: {f1_score(y_test, y_pred)}')

"""To ensure that our model's performance is reliable and not due to a particular random split of the data, we perform cross-validation. Cross-validation involves splitting the data multiple times and averaging the performance metrics.

"""

from sklearn.model_selection import cross_val_score,cross_validate
import numpy as np

# Use cross_validate to get multiple scores
cv_results = cross_validate(model, X_test, y_test, cv=5, 
                            scoring=('accuracy', 'precision', 'recall', 'f1'))

# Display scores with their mean and standard deviation
for score in ['test_accuracy', 'test_precision', 'test_recall', 'test_f1']:
    mean_score = np.mean(cv_results[score])
    std_score = np.std(cv_results[score])
    print(f"{score}: {mean_score:.2f} (+/- {std_score:.2f})")