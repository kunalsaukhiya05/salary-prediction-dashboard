# Salary Prediction Dashboard

A modern, interactive web dashboard for salary prediction and analytics using Streamlit and Machine Learning. Instantly predict your likely salary based on age, gender, education, job title, and work experience—or explore data insights, filter, and download results.  
**Impress interviewers or streamline HR analytics with just one click!**

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Screenshots](#screenshots)
- [How It Works](#how-it-works)
- [Setup & Installation](#setup--installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Modeling Details](#modeling-details)
- [Contributing](#contributing)
- [License](#license)

## Demo

Try the live app on your local machine.  
Predict salaries, visualize job trends, and download custom datasets in seconds.

## Features

- 🔍 **Powerful Filtering:** Slice & dice data by job title, gender, education, salary, age, or experience.
- 📊 **Analytics & Metrics:** Quickly view record count, average/maximum salary, and more.
- 📈 **Dynamic Visualizations:** Age distribution, salary vs. job, feature correlations.
- 🔮 **Salary Prediction:** Enter your details, get ML-powered annual salary prediction.
- 💾 **Export Options:** Download filtered data or predictions as CSV.
- 🏆 **Leaderboard:** See highest-paying jobs instantly.
- 🎉 **Modern UI:** Responsive tabs, sticky sidebar, attractive progress bars, and live toasts.

## Screenshots

1. **Correlation**

  ![Image Alt](https://github.com/kunalsaukhiya05/salary-prediction-dashboard/blob/72bb41b3b1f66fbe808039c13ed49b94dafbecb6/Salary_Prediction-main/images/Correlation.png )

  

2. **Distribution**

  ![Image Alt](https://github.com/kunalsaukhiya05/salary-prediction-dashboard/blob/72bb41b3b1f66fbe808039c13ed49b94dafbecb6/Salary_Prediction-main/images/Distribution.png )

  
  
3. **Feature_Importance**

  ![Image Alt]( https://github.com/kunalsaukhiya05/salary-prediction-dashboard/blob/72bb41b3b1f66fbe808039c13ed49b94dafbecb6/Salary_Prediction-main/images/Feature_Imp.png)

  
  
4. **Heatmap**

      ![Image Alt](https://github.com/kunalsaukhiya05/salary-prediction-dashboard/blob/72bb41b3b1f66fbe808039c13ed49b94dafbecb6/Salary_Prediction-main/images/Heatmap.png )

   

6. **Top10**

     ![Image Alt](https://github.com/kunalsaukhiya05/salary-prediction-dashboard/blob/72bb41b3b1f66fbe808039c13ed49b94dafbecb6/Salary_Prediction-main/images/Top10.png )

   

8. **Ed & gender_distribution**

      ![Image Alt](https://github.com/kunalsaukhiya05/salary-prediction-dashboard/blob/72bb41b3b1f66fbe808039c13ed49b94dafbecb6/Salary_Prediction-main/images/ed%26gender_distribution.png )

   

10. **ed_salary_gender**

      ![Image Alt](https://github.com/kunalsaukhiya05/salary-prediction-dashboard/blob/72bb41b3b1f66fbe808039c13ed49b94dafbecb6/Salary_Prediction-main/images/ed_salary_gender.png )

    

   

## How It Works

- Clean & preprocess the supplied salary dataset.
- Use a Random Forest model for robust and accurate regression prediction.
- Visualize key insights via Seaborn/Matplotlib charts.
- Streamlit powers the dynamic web dashboard with easy-to-adjust widgets.
- All prediction and analytics logic written in clean, readable Python.

## Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your_username/salary-prediction-dashboard.git
   cd salary-prediction-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Streamlit app**
   ```bash
   streamlit run app.py
   ```

4. **Open URL in your browser (auto-opens)**

## Project Structure

```
salary-prediction-dashboard/
│
├── app.py                # Streamlit dashboard (main file)
├── Salary_Data.csv       # Dataset (6700+ records)
├── requirements.txt      # All Python dependencies
├── images/               # Visualization assets
└── README.md             # You're here!
```

## Usage

- **Explore Data:** Use sidebar filters and "Data Preview" tab.
- **Visualize:** Switch to "Visualizations" for plots. Choose Age Distribution, Job Title vs. Salary, or Feature Correlation.
- **Analytics:** Check "Analytics" for summary stats and interactive metrics.
- **Predict:** Use "Salary Prediction" tab, enter your details, predict & download results.
- **Leaderboard:** The "Leaderboard" tab shows top earners in a snap.
- **Download:** All filtered data or your prediction can be exported as CSV.

## Modeling Details

- **Preprocessing:** Missing values dropped for reliable modeling.
- **Model:** RandomForestRegressor (best performing per R², MSE, MAE, RMSE)
- **Feature Importance:** Shown live in-app.
- **Metrics:** R², MSE, and MAE evaluated and available in analytics.
- **Why Random Forest?** Outperformed Decision Tree and Linear Regression for this dataset.

## Contributing

Pull requests welcome! Please create an issue for feature suggestions or bug fixes.

## License

MIT License.  
Free for personal, academic, or commercial use.

### Credits

- Dataset synthesised for demonstration/learning purposes.
- Built using Python, Pandas, Scikit-Learn, Streamlit, Matplotlib & Seaborn.

- 

**Star this repo if you found it helpful!  
Fork it for your own portfolio or HR application!**

