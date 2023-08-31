import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    """
    Logic works the same

    1. We can drop duplicates first
    2. Sort or find out the nlargest values
    3. Identify the second largest or else None
    4. Create new Dataframe for it
    """

    """Solution 1"""
    second_highest = None
    unique = employee['salary'].drop_duplicates()
    if len(unique) > 1:
        second_highest = unique.nlargest(2).iloc[1]

    return pd.DataFrame({"SecondHighestSalary": [second_highest]})

    """Solution 2"""
    second_highest = None
    unique = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(unique) > 1:
        second_highest = unique.iloc[1]

    return pd.DataFrame({"SecondHighestSalary": [second_highest]})