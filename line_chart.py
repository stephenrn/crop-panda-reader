import pandas as pd
import matplotlib.pyplot as plt

# Set the backend to 'Agg' for headless environments
plt.switch_backend('Agg')

def read_data(file_path):
    data = pd.read_excel(file_path)
    return data

def get_top_regions(data, top_n=4):  # Default to top 4 regions
    data['Total'] = data.iloc[:, 1:].sum(axis=1)
    top_regions = data.nlargest(top_n, 'Total')
    return top_regions

def plot_line_chart(data):
    plt.figure(figsize=(12, 8))  # Adjust the figure size (width, height)
    years = data.columns[1:-1]  # Exclude the 'Total' column
    for index, row in data.iterrows():
        plt.plot(years, row.iloc[1:-1], label=row.iloc[0])
    
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Top Regions by Total Values Over Years')
    plt.legend()
    plt.savefig('line_chart_top_regions.png')  # Save the plot to a file
    print("Line chart saved as 'line_chart_top_regions.png'")

if __name__ == "__main__":
    file_path = '2E4EAHO0 (1).xlsx'  # Update this path to your actual data file
    data = read_data(file_path)
    top_regions = get_top_regions(data, top_n=4)  # Change the number here to get top N regions
    plot_line_chart(top_regions)
