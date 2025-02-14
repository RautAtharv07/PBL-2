# forms/calculations.py

class CarbonEmissionCalculator:
    """Calculator for estimating carbon emissions aligned with form parameters."""

    # Emission factors for different diet types (kg CO2 per meal)
    DIET_EMISSION_FACTORS = {
        'veg': 0.7,      # Vegetarian
        'non-veg': 1.7,  # Non-vegetarian
        'vegan': 0.5     # Vegan
    }

    # Vehicle emission factors (kg CO2 per km)
    VEHICLE_EMISSION_FACTORS = {
        'car': {
            'petrol': 0.192,
            'diesel': 0.171,
            'electric': 0.053
        },
        'bike': {
            'petrol': 0.103,
            'electric': 0.025
        },
        'bus': {
            'diesel': 0.082,
            'electric': 0.045
        },
        'train': {
            'electric': 0.041,
            'diesel': 0.074
        },
        'cycle': {
            'manual': 0
        }
    }

    # Waste emission factors (kg CO2 per kg waste)
    WASTE_EMISSION_FACTORS = {
        'biodegradable': 0.14,
        'non_biodegradable': 0.35,
        'recycled': 0.04
    }

    # Energy emission factors
    ENERGY_EMISSION_FACTORS = {
        'electricity': 0.82,  # kg CO2 per kWh
        'lpg': 2.983         # kg CO2 per kg of LPG
    }

    # Expenditure emission factor (kg CO2 per ₹1000)
    EXPENDITURE_EMISSION_FACTOR = 2.5

    @classmethod
    def calculate_dietary_emissions(cls, form_data):
        """
        Calculate annual dietary emissions based on form data.
        
        Args:
            form_data (dict): Contains height, weight, gender, diet_type, diet_frequency
        
        Returns:
            float: Annual emissions in kg CO2
        """
        try:
            height = float(form_data.get('height', 170))
            weight = float(form_data.get('weight', 70))
            gender = form_data.get('gender', 'M')
            diet_type = form_data.get('diet_type', 'non-veg')
            meals_per_day = int(form_data.get('diet_frequency', 3))

            # Calculate BMR using Mifflin-St Jeor equation
            bmr = (10 * weight) + (6.25 * height) - (5 * 30)  # Assuming age 30
            bmr += 5 if gender == 'M' else -161

            # Calculate TDEE with activity factor
            tdee = bmr * 1.2  # Assuming sedentary lifestyle
            
            # Get emission factor for diet type
            emission_factor = cls.DIET_EMISSION_FACTORS.get(diet_type, 1.0)
            
            # Calculate annual emissions
            daily_emissions = meals_per_day * emission_factor * (tdee / 2000)  # Scaling by TDEE
            annual_emissions = daily_emissions * 365
            
            return round(annual_emissions, 2)
        except Exception as e:
            print(f"Error in dietary emissions calculation: {e}")
            return 0

    @classmethod
    def calculate_travel_emissions(cls, form_data):
        """
        Calculate annual travel emissions based on form data.
        
        Args:
            form_data (dict): Contains vehicle_type, distance_travelled, fuel_type, frequency
        
        Returns:
            float: Annual emissions in kg CO2
        """
        try:
            vehicle_type = form_data.get('vehicle_type', 'car')
            distance = float(form_data.get('distance_travelled', 0))
            fuel_type = form_data.get('fuel_type', 'petrol')
            days_per_week = int(form_data.get('frequency', 1))

            if vehicle_type not in cls.VEHICLE_EMISSION_FACTORS:
                return 0

            # Get emission factor for vehicle and fuel type
            emission_factor = cls.VEHICLE_EMISSION_FACTORS[vehicle_type].get(fuel_type, 0)
            
            # Calculate annual emissions (distance per week * weeks in year * emission factor)
            annual_emissions = distance * days_per_week * 52 * emission_factor
            
            return round(annual_emissions, 2)
        except Exception as e:
            print(f"Error in travel emissions calculation: {e}")
            return 0

    # Emission factors (in kg CO2 per kg waste)
    WASTE_EMISSION_FACTORS = {
        'biodegradable': 0.1,  # kg CO2 per kg of biodegradable waste
        'non_biodegradable': 0.5  # kg CO2 per kg of non-biodegradable waste
    }
    BAG_SIZE_MAPPING = {
        'small': 2,       # Small bag ~2 kg
        'large': 5,       # Large bag ~5 kg
        'extra_large': 10 # Extra Large bag ~10 kg
    }

    @classmethod
    def calculate_waste_emissions(cls, form_data):
        
       
        try:
            # Get bag sizes
            bio_bag = form_data.get('biodegradable_waste_bags', 'small')
            non_bio_bag = form_data.get('non_biodegradable_waste_bags', 'small')

            # Convert bag size to waste weight
            bio_weight = cls.BAG_SIZE_MAPPING.get(bio_bag, 0)
            non_bio_weight = cls.BAG_SIZE_MAPPING.get(non_bio_bag, 0)

            # Calculate emissions
            bio_emissions = bio_weight * cls.WASTE_EMISSION_FACTORS['biodegradable']
            non_bio_emissions = non_bio_weight * cls.WASTE_EMISSION_FACTORS['non_biodegradable']

            total_emissions = bio_emissions + non_bio_emissions
            return round(total_emissions, 2)  # Rounded to 2 decimal places
        
        except Exception as e:
            print(f"Error in waste emissions calculation: {e}")
            return 0

    @classmethod
    def calculate_energy_emissions(cls, form_data):
        """
        Calculate annual energy emissions based on form data.
        
        Args:
            form_data (dict): Contains lpg_usage, electricity_bill
        
        Returns:
            float: Annual emissions in kg CO2
        """
        try:
            lpg_kg = float(form_data.get('lpg_usage', 0))
            electricity_bill = float(form_data.get('electricity_bill', 0))

            # Convert electricity bill to approximate kWh (assuming ₹7 per kWh)
            estimated_kwh = electricity_bill / 7

            # Calculate monthly emissions
            monthly_emissions = (
                lpg_kg * cls.ENERGY_EMISSION_FACTORS['lpg'] +
                estimated_kwh * cls.ENERGY_EMISSION_FACTORS['electricity']
            )
            
            # Convert to annual emissions
            annual_emissions = monthly_emissions * 12
            
            return round(annual_emissions, 2)
        except Exception as e:
            print(f"Error in energy emissions calculation: {e}")
            return 0

