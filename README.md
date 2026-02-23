# Customer Churn Prediction - ChurnGuard AI

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-78%25-brightgreen)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Deployed-yellow)

An end-to-end machine learning project that predicts customer churn for a telecom company. The system uses a Random Forest model that correctly identifies churn 78% of the time and provides practical business recommendations based on the predictions.

## Live Demo
**[Click here to try the app!]((https://churn-guard.streamlit.app/))**
https://churn-guard.streamlit.app/

## Project Overview
- **Goal**: Identify which customers are likely to churn
- **Dataset**: 7,043 customers with 21 different features
- **Model**: Random Forest (Gave the best results)
- **Accuracy**: 78%
- **Recall**: 72% (How well we catch actual churners)

## Tech Stack
- **Frontend & Backend**: Streamlit (Python)
- **ML Libraries**: scikit-learn, pandas, joblib
- **Deployment**: Hugging Face Spaces (Free)

## Features
- **Interactive Web Interface** - Clean tabs to organize customer information
- **Real-time Predictions** - Instant churn risk assessment
- **Business Recommendations** - Practical suggestions based on risk level
- **Metrics Dashboard** - Key customer metrics at a glance
- **Mobile Responsive** - Works smoothly on all devices

## Model Performance
We tested three different models to find the best one:

| Model | ROC-AUC | Recall | Precision |
|-------|---------|--------|-----------|
| Logistic Regression | 0.845 | 53% | 69% |
| Random Forest | 0.841 | **72%** | 56% |
| XGBoost | 0.838 | 49% | 67% |

**Winner**: Random Forest - It catches the highest number of customers who actually end up churning, which is exactly what we want.


## Key Insights from Data Analysis
- Customers on **month-to-month contracts** are much more likely to leave
- **Fiber optic** internet users show higher churn rates compared to others
- How long someone has been with the company (**tenure**) is the strongest indicator of whether they'll stay
- People paying with **electronic check** tend to be at higher risk of churning

## Business Impact
- Spot at-risk customers early before they actually leave
- Save money on acquiring new customers by keeping existing ones
- Get more value from each customer over their lifetime
- Run smarter retention campaigns focused on the right people

## Developer
**M Fayaz Khan**
- GitHub: [@mfayazkhan50-AI](https://github.com/mfayazkhan50-AI)
- LinkedIn: [Muhammad Fayaz Khan](https://www.linkedin.com/in/muhammad-fayaz-khan-271487381/)

## License
MIT License - Feel free to use and modify this project.

## Show your support
If you found this project helpful, consider giving it a star on GitHub.
