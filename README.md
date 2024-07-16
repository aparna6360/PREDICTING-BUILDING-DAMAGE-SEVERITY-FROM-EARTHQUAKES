**PREDICTING BUILDING DAMAGE SEVERITY FROM EARTHQUAKES**

**Data Overview**

The project revolves around a dataset containing detailed information about buildings affected by earthquakes. This dataset includes 762,106 entries and 31 columns, capturing structural characteristics and post-earthquake conditions of buildings. Each entry represents a specific building in the earthquake-affected region.

**Objective**
------------
The main objective of this analysis is to develop a robust classification model that accurately predicts the severity of damage to buildings following earthquakes. The model utilizes a range of structural and geographical features to differentiate between various damage grades.

Steps Involved in the Project
Project Initiation and Planning: Setting objectives, defining scope, and outlining methodologies.
Data Collection: Gathering the dataset containing building characteristics and earthquake damage information.
Data Preprocessing: Cleaning the data, handling missing values, and removing duplicates.
Exploratory Data Analysis (EDA): Analyzing distributions, correlations, and relationships within the dataset.
Feature Engineering: Creating new features or transforming existing ones to improve model performance.
Model Selection: Choosing appropriate machine learning algorithms for classification.
Model Training: Training selected models on the prepared dataset.
Model Evaluation: Assessing model performance using metrics like accuracy, precision, recall, and F1-score.
Model Deployment: Implementing the best-performing model for real-world predictions.
Key Features
The dataset includes features such as:

Building age, height, and floor count before and after earthquakes.
Structural materials (e.g., adobe/mud, stone, timber) and foundation types.
Geographic attributes like land surface condition and location identifiers.
Analysis Tools
Python libraries including Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn were employed for data manipulation, visualization, and machine learning model implementation. Techniques like StandardScaler for normalization, feature selection using SelectKBest and chi-square tests, and model evaluation via confusion matrices and classification reports were integral to the project.

Outcome
After evaluating multiple models, including K Nearest Neighbors (KNN), Support Vector Machines (SVM), Decision Trees, Random Forests, Gradient Boosting, and XGBoost, the XGBoost classifier emerged as the best-performing model with an accuracy score of 85%. The model effectively predicts damage grades (ranging from Grade 1 to Grade 3) based on building attributes post-earthquake.

Conclusion
This project highlights the importance of leveraging machine learning for predictive analytics in disaster response planning. By accurately forecasting building damage severity, stakeholders can better allocate resources and prioritize recovery efforts in earthquake-prone regions.