@classmethod
@classmethod
def calculate_expenditure_emissions(cls, form_data):
    try:
        # Extract user inputs
        essentials = float(form_data.get('essentials', 0))
        transport = float(form_data.get('transport', 0))
        lifestyle = float(form_data.get('lifestyle', 0))
        high_impact = float(form_data.get('high_impact', 0))

        # Emission factors (kg CO2 per ₹1000 spent) - Example values
        ESSENTIALS_EMISSION_FACTOR = 0.3   # Essentials (lower impact)
        TRANSPORT_EMISSION_FACTOR = 2.5   # Travel (higher impact due to flights)
        LIFESTYLE_EMISSION_FACTOR = 1.2   # Clothing, gadgets, etc.
        HIGH_IMPACT_EMISSION_FACTOR = 3.0  # Luxury & high-carbon purchases

        # Calculate emissions per category
        essentials_emissions = (essentials / 1000) * ESSENTIALS_EMISSION_FACTOR * 12
        transport_emissions = (transport / 1000) * TRANSPORT_EMISSION_FACTOR * 12
        lifestyle_emissions = (lifestyle / 1000) * LIFESTYLE_EMISSION_FACTOR * 12
        high_impact_emissions = (high_impact / 1000) * HIGH_IMPACT_EMISSION_FACTOR * 12

        # Total expenditure-based emissions
        total_emissions = (
            essentials_emissions + transport_emissions + 
            lifestyle_emissions + high_impact_emissions
        )

        return round(total_emissions, 2)

    except Exception as e:
        print(f"Error in expenditure emissions calculation: {e}")
        return 0


    @classmethod
    def calculate_carbon_footprint(cls, session_data):
        """
        Calculate total carbon footprint from all sources.
        
        Args:
            session_data (dict): All session data from forms
        
        Returns:
            dict: Detailed breakdown of emissions and total
        """
        try:
            # Calculate emissions for each category
            dietary = cls.calculate_dietary_emissions(session_data.get('personal_info', {}))
            travel = cls.calculate_travel_emissions(session_data.get('travel', {}))
            waste = cls.calculate_waste_emissions(session_data.get('waste', {}))
            energy = cls.calculate_energy_emissions(session_data.get('energy', {}))
            expenditure = cls.calculate_expenditure_emissions(session_data.get('expenditure', {}))

            # Calculate total emissions
            total = sum([dietary, travel, waste, energy, expenditure])

            # Return detailed breakdown
            return {
                'dietary_emissions': dietary,
                'travel_emissions': travel,
                'waste_emissions': waste,
                'energy_emissions': energy,
                'expenditure_emissions': expenditure,
                'total_emissions': round(total, 2),
                'breakdown_percentage': {
                    'dietary': round((dietary / total * 100) if total > 0 else 0, 1),
                    'travel': round((travel / total * 100) if total > 0 else 0, 1),
                    'waste': round((waste / total * 100) if total > 0 else 0, 1),
                    'energy': round((energy / total * 100) if total > 0 else 0, 1),
                    'expenditure': round((expenditure / total * 100) if total > 0 else 0, 1)
                }
            }
        except Exception as e:
            print(f"Error in total carbon footprint calculation: {e}")
            return {
                'dietary_emissions': 0,
                'travel_emissions': 0,
                'waste_emissions': 0,
                'energy_emissions': 0,
                'expenditure_emissions': 0,
                'total_emissions': 0,
                'breakdown_percentage': {
                    'dietary': 0,
                    'travel': 0,
                    'waste': 0,
                    'energy': 0,
                    'expenditure': 0
                }
            }