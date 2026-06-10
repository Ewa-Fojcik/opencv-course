def get_inputs():
    height = float(input(f"whats your height"))
    weight = float(input(f"whats your weight"))
    return height, weight


def calculate_bmi(height_in_cm, weight_in_kg):
    bmi = weight_in_kg/((height_in_cm/100)**2)
    return round(bmi, 2)

height, weight = get_inputs()
bmi = calculate_bmi(height, weight)
print(f'your bmi is {bmi}')