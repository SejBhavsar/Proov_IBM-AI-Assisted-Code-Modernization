# analyze.py
# SUMMARY: Kilometers since service, average daily mileage, and vehicle load factor are the primary predictors of breakdowns.
# Total odometer mileage and vehicle age do not predict breakdown risk, as both broken and healthy cars share nearly identical averages.

import pandas as pd

# 1. Load dataset
df = pd.read_csv("fleet_history.csv")

# 2. Compare groups
broken = df[df["broke_down"] == 1]
ok = df[df["broke_down"] == 0]

print("=" * 77)
print("FLEET BREAKDOWN FACTOR COMPARISON")
print("=" * 77)
print(f"{'Feature':<20} {'Broke Down (Mean)':<20} {'Did Not Break Down (Mean)':<25} {'Predictive?':<12}")
print("-" * 77)

for col in ["odometer_km", "km_since_service", "avg_daily_km", "load_factor", "age_years"]:
    b_mean = broken[col].mean()
    ok_mean = ok[col].mean()
    diff_pct = abs(b_mean - ok_mean) / ok_mean * 100
    predictive = "YES" if diff_pct > 20 else "NO"
    print(f"{col:<20} {b_mean:<20.2f} {ok_mean:<25.2f} {predictive:<12}")

# 3. Build a simple risk score (0 to 100) using only the separating columns:
# km_since_service, avg_daily_km, load_factor
df["norm_km"] = df["km_since_service"] / df["km_since_service"].max()
df["norm_daily"] = df["avg_daily_km"] / df["avg_daily_km"].max()
df["norm_load"] = df["load_factor"] / df["load_factor"].max()

df["risk_score"] = ((df["norm_km"] + df["norm_daily"] + df["norm_load"]) / 3) * 100

# 4. Rank the cars by risk, highest first, and print the top 10
top_10 = df.sort_values(by="risk_score", ascending=False).head(10)
print("\n" + "=" * 77)
print("TOP 10 RISKIEST CARS (RANKED BY RISK SCORE)")
print("=" * 77)
print(top_10[["car_id", "risk_score", "km_since_service", "avg_daily_km", "load_factor", "broke_down"]].to_string(index=False))
