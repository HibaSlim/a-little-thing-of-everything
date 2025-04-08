import pandas as pd

purchases = pd.DataFrame({
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

print(purchases)
print(signups)

merged = purchases.merge(signups, on='customer_id')
print(merged)
merged['Duration_after_signup'] =(merged['purchase_date']-merged['signup_date']).dt.days
print(merged)


retained =merged[merged['Duration_after_signup']<=30]
print(retained)
retained_customers = retained['customer_id'].unique()
print(retained_customers)
signups_customers = signups['customer_id'].nunique()
print(signups_customers)
retention_rate=len(retained_customers)/signups_customers*100
print(retention_rate)




