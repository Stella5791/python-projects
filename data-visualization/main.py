import csv 
import matplotlib.pyplot as plt

# Function to extract data from CSV file and generate a users dictionary
def extract_data_from_csv(filename):
    users_per_continent = {}
    # Open the CSV file & create a CSV reader object
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        # Iterate over each line in the CSV file to get continent and users from line
        for line in csvreader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])

           # ensure that every continent is initialized in the dictionary 
            if continent not in users_per_continent: 
                users_per_continent[continent] = {'population':[], 'year' : []}
            
          # store data for each continent by appending population/year values 
            users_per_continent[continent]['population'].append(population)
            users_per_continent[continent]['year'].append(year)
          
        return users_per_continent
        
# Function to generate data plots for each continent
def plot_users_data (users_per_continent):
    # Iterate over each continent in dictionary & extract users/year/continent data
    for continent in users_per_continent:
        population = users_per_continent[continent]['population']
        year = users_per_continent[continent]['year']
      
        # Create a line plot for the continent
        plt.plot(year, population, label=continent, marker='o')
    # Set the title and labels for the plot
    plt.title('Population of Users by Continent')
    plt.xlabel('Year')
    plt.ylabel('Internet users in billions')
    # Add a legend to the plot
    plt.legend()
    # Show the plot
    plt.show()
      
# File path for CSV data
filename = 'data.csv'

# Calling both functions
users_per_continent = extract_data_from_csv(filename)
plot_users_data(users_per_continent)

  