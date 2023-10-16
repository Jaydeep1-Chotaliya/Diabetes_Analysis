# Diabetes-Analysis
![elena-leya-UE_Nl6Necnk-unsplash](https://github.com/Jaydeep1-Chotaliya/Diabetes_Analysis/assets/129647680/da7ae6e8-230f-4bdd-b45e-28b9c0aed04f)

## **INTRODUCTION** ##

+ Diabetes is a chronic disease that affects millions of people worldwide. It is caused by the inability of the body to produce or use insulin properly, resulting in high levels of glucose in the blood. Early detection and management of diabetes can prevent complications such as blindness, kidney disease, nerve damage, and heart disease.
+ In 2014, 8.5% of adults aged 18 years and older had diabetes. In 2019, diabetes was the direct cause of 1.5 million deaths and 48% of all deaths due to diabetes occurred before the age of 70 years. 
+ Another 460,000 kidney disease deaths were caused by diabetes, and raised blood glucose causes around 20% of cardiovascular deaths.

## **Outline of the problem to solve** ##

* Objective: Develop a predictive model for accurately forecasting the likelihood of developing diabetes based on health-related features.
* Method: Utilize machine learning algorithms and a comprehensive dataset to build the predictive model.
* Impact on Healthcare: Assist healthcare providers in identifying individuals at higher risk of diabetes. Enable proactive healthcare interventions like lifestyle modifications and targeted monitoring.
* Promoting a Data-Driven Approach in Healthcare: Showcase technology's potential in improving health outcomes. Empower healthcare professionals and individuals with valuable data-derived insights.
* Ultimate Goal: Contribute to a healthier society by utilizing machine learning for early diabetes risk assessment and promoting a proactive healthcare approach.

## **Methodology** ##
1. Dataset info: This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases.
   
| **Attribute** | **Feature's Meaning** |
| ------------- | :--- |
| Pregnancies  | Number of times pregnant |
| Glucose  | Plasma glucose concentration 2 hours in an oral glucose tolerance test |
| BloodPressure  | Diastolic blood pressure (mm Hg) |
| SkinThickness  | Triceps skin fold thickness (mm) |
| Insulin  | 2-Hour serum insulin (mu U/ml) |
| BMI  | Body mass index (weight in kg/(height in m)^2) |
| DiabetesPedigreeFunction  | Diabetes pedigree function |
| Age  | Age (years) |
| Outcome  | Class variable (0 or 1) |

2. Data Exploration: Summary Statistics: Calculate basic statistics (mean, median, standard deviation, min, max) for numerical features to understand their central tendencies and variability.
   
3. Explore the distribution and summary of each feature, identifying outliers, unusual patterns, or missing values.

4. Examine the correlation between features to identify potential multicollinearity and relationships that can aid in feature selection.

# **Results/Insights:** #

1. from the graph, we can illustrate that a high glucose level indicates a person has more chance of diabetes.

+ The correlation coefficient between glucose levels and the presence of diabetes in patients indicates a strong positive correlation. The plot visually supports this, showcasing higher glucose levels in individuals identified as diabetic.

+ Understanding this strong positive correlation is vital, as elevated glucose levels are a hallmark of diabetes. It emphasizes the importance of glucose levels as a predictive feature in the diabetes prediction model, supporting the model's accuracy in identifying individuals at risk of diabetes based on this crucial health indicator.

![diab_page-0002](https://github.com/Jaydeep1-Chotaliya/Diabetes_Analysis/assets/129647680/52ff7c86-b35f-4663-8317-d57a12342c5d)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. The correlation between BMI and the presence of diabetes was found, indicating a moderate to strong positive correlation. The plot visually supports this, revealing higher BMI levels in individuals identified as diabetic. This suggests that higher BMI is associated with an increased likelihood of diabetes.

+ Understanding this correlation is crucial, as BMI is a well-established indicator of body composition and health. The strong correlation between BMI and diabetes further emphasizes the importance of considering BMI as a predictive feature in the diabetes prediction model. Including BMI alongside glucose levels enhances the model's accuracy in identifying individuals at risk of diabetes, providing a more comprehensive assessment of their diabetes risk.

![diab_page-0003](https://github.com/Jaydeep1-Chotaliya/Diabetes_Analysis/assets/129647680/7fe23bf2-c540-44d2-a68d-f1404e176f1f)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **CONCLUSION** ##

* Project Objective and Model Selection:
  
Goal: Predict diabetes likelihood based on health-related features.

Model choice: Logistic Regression was selected after comprehensive analysis.


* Logistic Regression Model Performance.
  
Accurate classification into diabetes risk categories.

Effective use of key features like glucose levels, BMI, blood pressure, and age.

Strong interpretability, aiding diabetes risk assessment.

* Advantages of Logistic Regression Model:
* 
Clear feature contributions for better understanding.

Robustness and generalization were demonstrated through testing.

Performance evaluation using accuracy, precision, recall, and F1-score.

* Model Metrics:
  
High accuracy: 81%.

Precision score: 0.7.

Recall: 0.63.

F1-score: 0.66, indicating strong predictive capabilities.


## **Summary of limitations/challenges faced** ##

* Achieving an overall model accuracy of 81% is promising, it's important to note that accuracy alone may not provide a complete picture, especially in datasets or critical domains such as healthcare.

* The precision of 70% suggests that there is a significant false positive rate, meaning the model may incorrectly identify some individuals as diabetic. This could have serious implications in healthcare where false positives may lead to unnecessary interventions or anxiety for patients.

* Navigating the intricacies of the healthcare domain, specifically diabetes, can be daunting for individuals with an engineering background due to its complex nature. Diabetes involves multifaceted biological systems and medical intricacies that require specialized knowledge and a nuanced understanding of both the physiological and technological aspects.

* The healthcare industry faces significant challenges, particularly regarding the integration of advanced technologies that bring it closer to a human-centered approach while upholding the necessity for high accuracy in medical processes. Balancing these two objectives poses a complex dilemma for the industry.

* ## **Deployment of our project :** ##

![Untitled video - Made with Clipchamp (1)](https://github.com/Jaydeep1-Chotaliya/Diabetes_Analysis/assets/129647680/7142c905-6226-42ca-96d3-90b698bdb327)

* Deployment transitions a project from development/testing to the live production environment.
* Goal: Make the project fully operational for intended users and stakeholders.
* Successful deployment ensures smooth function and value delivery.
