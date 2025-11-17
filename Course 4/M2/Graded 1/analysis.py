import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load the dataset
df = pd.read_excel('graded_1_data.xlsx', index_col=0)

# Remove the university name column (index column is already excluded)
# The dataset should now only contain numeric and categorical columns

# Obtain descriptive statistics rounded to 2 decimal places
print("Descriptive Statistics:")
print(df.describe().round(2))
print("\n")

# Compute and display mean graduation rate before train:test split
if 'Grad.Rate' in df.columns:
    mean_grad_rate = round(df['Grad.Rate'].mean(), 2)
    print(f"Mean Graduation Rate (before split): {mean_grad_rate}")
else:
    print("Grad.Rate column not found in dataset.")

# Prepare the data
# One-hot encode the 'Private' variable with drop_first=True
df_encoded = pd.get_dummies(df, columns=['Private'], drop_first=True)

# Separate features and target
X = df_encoded.drop('Grad.Rate', axis=1)
y = df_encoded['Grad.Rate']

# Split the data into training and testing sets (70:30 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Output model coefficients rounded to 2 decimal places
coefficients = pd.Series(model.coef_, index=X.columns).round(2)
print("Model Coefficients:")
print(coefficients)

# { changed code }
# Identify categorical columns from the original dataframe (before get_dummies)
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
# Build list of prefixes used by get_dummies for those categorical columns (e.g., "Private_")
excluded_prefixes = [f"{col}_" for col in categorical_cols]

# Filter out encoded categorical predictors from X.columns
numeric_predictors = [col for col in X.columns if not any(col.startswith(prefix) for prefix in excluded_prefixes)]

if numeric_predictors:
    # coefficients is already rounded; select only numeric predictors
    numeric_coefs = coefficients.loc[numeric_predictors]
    top_predictor = numeric_coefs.idxmax()
    top_value = numeric_coefs.max()
    print(f"Highest coefficient (excluding categorical predictors): {top_predictor} = {top_value}")
else:
    print("No numeric predictors found after excluding categorical predictors.")
# { changed code }

intercept_rounded = round(model.intercept_, 2)
print(f"Intercept: {intercept_rounded}")
# { changed code }
print("\n")

# Obtain predictions on training and testing sets
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate metrics for training set
train_r2 = round(r2_score(y_train, y_train_pred), 2)
train_mse = round(mean_squared_error(y_train, y_train_pred), 2)
train_mae = round(mean_absolute_error(y_train, y_train_pred), 2)

# Calculate metrics for testing set
test_r2 = round(r2_score(y_test, y_test_pred), 2)
test_mse = round(mean_squared_error(y_test, y_test_pred), 2)
test_mae = round(mean_absolute_error(y_test, y_test_pred), 2)

# Display metrics
print("Training Set Metrics:")
print(f"R² (training): {train_r2}")
print(f"Mean Squared Error: {train_mse}")
print(f"Mean Absolute Error: {train_mae}")
print("\n")

print("Testing Set Metrics:")
print(f"R²: {test_r2}")
print(f"Mean Squared Error: {test_mse}")
print(f"Mean Absolute Error: {test_mae}")
