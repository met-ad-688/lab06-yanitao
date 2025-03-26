analysis_content = """
# Job Market Analysis Report

## Q1: Salary Distribution by Employment Type
![Q1 Salary Distribution by Employment Type](_output/q1_salary_by_employment_type.svg)
Full-time employment (more than 32 hours) shows a higher median starting salary compared to part-time roles. However, salary distributions for all employment types include significant outliers, indicating variation within each category.

## Q2: Salary Distribution by Industry
![Q2 Salary Distribution by Industry](_output/q2_salary_by_industry.svg)
Industries such as "Information" and "Professional, Scientific, and Technical Services" exhibit higher median starting salaries. In contrast, sectors like "Educational Services" and “Public Administration” tend to offer lower starting salaries, reflecting industry-based compensation differences.

## Q3: Job Posting Trends Over Time
![Q3 Job Posting Trends Over Time](_output/q3_posting_trend.svg)
Job postings decreased from May to July 2024, hitting a low point in July. However, there was a strong rebound in August and September, indicating renewed hiring activity towards the end of the quarter.

## Q4: Top 10 Job Titles by Count
![Q4 Top 10 Job Titles](_output/q4_top_titles.svg)
"Data Analysts" dominate the job postings with a significantly higher count than other titles, highlighting strong demand for data-focused roles. Roles like "Business Intelligence Analysts" and "Enterprise Architects" also appear frequently, suggesting ongoing needs in analytics and strategic IT planning.

## Q5: Remote vs On-Site Job Postings
![Q5 Remote vs On-Site Job Postings](_output/q5_remote_vs_onsite.svg)
A significant portion (73.2%) of job postings lack remote work classification, indicating incomplete labeling or on-site defaults. Among those labeled, 21.3% are remote roles, suggesting a moderate trend toward remote work but still a minority overall.

## Q6: Top 5 Skill Demand by Industry
![Q6 Top 5 Skill Demand by Industry](_output/q6_skill_stacked.svg)
Across industries, Communication, Data Analysis, and Management consistently rank among the top demanded skills. Particularly in “Professional, Scientific, and Technical Services” and “Finance and Insurance”, the demand for these core skills is significantly higher, indicating a strong emphasis on both interpersonal and analytical capabilities.

## Q7: Salary by ONET Occupation Type
![Q7 Salary by ONET Occupation Type](_output/q7_onet_bubble.svg)
The dataset shows only one ONET occupation type, Business Intelligence Analysts, with a median starting salary of around $88,000. The large bubble size reflects a high number of job postings, indicating both strong demand and a concentrated occupation type in this dataset.

## Q8: Career Pathway Trends
![Q8 Career Pathway Sankey](_output/q8_career_sankey.svg)
The Sankey diagram shows a single career transition from Computer and Mathematical Occupations to Mathematical Science Occupations.
"""

with open("_output/analysis.md", "w") as file:
    file.write(analysis_content)