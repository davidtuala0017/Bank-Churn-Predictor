# 🏦 Bank Customer Churn Predictor

A machine learning web app that predicts whether a bank customer is likely to **leave (churn)** or **stay**, based on their profile. Built with Python, scikit-learn, and Streamlit.

### 🔗 Try the live app
**https://bank-churn-predictor-5sfigkzvwkqdkghdmygzjj.streamlit.app/**

Enter a customer's details (age, balance, country, activity, and more) and the app returns a churn risk percentage and a clear verdict.

---

## Why this matters (business value)

Keeping an existing customer is far cheaper than finding a new one. If a bank can spot **who is likely to leave before they go**, it can act early, for example with a better offer or a check-in call, and keep them. This project finds **who is at risk and why**, and turns it into a tool anyone can use.

---

## What I did

1. **Explored the data** to find what makes customers leave.
2. **Prepared the data** with pandas: dropped ID columns and converted text fields (country, gender) into numbers.
3. **Trained a Random Forest model** with scikit-learn on 80% of the data (8,000 customers) and tested it on the other 20% (2,000 customers).
4. **Tuned the model for the business goal.** The default model missed more than half of the customers who actually left (47% recall). By lowering the decision threshold to 0.30, I raised that to **70% of leavers caught**, accepting more false alarms in exchange. For a bank, missing a real leaver is far more costly than a false alarm, so this trade-off is worth it.
5. **Built and deployed a web app** with Streamlit so anyone can enter a customer's details and get a prediction.

---

## What I found

- **About 20% of customers churned** — a significant loss for any bank.
- **Age is the strongest predictor.** Customers who left averaged 45 years old versus 37 for those who stayed.
- **German customers left at about twice the rate** of customers in France or Spain (32% vs ~16%).
- **Inactive members left almost twice as often** as active ones (27% vs 14%).
- **Higher-balance customers left more**, meaning the bank was losing some of its most valuable customers.
- **Women churned more than men** (25% vs 16%).

Together these point to a clear action plan: focus retention on older, less-active, higher-value customers, especially in Germany.

---

## A note on precision vs. recall

Overall accuracy was about 87%, but accuracy alone is misleading here because only 20% of customers churned. The number that matters for the business is **recall on the "leaver" group** — how many of the real leavers the model catches. I deliberately optimized for that, which is why the final app flags customers at a 30% risk threshold rather than 50%.

---

## Tools used

- **Python** — core language
- **pandas** — data loading and preparation
- **scikit-learn** — Random Forest model and evaluation
- **Streamlit** — the interactive web app
- **joblib** — saving and loading the trained model

---

## About the data

This project uses a public **Bank Customer Churn** dataset, widely used for learning. It is **simulated data** built to resemble real bank customers — real customer data is private and legally protected, so, like most churn projects, this uses realistic practice data. The analysis and model would work the same way on a real bank's data.

---

## How it works

The app loads a pre-trained model (`churn_model.pkl`) and the expected column order (`model_columns.pkl`). When you enter a customer's details, it builds a single-row table in the same format the model was trained on, predicts the probability of churn, and shows the result using a 30% risk threshold.

---

*Built by David Tuala — Information Technology student at Texas Tech University.*
