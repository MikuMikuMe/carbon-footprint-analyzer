Creating a Python-based application to track and analyze carbon emissions can be a fulfilling project. For simplicity, this example will focus on tracking emissions based on common activities such as transportation, energy usage, and diet. The program will then suggest alternatives to reduce the carbon footprint. Here's a basic outline:

```python
import json

def get_carbon_emission(activity_type, activity_details):
    # Emission factors: assumed constants in kg CO2e
    emission_factors = {
        "transportation": {
            "car": 0.24,  # per km
            "bus": 0.05,  # per km
            "bicycle": 0, # per km
            "walk": 0     # per km
        },
        "energy": {
            "electricity": 0.45,  # per kWh
            "gas": 2.5,           # per therm
        },
        "diet": {
            "meat": 5.0,       # per serving
            "vegetarian": 2.0, # per serving
            "vegan": 1.5,      # per serving
        }
    }
    
    try:
        factor = emission_factors[activity_type]

        if isinstance(activity_details, dict):
            total_emission = sum(factor[key] * value for key, value in activity_details.items() if key in factor)
            return total_emission
        else:
            raise ValueError("Activity details should be a dictionary matching activity types to quantities.")
    except KeyError as e:
        print(f"Error: {e} is not a valid activity type.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def suggest_alternatives(activity_type):
    suggestions = {
        "transportation": "Consider walking, cycling, or using public transport to reduce emissions.",
        "energy": "Try to reduce energy consumption or use renewable energy sources.",
        "diet": "Consider reducing meat consumption and opting for plant-based alternatives."
    }
    return suggestions.get(activity_type, "No suggestions available for this activity type.")

def analyze_carbon_footprint(activities):
    total_emissions = 0
    for activity_type, activity_details in activities.items():
        emission = get_carbon_emission(activity_type, activity_details)
        if emission is not None:
            print(f"Total emissions for {activity_type}: {emission:.2f} kg CO2e")
            print(suggest_alternatives(activity_type))
            total_emissions += emission
    print(f"Overall total emissions: {total_emissions:.2f} kg CO2e")

def load_activities_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return {}

def main():
    filename = 'activities.json'  # You can change this file name as needed
    activities = load_activities_from_file(filename)
    if activities:
        analyze_carbon_footprint(activities)

if __name__ == "__main__":
    main()
```

### `activities.json` Example:
```json
{
    "transportation": {"car": 20, "bus": 10},
    "energy": {"electricity": 30},
    "diet": {"meat": 2, "vegetarian": 3}
}
```

### Program Explanation:
- **Emission Calculation**: The program calculates emissions using predefined factors for each activity type.
- **Suggestions**: It offers basic suggestions for reducing emissions.
- **JSON Input**: Activities are loaded from a JSON file, which allows flexible data input.
- **Error Handling**: It includes handling for common errors, including incorrect activity types and invalid file formats.

This basic script provides a structure you can build upon, adding more detailed activities, alternative suggestions, or even a user interface.