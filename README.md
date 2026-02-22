# Customer Churn Prediction - ChurnGuard AI

An end-to-end machine learning project that predicts customer churn for a telecom company. The system uses a Random Forest model that correctly identifies churn 78% of the time and provides practical business recommendations based on the predictions.

## Live Demo
[Deployed on Render](#) (Add your link after deployment)

## Project Overview
- **Goal**: Identify which customers are likely to churn
- **Dataset**: 7,043 customers with 21 different features
- **Model**: Random Forest (Gave the best results)
- **Accuracy**: 78%
- **Recall**: 72% (How well we catch actual churners)

## Tech Stack
- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **ML Libraries**: scikit-learn, pandas, joblib
- **Deployment**: Render (Free Tier)

## Features
- **Interactive Web Interface** - Simple form with organized tabbed sections
- **Real-time Predictions** - Get instant churn risk assessment
- **Business Recommendations** - Practical suggestions based on risk level
- **Clean Design** - Modern glassmorphism look with smooth animations
- **Mobile Responsive** - Works smoothly on phones, tablets, and desktops

## Model Performance
We tested three different models to find the best one:

| Model | ROC-AUC | Recall | Precision |
|-------|---------|--------|-----------|
| Logistic Regression | 0.845 | 53% | 69% |
| Random Forest | 0.841 | **72%** | 56% |
| XGBoost | 0.838 | 49% | 67% |

**Winner**: Random Forest - It catches the highest number of customers who actually end up churning, which is exactly what we want.

## Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/churn-predictor.git
cd churn-predictor
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Start the application**
```bash
uvicorn app:app --reload
```

4. **Open in browser**
```
http://localhost:8000
```

## Project Structure
```
churn-predictor/
├── model/
│   ├── churn_model_rf.pkl    # Trained Random Forest model
│   └── model_columns.pkl      # Feature names needed for predictions
├── templates/
│   └── index.html             # Frontend interface
├── app.py                      # FastAPI application
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

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
- Portfolio: [Your Portfolio Link]
- LinkedIn: [Your LinkedIn]
- GitHub: [Your GitHub]

## License
MIT License - Feel free to use and modify this project.

## Show your support
If you found this project helpful, consider giving it a star on GitHub.
