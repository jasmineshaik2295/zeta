import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Create the DataFrame with an additional 'city' column
data = {
    "customer_id": [1, 2, 3, 4],
    "gender": ["Male", "Female", "Female", "Male"],
    "city": ["New York", "Los Angeles", "New York", "Chicago"]
}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Initialize the OneHotEncoder
one_hot_encoder = OneHotEncoder(sparse_output=False)

# Specify the columns to encode
columns_to_encode = ["gender", "city"]

# Fit and transform the specified columns
encoded_data =one_hot_encoder.fit_transform(df[columns_to_encode])

# Get the names of the encoded columns
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)

# Create a DataFrame from the encoded data
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

# Display the encoded DataFrame
print("\nEncoded DataFrame:")
print(encoded_df)

# Optionally, you can concatenate the original DataFrame with the encoded DataFrame
final_df = pd.concat([df, encoded_df], axis=1)
print("\nFinal DataFrame with Encoded Columns:")
print(final_df) 