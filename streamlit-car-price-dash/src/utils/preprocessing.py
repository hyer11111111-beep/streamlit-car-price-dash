def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values
    df = df.fillna(method='ffill')
    
    return df

def transform_data(df):
    # Example transformation: Convert categorical variables to numerical
    df['Gender'] = df['Gender'].map({'여자': 0, '남자': 1})
    
    return df

def preprocess_data(df):
    df = clean_data(df)
    df = transform_data(df)
    
    return df