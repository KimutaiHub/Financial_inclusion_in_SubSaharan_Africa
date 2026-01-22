import pandas as pd
from pathlib import Path

train_path = Path("data_raw/Train.csv")
test_path = Path("data_raw/Test.csv")
vardef_path = Path("data_raw/VariableDefinitions.csv")

for p in [train_path, test_path, vardef_path]:
    if not p.exists():
        raise FileNotFoundError(f"Missing required file: {p.resolve()}")

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)
vardef = pd.read_csv(vardef_path)

print("=== SHAPES ===")
print("Train:", train.shape)
print("Test :", test.shape)
print("VarDef:", vardef.shape)

print("\n=== COLUMNS (first 30) ===")
print(train.columns.tolist()[:30])

# Identify target column
target = "bank_account" if "bank_account" in train.columns else train.columns[-1]
print("\n=== TARGET COLUMN ===")
print("Target:", target)
print(train[target].value_counts(dropna=False))

print("\n=== MISSINGNESS (top 15) ===")
missing = train.isna().mean().sort_values(ascending=False).head(15)
print((missing * 100).round(2).astype(str) + "%")

print("\n=== DUPLICATES ===")
print("Duplicate rows:", int(train.duplicated().sum()))

if "country" in train.columns:
    kenya = train[train["country"].astype(str).str.lower() == "kenya"]
    print("\n=== KENYA SUBSET ===")
    print("Kenya rows:", kenya.shape[0])
    if kenya.shape[0] > 0:
        print("Kenya target distribution:")
        print(kenya[target].value_counts(normalize=True).round(4))
else:
    print("\nNo 'country' column found in Train.csv (cannot filter Kenya here).")
