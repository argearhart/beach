# Find outliers in all numeric columns of a DataFrame using the Interquartile Range (IQR) method.
#    Parameters:
#    - df: A pandas DataFrame with numeric columns.
# Returns:
#  - outliers: A DataFrame with the same structure as the input, where each cell
#  is either the value (if not an outlier) or NaN (if an outlier).


import pandas as pd


def find_all_outliers(df):
    outliers = pd.DataFrame()
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        # Mark outliers as NaN or you can choose to mark them with any indicator
        outliers[column] = df[column].apply(
            lambda x: x if x >= lower_bound and x <= upper_bound else None)

    return outliers
