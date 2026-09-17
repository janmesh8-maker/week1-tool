raw_minutes = input("How many minutes do you have available to study? ")

try:
    study_minutes = int(raw_minutes)
except ValueError:
    print(f"'{raw_minutes}' is not a valid number. Please enter a whole number.")
    raise SystemExit(1)

if not 1 <= study_minutes <= 480:
    print(f"{study_minutes} minutes is outside the sensible range (1 to 480 minutes).")
    raise SystemExit(1)

if study_minutes < 30:
    recommendation = "Quick review session."
elif study_minutes < 60:
    recommendation = "Focused study session."
elif study_minutes <= 120:
    recommendation = "Deep study session."
else:
    recommendation = "Long study session. Remember to take regular breaks."

print(f"You have {study_minutes} minutes available. Recommendation: {recommendation}")