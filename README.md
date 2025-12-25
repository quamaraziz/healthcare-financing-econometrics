Deciphering Healthcare Financing: Income, Spending, and OOP Burdens
This project investigates how national wealth (GDP) and government policy effort influence the financial burden of healthcare on households across 38 OECD countries over a 23-year period (2000–2023).

🚀 Project Overview
The core objective is to determine if higher national income effectively reduces Out-of-Pocket (OOP) expenses for citizens and to analyze the impact of high-income economic outliers on global trends.

Key Research Questions:
Do high-spending or high-income countries show lower OOP burdens?

How does government policy effort (supply-side financing) offset household-level payments?

How do structural economic outliers skew healthcare financing patterns?

🛠 Tech Stack & Data Engineering
Language: Python 3.x

Data Acquisition: Automated extraction via wbgapi (World Bank) and pandasdmx (OECD SDMX).

Data Wrangling: Extensive use of Pandas for melting, unpivoting, and cleaning 20+ years of panel data (800+ observations).

Statistics & Econometrics: * Univariate and Distributional Analysis (Skewness testing).

LOWESS Regression (Locally Weighted Scatterplot Smoothing).

Panel data modeling using statsmodels and linearmodels.

📊 Key Findings
The 4–8% Rule: Most OECD nations allocate between 4% and 8% of their GDP to healthcare.

Spending Efficiency: While higher GDP generally correlates with lower household burdens, government health expenditure as a % of GDP is the primary factor in insulating citizens from costs.

Outlier Insights: 75% of countries fall below ~$46K GDP per capita; countries exceeding this threshold exhibit structurally different financing patterns.

📁 Repository Structure
EwPY_Quamar_Aziz_2788342.ipynb: Full analytical pipeline from data extraction to visualization.

oecd_health_panel_raw.csv: Extracted and cleaned panel dataset.

📈 Visualizations
The analysis includes:

Distribution histograms for GDP and Healthcare Spending.

Scatter plots with LOWESS smoothing to identify non-linear trends in household burdens.
