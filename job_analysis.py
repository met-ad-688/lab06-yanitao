import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams['font.size'] = 10

def plot_salary_by_employment_type(df):
    filtered_df = df[df['SALARY_FROM'] > 0]
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='EMPLOYMENT_TYPE_NAME', y='SALARY_FROM', data=filtered_df, palette='Set2')
    plt.title('Salary Distribution by Employment Type')
    plt.xlabel('Employment Type')
    plt.ylabel('Starting Salary')
    plt.tight_layout()
    plt.savefig('_output/q1_salary_by_employment_type.svg', format='svg')
    plt.close()

def plot_salary_distribution_by_industry(df):
    output_path = '_output/q2_salary_by_industry.svg'

    filtered_df = df[df['SALARY_FROM'] > 0].copy()

    plt.figure(figsize=(20, 12)) 
    sns.boxplot(
        x='NAICS2_NAME',
        y='SALARY_FROM',
        data=filtered_df,
        palette='cubehelix',
        showfliers=False
    )

    plt.title('Salary Distribution by Industry', fontsize=14)
    plt.xlabel('Industry', fontsize=12)
    plt.ylabel('Starting Salary', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_path, format='svg')
    plt.close()


def plot_job_trends_over_time(df):
    df['POSTED_DATE'] = df['POSTED'].dt.to_period('M')
    post_counts = df.groupby('POSTED_DATE').size().reset_index(name='Job Count')
    post_counts['POSTED_DATE'] = post_counts['POSTED_DATE'].astype(str)
    plt.figure(figsize=(12, 5))
    sns.lineplot(x='POSTED_DATE', y='Job Count', data=post_counts, marker='o', color='steelblue')
    plt.title('Job Posting Trends Over Time')
    plt.xlabel('Posted Date (Month)')
    plt.ylabel('Number of Job Postings')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('_output/q3_posting_trend.svg', format='svg')
    plt.close()

def plot_top_10_job_titles(df):
    top_titles = df['TITLE_NAME'].value_counts().nlargest(10).reset_index()
    top_titles.columns = ['TITLE_NAME', 'Job Count']
    plt.figure(figsize=(10, 6))
    sns.barplot(y='TITLE_NAME', x='Job Count', data=top_titles, palette='mako')
    plt.title('Top 10 Job Titles by Count')
    plt.xlabel('Job Count')
    plt.ylabel('Job Title')
    plt.tight_layout()
    plt.savefig('_output/q4_top_titles.svg', format='svg')
    plt.close()

def plot_remote_vs_onsite(df):
    remote_counts = df['REMOTE_TYPE_NAME'].value_counts().reset_index()
    remote_counts.columns = ['REMOTE_TYPE_NAME', 'Job Count']
    plt.figure(figsize=(6, 6))
    plt.pie(remote_counts['Job Count'], labels=remote_counts['REMOTE_TYPE_NAME'], autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title('Remote vs On-Site Job Postings')
    plt.tight_layout()
    plt.savefig('_output/q5_remote_vs_onsite.svg', format='svg')
    plt.close()

def plot_skill_demand_stacked(df):
    import ast
    df['SKILLS_NAME'] = df['SKILLS_NAME'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else [])
    exploded = df.explode('SKILLS_NAME')
    grouped = exploded.groupby(['NAICS2_NAME', 'SKILLS_NAME']).size().reset_index(name='Count')
    top_skills = grouped.groupby('SKILLS_NAME')['Count'].sum().nlargest(5).index
    filtered = grouped[grouped['SKILLS_NAME'].isin(top_skills)]

    pivot = filtered.pivot_table(index='NAICS2_NAME', columns='SKILLS_NAME', values='Count', fill_value=0)

    pivot.plot(kind='bar', stacked=True, figsize=(20, 12), colormap='tab20c')
    plt.xticks(rotation=45, ha='right') 
    plt.title('Top 5 Skill Demand by Industry')
    plt.ylabel('Skill Count')
    plt.xlabel('Industry')
    plt.tight_layout()
    plt.savefig('_output/q6_skill_stacked.svg', format='svg')
    plt.close()


def plot_salary_by_onet_type(df):
    onet_group = df.groupby('ONET_NAME').agg({
        'SALARY_FROM': 'median',
        'TITLE_NAME': 'count'
    }).reset_index().rename(columns={'SALARY_FROM': 'Median Salary', 'TITLE_NAME': 'Job Count'})
    plt.figure(figsize=(12, 6))
    plt.scatter(
        onet_group['ONET_NAME'], 
        onet_group['Median Salary'], 
        s=onet_group['Job Count'] * 0.2, 
        alpha=0.6, c=onet_group['Median Salary'], cmap='coolwarm'
    )
    plt.xticks(rotation=90)
    plt.title('Salary by ONET Occupation Type')
    plt.xlabel('ONET Type')
    plt.ylabel('Median Salary')
    plt.tight_layout()
    plt.savefig('_output/q7_onet_bubble.svg', format='svg')
    plt.close()

def plot_career_path_sankey(df):
    import plotly.graph_objects as go
    df_path = df[['SOC_2021_2_NAME', 'SOC_2021_3_NAME']].dropna()
    path_counts = df_path.groupby(['SOC_2021_2_NAME', 'SOC_2021_3_NAME']).size().reset_index(name='Count')
    all_nodes = list(set(path_counts['SOC_2021_2_NAME']) | set(path_counts['SOC_2021_3_NAME']))
    node_indices = {k: v for v, k in enumerate(all_nodes)}
    fig = go.Figure(data=[go.Sankey(
        node=dict(label=all_nodes),
        link=dict(
            source=path_counts['SOC_2021_2_NAME'].map(node_indices),
            target=path_counts['SOC_2021_3_NAME'].map(node_indices),
            value=path_counts['Count']
        )
    )])
    fig.write_image('_output/q8_career_sankey.svg') 


if __name__ == "__main__":
    df = pd.read_csv('_output/lightcast_cleaned.csv', parse_dates=['POSTED', 'EXPIRED', 'LAST_UPDATED_DATE'])
    plot_salary_by_employment_type(df)
    plot_salary_distribution_by_industry(df)
    plot_job_trends_over_time(df)
    plot_top_10_job_titles(df)
    plot_remote_vs_onsite(df)
    plot_skill_demand_stacked(df)
    plot_salary_by_onet_type(df)
    plot_career_path_sankey(df)