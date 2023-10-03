# Diabetes-Analysis
![elena-leya-UE_Nl6Necnk-unsplash](https://github.com/Jaydeep1-Chotaliya/Diabetes_Analysis/assets/129647680/da7ae6e8-230f-4bdd-b45e-28b9c0aed04f)
**1 INTRODUCTION** 

Diabetes is a chronic disease that affects millions of people worldwide. It is caused by the inability of the body to produce or use insulin properly, resulting in high levels of glucose in the blood. Early detection and management of diabetes can prevent complications such as blindness, kidney disease, nerve damage, and heart disease.

In 2014, 8.5% of adults aged 18 years and older had diabetes. In 2019, diabetes was the direct cause of 1.5 million deaths and 48% of all deaths due to diabetes occurred before the age of 70 years. 
Another 460 000 kidney disease deaths were caused by diabetes, and raised blood glucose causes around 20% of cardiovascular deaths.

**2 SOLUTION STRATERGY** 

Problem solution follows the following steps:

**Step 1 Data description :**

This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases.
The objective of the dataset is to diagnostically predict whether a patient has diabetes, based on certain diagnostic measurements included such as, Glucose, Bloodpressure, insuline and  BMI in the dataset. Several constraints were placed on the selection of these instances from a larger database.

**Step 2 Data Filtering :**
This step involves finding and removing the NaN value and unnecessary rows and columns that are not a part of the business. Removing the Outliers.

**Step 3 Data Analysis :**
This step follows the finding unique values, Data summary, co-relation of data.

**Step 4 Data Preparation:**
Spliting the data into test and train sets, Data Scaling involved.

**Step 5 Machine Learning Model:**
the aim of step 5 to train Machine learning model on various model like Linear Regression, decision tree, random forest and svm to find the best model suits.

**Step 6 Conclusion :**
In conclusion stage which the generation capacity model is tested using unseen data.

**3 DATA INSIGHTS** 

There are some Key details found that follows:

![diab_page-0002](https://github.com/Jaydeep1-Chotaliya/Diabetes_Analysis/assets/129647680/52ff7c86-b35f-4663-8317-d57a12342c5d)


from above graph we can illustrate that a high glucose level indicates a person has more chance of diabetes.

In a real-life scenario Several factors can play a role in high glucose levels in people with diabetes. 

In a person without diabetes, the pancreas produces insulin, a hormone that helps cells absorb glucose from the bloodstream, thus regulating blood sugar levels. However, in individuals with diabetes, either the body doesn't produce enough insulin (Type 1 diabetes), or the insulin it does produce is not effectively used (Type 2 diabetes). They include food and physical activity, illness, and medications not related to diabetes.

![diab_page-0003](https://github.com/Jaydeep1-Chotaliya/Diabetes_Analysis/assets/129647680/7fe23bf2-c540-44d2-a68d-f1404e176f1f)

The Body Mass Index (BMI) is a metric that assesses body fat in relation to height and weight. To compute it, weight in kilograms is divided by the square of height in meters. An individual with a BMI of 25 or more is classified as overweight, while a BMI of 30 or more indicates obesity.

The graph shows elevated glucose levels in patients compared to the average glucose level, suggesting potential implications for the individuals' health.

**4 CONCLUSION**

In conclusion, after a comprehensive evaluation of four machine learning models for our classification problem, it is evident that the logistic regression model stands out as the best fit. Several factors contribute to this determination.

Firstly, logistic regression is known for its simplicity and interpretability, making it easy to understand and explain to stakeholders, aiding in decision-making processes. The model provides clear insights into the impact of each feature on the predicted outcome.

Secondly, logistic regression has demonstrated a **high accuracy model with 81% accuracy, 0.7 precision score, 0.63 recall, and 0.66 F1-score.**
