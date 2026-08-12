# Concrete Compressive Strength Prediction

This repository contains a Predictive Machine Learning system built using **Supervised regression (Random Forest Regressor)** to predict the compressive strength of concrete based on its ingredients and age. It is completed as part of the **Codetech IT Solutions** Machine Learning Internship.

## Project Structure
```
concrete_strength_prediction/
│
├── data/
│   └── concrete.csv                    # Raw dataset containing ingredient volumes & age
│
├── README.md                           # Project documentation
├── download_data.py                    # Script to download raw dataset
├── concrete_strength_prediction.ipynb  # Jupyter notebook with EDA, Pipeline, and regression modeling
└── concrete_strength_pipeline.pkl      # Serialized trained model pipeline
```

## Dataset Specifications
* **Total Instances:** 1,030 mixtures
* **Features Selected ($X$):**
  * `cement` (kg in a m3 mixture)
  * `slag` (blast furnace slag, kg in a m3 mixture)
  * `ash` (fly ash, kg in a m3 mixture)
  * `water` (kg in a m3 mixture)
  * `superplastic` (superplasticizer, kg in a m3 mixture)
  * `coarseagg` (coarse aggregate, kg in a m3 mixture)
  * `fineagg` (fine aggregate, kg in a m3 mixture)
  * `age` (time in days, 1 to 365)
* **Target ($y$):** `strength` (Concrete Compressive Strength in MPa)

## Methodology & Pipeline
1. **Train-Test Split:** Split the dataset into 80% training data and 20% testing data.
2. **Standardization:** Employed `StandardScaler` to normalize feature dimensions to a uniform scale.
3. **Pipeline Construction:** Bundled preprocessing and model training using scikit-learn `Pipeline` to enforce strict isolation against data leakage.
4. **Estimator:** Fitted a `RandomForestRegressor(random_state=42)` as the core predictive regressor.
5. **Model Tuning:** Conducted a `GridSearchCV` evaluation with 3-fold cross validation. The default baseline estimator parameters proved to provide optimal generalization characteristics.
6. **Results & Performance Metrics:**
   * **Mean Absolute Error (MAE):** 3.73 MPa (On average, predictions differ by 3.73 MPa from true value)
   * **Root Mean Squared Error (RMSE):** 5.46 MPa
   * **R² Score (Coefficient of Determination):** 0.8842 (Explains 88.42% of the variance)

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
2. Download the data:
   ```bash
   python download_data.py
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook concrete_strength_prediction.ipynb
   ```
