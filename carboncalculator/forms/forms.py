from django import forms

class PersonalInfoForm(forms.Form):
    height = forms.FloatField(label="Height (cm)")
    weight = forms.FloatField(label="Weight (kg)")
   # bmi = forms.FloatField(label="BMI", required=False)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    diet_type = forms.ChoiceField(choices=[('veg', 'Vegetarian'), ('non-veg', 'Non-Vegetarian'), ('vegan', 'Vegan')])
    diet_frequency = forms.IntegerField(label="Diet Frequency (meals per day)")



class TravelForm(forms.Form):
    VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('cycle', 'Bicycle'),
    ]
    days=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
    ]

    vehicle_type = forms.ChoiceField(choices=VEHICLE_CHOICES, label="Vehicle Type")
    distance_travelled = forms.FloatField(label="Distance Travelled (km per week)")
    fuel_type = forms.ChoiceField(
        choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')],
        label="Fuel Type (if applicable)",
        required=False  # Not all vehicles need fuel
    )
    frequency = forms.ChoiceField(choices=days, label="Days of Travel per Week")



class WasteForm(forms.Form):
    BAG_SIZE_CHOICES = [
        ('small', 'Small (~2 kg)'),
        ('large', 'Large (~5 kg)'),
        ('extra_large', 'Extra Large (~10 kg)'),
    ]

    biodegradable_waste_bags = forms.ChoiceField(
        choices=BAG_SIZE_CHOICES, 
        label="Biodegradable Waste Bag Size",
        required=True
    )
    non_biodegradable_waste_bags = forms.ChoiceField(
        choices=BAG_SIZE_CHOICES, 
        label="Non-Biodegradable Waste Bag Size",
        required=True
    )
    recycling_habit = forms.ChoiceField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        label="Do you recycle regularly?",
        required=True
    )


class EnergyForm(forms.Form):
    lpg_usage = forms.FloatField(label="LPG Usage (kg per month)")
    electricity_bill = forms.FloatField(label="Electricity Bill (₹ per month)")
    internet_data = forms.FloatField(label="Internet Data Usage (GB per month)")
    
    

class ExpenditureForm(forms.Form):
    ESSENTIALS_CHOICES = [
        ('groceries', 'Groceries & Food'),
        ('healthcare', 'Healthcare & Medicine'),
        ('education', 'Education & Books'),
        ('electricity', 'Electricity Bill'),
        ('water', 'Water Bill'),
        ('internet', 'Internet & Data Usage'),
    ]
    TRANSPORT_CHOICES = [
        ('public_transport', 'Public Transport'),
        ('ride_sharing', 'Ride Sharing (Uber, Ola, etc.)'),
        ('flights', 'Flights (Domestic & International)'),
        ('tourism', 'Hotel Stays & Tourism'),
    ]
    LIFESTYLE_CHOICES = [
        ('clothing', 'Clothing & Fashion'),
        ('electronics', 'Electronics & Gadgets'),
        ('furniture', 'Furniture & Appliances'),
        ('entertainment', 'Entertainment & Leisure'),
        ('luxury_goods', 'Luxury Goods & Jewelry'),
    ]

    essentials = forms.FloatField(label="Essentials & Daily Needs (₹)", required=True)
    transport = forms.FloatField(label="Transportation & Travel (₹)", required=True)
    lifestyle = forms.FloatField(label="Lifestyle & Luxury (₹)", required=True)
    high_impact = forms.FloatField(label="High-Impact Purchases (₹)", required=True)


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
