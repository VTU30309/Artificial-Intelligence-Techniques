facts = [
    "john_is_cold.",
    "raining.",
    "john_Forgot_His_Raincoat.",  
    "fred_lost_his_car_keys.",    
    "peter_footballer."
]

def verify_fact(fact):
    fact = fact.rstrip(".").lower()  # Convert to lowercase for consistent checking
    if fact == "john_forgot_his_raincoat":
        return True
    elif fact == "raining":
        return True
    elif fact == "foggy":
        return

