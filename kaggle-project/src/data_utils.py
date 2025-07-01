def split_numerical_categorical(df):
    """
    Splits the columns of a DataFrame into numerical and categorical features.

    Parameters:
    df (pandas.DataFrame): The DataFrame to split.

    Returns:
    tuple: A tuple containing two lists - numerical columns and categorical columns.
    """
    numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=['number']).columns.tolist()
    return numerical_cols, categorical_cols
