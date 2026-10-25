# Project Scope: Australia Student Disposable Income Explorer

## 1. Project Overview

This project analyses disposable income for international students across five Australian cities: Melbourne, Sydney, Brisbane, Perth and Adelaide.

It combines wage data, rental prices and essential living expenses to show how employment type, working hours and living arrangements affect financial affordability.

Deliverables: an interactive Power BI dashboard, supported by Python data cleaning, SQL analysis and evidence-based recommendations.

## 2. Problem Statement

International students face different living costs and employment opportunities depending on where they live and work. A city with higher wages may also have higher rent and living expenses, so higher earnings do not necessarily mean higher disposable income.

This project identifies which cities and employment scenarios offer better financial affordability for international students.

## 3. Objectives

- Compare estimated income and essential living costs across five cities.
- Analyse income scenarios for four employment categories.
- Calculate estimated after-tax income and disposable income.
- Evaluate the impact of rent, working hours and living arrangements on affordability.
- Build an interactive dashboard to support data-informed decisions.
- Provide practical, evidence-based recommendations.

## 4. Target Users

- International students currently studying in Australia.
- Prospective international students comparing cities.
- Students budgeting while working part-time or casually.

## 5. Scope

### In Scope

- Cities: Melbourne, Sydney, Brisbane, Perth, Adelaide.
- Employment categories: Hospitality, Retail, Tutoring, Junior IT (subject to data availability; may be dropped if no defensible wage data exists).
- Wage, rental and essential living cost data collection.
- Estimated income tax under documented assumptions.
- Share-house vs living-alone comparison.
- Scenario modelling for working hours, rent and wage changes.
- Power BI dashboard, insights and recommendations.

### Out of Scope

- Guaranteeing job offers or individual earnings.
- Personalised tax, immigration or financial advice.
- Analysis of every suburb or occupation.
- Treating estimates as exact costs for every student.
- Advanced forecasting of future rents or wages.

## 6. Key Business Questions

1. Which city provides the highest estimated disposable income under comparable scenarios?
2. How does employment category affect a student's financial position?
3. What share of after-tax income goes to rent?
4. How would a 10% rent increase affect disposable income?
5. How do different working-hour scenarios affect affordability?
6. How do share-house and living-alone arrangements change the results?
7. Which city and living arrangement suits different student profiles best?

## 7. Data Sources

Credible, traceable sources are prioritised.

- Australian Bureau of Statistics (ABS): Employee Earnings and Hours, Consumer Price Index, household expenditure.
- Fair Work Ombudsman: casual pay rates under relevant modern awards (hospitality, retail).
- Jobs and Skills Australia: occupation and industry profiles.
- Study Australia: Cost of Living Calculator.
- Rental market reports and documented rental listings (e.g. Domain, SQM Research, state housing reports).
- Australian Taxation Office (ATO): tax rates and guidance.
- Department of Home Affairs: student visa work conditions and living cost requirements.
- OSHC provider pricing and public transport fare schedules.
- Additional documented sources for expenses not covered above.

For each dataset, record: source URL, download date, reference period, geographic coverage, units and known limitations. Data availability will be assessed before confirming final coverage.

## 8. Methodology

1. **Collect:** gather wage, rental and expense data from credible sources.
2. **Clean (Python/pandas):** standardise formats, handle missing values, check duplicates, validate quality.
3. **Integrate (SQL, SQLite or DuckDB):** join datasets by city, employment category and reference period.
4. **Model:** calculate gross income, after-tax income, living expenses and disposable income.
5. **Scenario analysis:** test alternative working-hour, rent and wage assumptions.
6. **Visualise (Power BI):** compare cities, employment categories and living arrangements.
7. **Recommend:** interpret results, identify key affordability drivers and give recommendations.

## 9. Key Metrics

- Estimated gross weekly income
- Estimated after-tax weekly income
- Weekly essential living costs
- Weekly and monthly disposable income
- Rent-to-net-income ratio
- Affordability gap against a defined budget target
- Change in disposable income under alternative scenarios

**Core calculation:**
Disposable Income = Income After Tax − Essential Living Expenses

Essential expenses may include rent, food, transport, utilities, phone/internet, OSHC and other documented items. A category is included only where a defensible estimate exists.

## 10. Scenario Modelling

- **Base case:** working hours within the current student visa limit (to be verified against Home Affairs guidance before finalising; currently 48 hours per fortnight).
- **Hypothetical sensitivity test:** higher weekly hours (e.g. 48 hours/week). This is not an assumption that such hours are permitted during study periods.
- Rent increase of 10%.
- Share house vs living alone.
- Changes in wage rates and essential living expenses.

Scenarios are interpreted as realistic options only after checking official visa work conditions.

## 11. Tools

- **Python / pandas:** cleaning and exploratory analysis
- **SQL (SQLite or DuckDB):** data integration and analytical queries
- **Power BI:** dashboard and scenario visualisation
- **GitHub:** version control and documentation

## 12. Deliverables

- Raw datasets and source register
- Cleaned datasets, data dictionary and data quality checks
- Reproducible Python notebooks
- SQL queries
- Interactive Power BI dashboard
- Report with insights and recommendations (8-10 pages)
- GitHub repository with documentation

## 13. Success Criteria

- Metrics have clear definitions and reproducible calculations.
- Sources, assumptions and reference periods are transparent.
- Comparisons use compatible geographic levels, periods and scenarios.
- Missing or unavailable data is explicitly identified.
- Scenario analysis shows how rent and working hours affect disposable income.
- The dashboard answers the key business questions.
- Recommendations are supported by analysis, not unsupported assumptions.

## 14. Limitations and Assumptions

- Wage and rental datasets may differ in geographic coverage, reference periods and population groups.
- National wage estimates may not represent city-level earnings.
- Occupation-level wages may not reflect casual student employment.
- Tax outcomes depend on individual circumstances; living costs vary by suburb and personal spending.
- Where city- or occupation-specific data is unavailable, the limitation is documented and the analysis uses a clearly labelled proxy or excludes the comparison.
- All results are estimates, not guaranteed financial outcomes.

## 15. Project Status

| Step | Status |
|---|---|
| Scope definition | Done |
| Repository setup | Done |
| Data collection | Not started |
| Data cleaning | Not started |
| Financial modelling | Not started |
| Dashboard | Not started |
| Report and publish | Not started |

**Next milestone:** collect the first wage dataset (Fair Work Ombudsman casual rates) and assess its suitability.
