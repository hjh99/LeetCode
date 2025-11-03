# DataFrame products
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | quantity    | int    |
# | price       | int    |
# +-------------+--------+
# Write a solution to fill in the missing value as 0 in the quantity column.

# The result format is in the following example.

 

# Example 1:
# Input:+-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | None     | 135   |
# | WirelessEarbuds | None     | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+
# Output:
# +-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | 0        | 135   |
# | WirelessEarbuds | 0        | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+
# Explanation: 
# The quantity for Wristwatch and WirelessEarbuds are filled by 0.

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"]=products["quantity"].fillna(0)

    return products

# ** Pandas Helpful 💡**
# Handling NUll or NaN
# df.isnull() # boolean series of true & false
# df.notnull() # true if not null else false

# Dropping MISSING values
# df.dropna(inplace=True) # drops all rows have any cell NaN
# df.dropna(axis=1,inplace=True) # drops entire column if any cell is Nan

# Filling MISSING values
# df.fillna(0,inplace=True) # fill all the cells to 0 if missing
# df.interpolate() # fill value based on surrounding values