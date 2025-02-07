from django import forms

class PersonalInfoForm(forms.Form):
    height = forms.FloatField(label="Height (cm)")
    weight = forms.FloatField(label="Weight (kg)")
    bmi = forms.FloatField(label="BMI", required=False)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    diet_type = forms.ChoiceField(choices=[('veg', 'Vegetarian'), ('non-veg', 'Non-Vegetarian'), ('vegan', 'Vegan')])
    diet_frequency = forms.IntegerField(label="Diet Frequency (meals per day)")

class TravelForm(forms.Form):
    vehicle_type = forms.ChoiceField(choices=[('car', 'Car'), ('bike', 'Bike'), ('bus', 'Bus')])
    distance_travelled = forms.FloatField(label="Distance Travelled (km)")
    fuel_type = forms.ChoiceField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')])
    frequency = forms.IntegerField(label="Frequency (days per week)")

class WasteForm(forms.Form):
    biodegradable_waste = forms.FloatField(label="Biodegradable Waste (kg)")
    non_biodegradable_waste = forms.FloatField(label="Non-Biodegradable Waste (kg)")
    recycle_bag_size = forms.FloatField(label="Recycle Bag Size (kg)")

class EnergyForm(forms.Form):
    lpg_usage = forms.FloatField(label="LPG Usage (kg per month)")
    electricity_bill = forms.FloatField(label="Electricity Bill (₹ per month)")

class ExpenditureForm(forms.Form):
    expenditure = forms.FloatField(label="Monthly Expenditure (₹)")

def calculate_carbon_footprint(session_data):
    carbon_score = 0

    # Travel emissions (example)
    travel = session_data.get('travel', {})
    if travel:
        distance = float(travel.get('distance_travelled', 0))
        frequency = int(travel.get('frequency', 1))
        carbon_score += distance * frequency * 0.2  # Example emission factor

    # Waste emissions
    waste = session_data.get('waste', {})
    if waste:
        carbon_score += float(waste.get('biodegradable_waste', 0)) * 0.1

    # Energy emissions
    energy = session_data.get('energy', {})
    if energy:
        carbon_score += float(energy.get('electricity_bill', 0)) * 0.5

    return round(carbon_score, 2)  # Returning the final calculated value
