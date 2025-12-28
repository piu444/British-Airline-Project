import matplotlib.pyplot as plt

import pandas as pd
from sqlalchemy import create_engine

# Create SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://root:@localhost/airline_project')

# Method 1: Read entire table
df = pd.read_sql_table('ba_reviews', engine)

# Method 2: Read with custom query
df = pd.read_sql_query("SELECT * FROM ba_reviews", engine)



# # Show info
# print("\nDataset Info:")
# print(f"Shape: {df.shape}")
# print(f"Columns: {df.columns.tolist()}")

# Close connection
engine.dispose()

df = pd.read_sql_query("SELECT avg(rating) FROM ba_reviews", engine)
print(df)


