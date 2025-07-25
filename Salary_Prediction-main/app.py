import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Salary Prediction Dashboard", layout="wide", page_icon="💸")

# ----- Sidebar Branding & Information ----- #
st.sidebar.image("https://img.icons8.com/doodle/96/000000/money-bag.png", width=80)
st.sidebar.title("About the App")
st.sidebar.markdown("""
Modern interactive dashboard for salary prediction and analytics.
- Multiple filters and charts
- Download predictions & filtered data
- Discover insights and leaderboard
""")

# ----- Title and Description ----- #
st.title("💸 Salary Predictor Dashboard")
st.markdown("Use this tool to explore, filter, and predict salaries based on real-world data. Download results for further use!")

# ----- Data Loading Function ----- #
@st.cache_data
def load_data():
    df = pd.read_csv("Salary_Prediction-main/Salary_Data.csv")
    return df

df = load_data()

# ----- Sidebar Filters ----- #
st.sidebar.header("Filter Data")
job_options = ["All"] + sorted(df["Job Title"].dropna().unique())
education_options = ["All"] + sorted(df["Education Level"].dropna().unique())
gender_options = ["All"] + sorted(df["Gender"].dropna().unique())
salary_min, salary_max = int(df["Salary"].min()), int(df["Salary"].max())
age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
exp_min, exp_max = int(df["Years of Experience"].min()), int(df["Years of Experience"].max())

selected_job = st.sidebar.selectbox("Job Title", job_options)
selected_education = st.sidebar.selectbox("Education Level", education_options)
selected_gender = st.sidebar.selectbox("Gender", gender_options)
salary_range = st.sidebar.slider("Salary Range", min_value=salary_min, max_value=salary_max, value=(salary_min, salary_max))
age_range = st.sidebar.slider("Age Range", min_value=age_min, max_value=age_max, value=(age_min, age_max))
exp_range = st.sidebar.slider("Experience Range", min_value=exp_min, max_value=exp_max, value=(exp_min, exp_max))

# ----- Filtering Logic ----- #
filtered_df = df[
    ((df["Job Title"] == selected_job) | (selected_job == "All")) &
    ((df["Education Level"] == selected_education) | (selected_education == "All")) &
    ((df["Gender"] == selected_gender) | (selected_gender == "All")) &
    (df["Salary"].between(*salary_range)) &
    (df["Age"].between(*age_range)) &
    (df["Years of Experience"].between(*exp_range))
]

# ----- Main Tabs ----- #
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Data Preview", "Analytics", "Visualizations", "Salary Prediction", "Leaderboard"
])

# ----- Tab 1: Filtered Data Preview ----- #
with tab1:
    st.header("Filtered Data Preview")
    st.dataframe(filtered_df.head(20), use_container_width=True)
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Filtered Data (CSV)", data=csv_data, file_name="filtered_salary_data.csv")

# ----- Tab 2: Data Metrics / Analytics ----- #
with tab2:
    st.header("Data Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records", len(filtered_df))
    col2.metric("Average Salary", f"₹{int(filtered_df['Salary'].mean()):,}" if len(filtered_df)>0 else "–")
    col3.metric("Highest Salary", f"₹{int(filtered_df['Salary'].max()):,}" if len(filtered_df)>0 else "–")
    col4.metric("Average Experience", f"{filtered_df['Years of Experience'].mean():.1f} yrs" if len(filtered_df)>0 else "–")

# ----- Tab 3: Visualizations ----- #
with tab3:
    st.header("Interactive Visualizations")
    plot_opt = st.selectbox("Choose Visualization", ["Age Distribution", "Job Title vs Salary (Top 10)", "Feature Correlation"])
    if plot_opt == "Age Distribution":
        fig, ax = plt.subplots()
        sns.histplot(filtered_df["Age"].dropna(), kde=True, ax=ax, color='orange')
        ax.set_title("Age Distribution")
        st.pyplot(fig)
    elif plot_opt == "Job Title vs Salary (Top 10)":
        top_jobs = filtered_df.groupby("Job Title")["Salary"].mean().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots()
        sns.barplot(x=top_jobs.values, y=top_jobs.index, ax=ax, palette="Blues_r")
        ax.set_xlabel("Average Salary")
        ax.set_ylabel("Job Title")
        ax.set_title("Top 10 Highest Paying Jobs")
        st.pyplot(fig)
    elif plot_opt == "Feature Correlation":
        fig, ax = plt.subplots()
        corr = filtered_df.select_dtypes(include=np.number).corr()
        sns.heatmap(corr, annot=True, cmap='crest', ax=ax)
        st.pyplot(fig)

# ----- Tab 4: Salary Prediction and Download ----- #
with tab4:
    st.header("Predict Your Salary")
    with st.form("prediction_form"):
        age = st.slider("Your Age", age_min, age_max, int(np.median([age_min, age_max])))
        gender = st.selectbox("Gender", sorted(df["Gender"].dropna().unique()))
        edu = st.selectbox("Education Level", sorted(df["Education Level"].dropna().unique()))
        exp = st.slider("Years of Experience", exp_min, exp_max, int(np.median([exp_min, exp_max])))
        pred_btn = st.form_submit_button("Predict Salary")
    
    if pred_btn:
        # Model setup and label encoding
        data_no_na = df.dropna()
        le_gender = LabelEncoder()
        le_edu = LabelEncoder()
        data_no_na["Gender_enc"] = le_gender.fit_transform(data_no_na["Gender"])
        data_no_na["Edu_enc"] = le_edu.fit_transform(data_no_na["Education Level"])
        X = data_no_na[["Age", "Gender_enc", "Edu_enc", "Years of Experience"]]
        y = data_no_na["Salary"]
        rf = RandomForestRegressor(n_estimators=80, random_state=0)
        rf.fit(X, y)
        X_pred = np.array([[age, le_gender.transform([gender])[0], le_edu.transform([edu])[0], exp]])
        salary_pred = rf.predict(X_pred)[0]
        st.success(f"Your Estimated Salary: ₹{int(salary_pred):,} per year")
        
        pred_result = pd.DataFrame({
            'Age':[age], 'Gender':[gender], 'Education Level':[edu], 'Experience':[exp], 'Predicted Salary':[int(salary_pred)]
        })
        csv_pred = pred_result.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Prediction Result", data=csv_pred, file_name="salary_prediction.csv")
        st.balloons()

# ----- Tab 5: Leaderboard ----- #
with tab5:
    st.header("Top 10 Highest Salaries")
    st.dataframe(filtered_df.sort_values("Salary", ascending=False).head(10)[
        ["Job Title", "Education Level", "Gender", "Years of Experience", "Salary"]
    ].reset_index(drop=True))


