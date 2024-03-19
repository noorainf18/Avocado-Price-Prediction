<p align="center"><img width=100% src="https://github.com/noorainf18/noorainf18/blob/main/Noorain%20Fathima%20-%20Banner.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# AVOCADO PRICE PREDICTOR

The objective of the "Forecasting Avocado Prices using Random Forest Regression and Grid Search Cross Validation" project is to develop an end-to-end machine learning solution for predicting the average price of avocados based on region and variety.

The project utilizes Random Forest Regression and Grid Search cross-validation techniques to build a predictive model. The aim is to achieve high accuracy in price predictions, as measured by Mean Squared Error (MSE).

Once the model is trained and optimized, it is deployed using Flask, a web framework for Python. The deployed model is accessible through a Flask API, allowing users to make predictions on new data by sending HTTP requests.

Overall, the project aims to provide a robust and scalable solution for forecasting avocado prices, which can be valuable for stakeholders in the avocado industry for decision-making and planning.


## Table of Contents

1. Data Description
2. Data Preprocessing
3. Cross Validation
4. Model Building
5. Results
6. Deployment
7. License


## Data Description

The dataset used for this project was taken from Kaggle and contains information about avocado prices, volume, and varieties.
- Date: The date of the recorded avocado price data.
- AveragePrice: The average price of avocados.
- Region: The region where the avocados were sold.
- Variety: The variety of avocados, which may include types such as Hass, Fuerte, or other varieties.
- Total Volume: The total volume of avocados sold.
- 4046: The total number of avocados with PLU 4046 sold.
- 4225: The total number of avocados with PLU 4225 sold.
- 4770: The total number of avocados with PLU 4770 sold.
- Total Bags: The total number of bags of avocados sold.
- Small Bags: The number of small bags of avocados sold.
- Large Bags: The number of large bags of avocados sold.
- XLarge Bags: The number of extra-large bags of avocados sold.


## Data Preprocessing

- Removing irrelevant columns
- Standardizing the dataset by renaming columns
- The Standard Scaler was applied to normalize the feature variables, ensuring all inputs have a mean of 0 and a standard deviation of 1.


## Cross Validation

Grid Search CV is a method for optimizing hyperparameters in a machine learning model. It aims to identify the optimal combination of hyperparameter values by systematically searching through a predefined set. The model's performance is evaluated using cross-validation at each combination.


## Model Building

Random Forest is an ensemble learning algorithm that operates by constructing a multitude of decision trees at training time and outputs the average prediction of the individual trees for regression tasks. It builds multiple trees and merges their predictions to improve the accuracy and control over-fitting.

The model's hyperparameters were optimized using Grid Search CV. The parameter grid included:
- n_estimators: [50, 100, 200]
- max_depth: [None, 10, 20, 30]
- min_samples_split: [2, 5, 10]
- min_samples_leaf: [1, 2, 4]

The model was fine-tuned to its optimal performance with the following parameters:
- max_depth: 30
- min_samples_leaf: 1
- min_samples_split: 2
- n_estimators: 200


## Results

The mean squared error (MSE) after tuning stood impressively low at 0.03, affirming the robustness of the predictive model.


## Deployment

Taking the model from development to deployment, Flask - a powerful web framework for Python - was utilized.


## License

MIT License

Copyright (c) 2024 Noorain Fathima

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
