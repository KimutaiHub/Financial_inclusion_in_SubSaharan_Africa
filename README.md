
# Financial_inclusion_in_SubSaharan_Africa
=======
# Financial Inclusion & Household Economic Resilience (Kenya & Sub-Saharan Africa)

## Executive Summary
This project delivers an end-to-end machine learning solution to predict household financial inclusion (bank account ownership) and generate actionable segments for targeted interventions. It supports decision-making for banks, fintechs, insurers, government agencies, and NGOs by providing inclusion probability scores, interpretable drivers of inclusion/exclusion, and dashboard-ready outputs.

## Business Problem
A significant share of households in Sub-Saharan Africa remain unbanked, limiting access to savings, credit, payments, and financial resilience. Stakeholders need data-driven tools to:
- identify financially excluded households and prioritize outreach,
- understand the strongest barriers and enablers of inclusion,
- design targeted products and policies, and
- monitor inclusion programs with measurable indicators.

## Data
Household survey data across four countries:
- **Train:** 23,524 records (includes target)
- **Test:** 10,086 records (for scoring)
- **Countries:** Kenya, Rwanda, Tanzania, Uganda
- **Target:** `bank_account` (Yes/No)

Key predictors include:
- `location_type` (Urban/Rural)
- `cellphone_access` (Yes/No)
- `education_level`
- `job_type`
- `household_size`
- `age_of_respondent`
- `gender_of_respondent`
- `marital_status`
- `relationship_with_head`
- `year`
- `country`

Data quality note: no missing values were observed in training data.

## Methodology (CRISP-DM)
1. **Business Understanding:** stakeholder goals, success criteria, and use cases
2. **Data Understanding & EDA:** distribution checks, country comparison, class imbalance assessment
3. **Data Preparation:** target encoding, feature typing, preprocessing pipeline (one-hot encoding)
4. **Modeling:** Logistic Regression baseline + Random Forest benchmark
5. **Evaluation:** ROC-AUC, confusion matrix, precision/recall trade-offs, interpretability
6. **Deployment:** scoring pipeline, inclusion probability and segmentation outputs

## Modeling Results (Validation Set)
Two models were evaluated using a stratified validation split:

| Model | Accuracy | ROC-AUC | Notes |
|------|----------|---------|------|
| Logistic Regression | 0.89 | **0.864** | Selected production model (best AUC + interpretable) |
| Random Forest | 0.87 | 0.829 | Strong baseline, more false positives |

**Key performance insight:**  
Logistic Regression shows strong overall discrimination (ROC-AUC 0.864). Due to class imbalance (≈14% banked), the model is conservative in predicting the “banked” class; threshold tuning can increase recall depending on stakeholder priorities.

## Outputs
This project produces:
- **Inclusion probability score** for each household
- **Predicted class** (banked/unbanked) using a configurable threshold
- **Inclusion segments** (Very Low, Low, Medium, High) to support targeting
- **Dashboard-ready exports** for Excel/Tableau/Power BI
- **Saved production pipeline** (model + preprocessing)
