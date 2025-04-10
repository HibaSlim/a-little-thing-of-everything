import pandas as pd
import numpy as np

'''purchases = pd.DataFrame({
    'customer_id': ['C1', 'C2', 'C1', 'C3', 'C2', 'C4', 'C1', 'C3', 'C5', 'C2'],
    'purchase_date': pd.to_datetime([
        '2024-01-05', '2024-01-06', '2024-02-15', '2024-02-20', '2024-03-01',
        '2024-03-05', '2024-04-01', '2024-04-10', '2024-04-12', '2024-04-20'
    ]),
    'amount': [100, 150, 80, 120, 130, 200, 90, 110, 70, 160]
})

signups = pd.DataFrame({
    'customer_id': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'signup_date': pd.to_datetime([
        '2024-01-01', '2024-01-04', '2024-02-01', '2024-03-01', '2024-04-01'
    ])
})

merge_data = purchases.merge(signups, on='customer_id')
print(merge_data)

merge_data['duration_since_signup'] = (merge_data['purchase_date']-merge_data['signup_date']).dt.days
print(merge_data)
retained = merge_data[merge_data['duration_since_signup'] <= 30]
print(retained)

retained_customer = retained['customer_id'].unique()
total_customers = signups['customer_id'].nunique()
retention_rate = len(retained_customer)/total_customers *100
print(retention_rate)

# extract the signup month and purchase month
merge_data['signup_month'] = merge_data['signup_date'].dt.to_period('M')
merge_data['purchase_month'] = merge_data['purchase_date'].dt.to_period('M')

# groupby signup month and perchase month to get the total amount/ revenue
#merged_table = merge_data.groupby(['signup_month','purchase_month'])['amount'].agg( total_rev = 'sum')

cohort_table = merge_data.groupby(['signup_month','purchase_month'])['amount'].sum().reset_index()

# reshape / transform / pivot the table use the sign_month values as index and purchase_month values as column names

cohort_pivot = cohort_table.pivot(index = 'signup_month', columns='purchase_month', values='amount').fillna(0)
print(cohort_pivot)

# average revenue per customer per signup cohort
total_revenue_per_cohort = merge_data.groupby('signup_month')['amount'].sum()
customer_count = merge_data.groupby('signup_month')['customer_id'].nunique()
avg_revenue_per_customer = (total_revenue_per_cohort/customer_count).sort_values(ascending=False)
print(avg_revenue_per_customer)

top_customer = merge_data.groupby('customer_id')['amount'].sum().sort_values(ascending=False).head(2)
print(top_customer)
'''

np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=90, freq='D')
data = pd.DataFrame({
    'date': np.random.choice(dates, 300),
    'store': np.random.choice(['Store_A', 'Store_B', 'Store_C', 'Store_D'], 300),
    'category': np.random.choice(['Electronics', 'Clothing', 'Groceries'], 300),
    'sales': np.random.randint(100, 1000, 300)
})

data['month'] = data['date'].dt.month # dt.to_period('M')
result = data.groupby(['month', 'category', 'store'])['sales'].mean().reset_index()
print(result)
data_pivot = result.pivot_table(index=['month','category'], columns='store', values= 'sales')
print(data_pivot)

#



