import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

files = sorted(DATA_DIR.glob("*.csv"))

print("=" * 70)
print("F1 POWER BI - INSPEÇÃO DOS DADOS")
print("=" * 70)

for file in files:
    print(f"\n{'=' * 70}")
    print(f"ARQUIVO: {file.name}")
    print(f"{'=' * 70}")

    df = pd.read_csv(file)

    print(f"Linhas: {len(df):,}")
    print(f"Colunas: {len(df.columns)}")

    print("\nColunas:")
    for column in df.columns:
        print(f"  - {column}")

    print("\nPrimeiro registro:")
    print(df.head(1).to_string(index=False))