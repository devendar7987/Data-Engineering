import pandas as pd
import numpy as np

rows = 1_000_000

# Customers
customers = pd.DataFrame({
    "customer_id" : range(rows),
    "name" : np.random.choice(["Sai", "Rakesh", "Amit", "Ajay"], rows),
    "city" : np.random.choice(["Hyderabad", "Delhi", "Mumbai"], rows)
})
customers.to_csv("customers.csv", index=False)



# Orders
orders = pd.DataFrame({
    "order_id" : range(rows),
    "customer_id" : np.random.randint(0, rows, rows),
    "amount" : np.random.randint(100, 5000, rows)
})
orders.to_csv("orders.csv", index=False)


# Payments
payments = pd.DataFrame({
    "payment_id" : range(rows),
    "order_id" : np.random.randint(0, rows, rows),
    "status" : np.random.choice(["SUCCESS", "FAILED"], rows)
})
payments.to_csv("payments.csv", index=False)