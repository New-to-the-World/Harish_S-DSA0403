import pandas as pd
def calculate_age_frequency(ages_list):
    age_freq = {}
    for age in ages_list:
        age_freq[age] = age_freq.get(age, 0) + 1
    return age_freq

def display_age_frequency_distribution(age_freq):
    print("Age\tFrequency")
    for age, freq in age_freq.items():
        print(f"{age}\t{freq}")

if __name__ == "__main__":
    customer_ages = [25, 30, 35, 25, 40, 30, 25, 35, 40, 45, 30, 25, 30]
    df=pd.DataFrame(customer_ages)
    print("Data Frame",df)
    print("Frequency Distribution")
    age_frequency = calculate_age_frequency(customer_ages)
    display_age_frequency_distribution(age_frequency)
