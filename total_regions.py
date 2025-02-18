import pandas as pd

def read_data(file_path):
    data = pd.read_excel(file_path)
    # Sum the values across the years for each region
    data['Total'] = data.iloc[:, 1:].sum(axis=1)
    totals = dict(zip(data.iloc[:, 0], data['Total']))
    return totals

def print_totals(data):
    for region, total in data.items():
        print(f"Region: {region}, Total: {total}")

if __name__ == "__main__":
    file_path = '2E4EAHO0 (1).xlsx'  # Update this path to your actual data file
    data = read_data(file_path)
    print_totals(data)
