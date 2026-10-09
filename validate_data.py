import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

print("=" * 70)
print("VALIDAÇÃO DOS DADOS - F1")
print("=" * 70)

# ---------------------------------------------------------
# 1. PERÍODO DAS CORRIDAS
# ---------------------------------------------------------

races = pd.read_csv(DATA_DIR / "races.csv")

print("\nPERÍODO DOS DADOS")
print("-" * 70)

print(f"Primeiro ano: {races['year'].min()}")
print(f"Último ano:   {races['year'].max()}")

print(f"Quantidade de temporadas: {races['year'].nunique()}")
print(f"Quantidade de corridas:   {races['raceId'].nunique()}")

# ---------------------------------------------------------
# 2. VERIFICAÇÃO DAS CHAVES
# ---------------------------------------------------------

print("\nVERIFICAÇÃO DAS CHAVES")
print("-" * 70)

tables_keys = {
    "drivers": ("drivers.csv", "driverId"),
    "constructors": ("constructors.csv", "constructorId"),
    "circuits": ("circuits.csv", "circuitId"),
    "races": ("races.csv", "raceId"),
    "results": ("results.csv", "resultId"),
    "qualifying": ("qualifying.csv", "qualifyId"),
    "status": ("status.csv", "statusId")
}

for table, (filename, key) in tables_keys.items():

    df = pd.read_csv(DATA_DIR / filename)

    total = len(df)
    unique = df[key].nunique()
    duplicates = total - unique

    print(f"\n{table}")
    print(f"  Registros: {total:,}")
    print(f"  IDs únicos: {unique:,}")
    print(f"  IDs duplicados: {duplicates:,}")

# ---------------------------------------------------------
# 3. VALORES AUSENTES
# ---------------------------------------------------------

print("\nVALORES AUSENTES")
print("-" * 70)

for table in [
    "drivers",
    "constructors",
    "circuits",
    "races",
    "results",
    "qualifying",
    "status"
]:

    df = pd.read_csv(DATA_DIR / f"{table}.csv")

    missing = df.isna().sum()
    missing = missing[missing > 0]

    print(f"\n{table}:")

    if len(missing) == 0:
        print("  Nenhum valor ausente detectado.")
    else:
        for column, count in missing.items():
            print(f"  {column}: {count:,}")

print("\n" + "=" * 70)
print("VALIDAÇÃO CONCLUÍDA")
print("=" * 70)