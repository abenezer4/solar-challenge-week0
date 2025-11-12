Project Overview
This project performs data cleaning, exploratory data analysis (EDA), and cross-country comparison of solar irradiance and temperature data from three West African countries:
🇧🇯 Benin
🇸🇱 Sierra Leone
🇹🇬 Togo
The analysis investigates how irradiance (GHI, DNI, DHI) and temperature (Tamb, TModA, TModB) behave across regions and time — providing data-driven insights into solar energy potential and environmental variability.
Installation Guide
1. Clone this repository

cd solar-challenge-week0

2. Create and activate a virtual environment

For Windows (PowerShell):

python -m venv .venv
.venv\Scripts\Activate.ps1


For macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. (Optional) Set up Git pre-commit hooks

If you want to maintain formatting consistency:

pip install pre-commit
pre-commit install

🚀 How to Run the Project
A. Run the Jupyter notebooks

Launch Jupyter:

jupyter notebook


Open and run notebooks in order:

notebooks/benin_eda.ipynb

notebooks/sierraleone_eda.ipynb

notebooks/togo_eda.ipynb

notebooks/compare_countries.ipynb

The cleaned datasets will be automatically generated under /data.

B. Run via Streamlit (optional future extension)

A dashboard app can be added to visualize results interactively:

streamlit run app.py


(This feature is under development.)

📈 Results & Insights
Per-Country Observations
Country	Observation
Benin	High irradiance stability and strong correlation with temperature — excellent solar potential.
Sierra Leone	High variability due to rainy season and cloud interference — lower predictability.
Togo	Moderate and stable irradiance — reliable for consistent generation.
Statistical Summary

Z-score cleaning successfully removed statistical outliers.

ANOVA test confirmed significant differences in GHI across countries (p < 0.05).

Temperature variables (TModA, TModB, Tamb) followed irradiance closely, validating physical relationships.


👩‍💻 Author & Acknowledgments

Author: Abenezer Sileshi

Mentorship: 10 Academy
Challenge: Week 0 — Solar Data Discovery
Date: November 2025
