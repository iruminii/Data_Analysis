import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df.tail(1))

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(9,5))
    ax = df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', title='Rise in Sea Level', c='pink')
    ax.set_ylabel('Sea Level (inches)')
    # Create first line of best fit
    years_added = pd.Series(
    pd.date_range(start=str(df['Year'].iloc[-1] + 1), periods=2050-df['Year'].iloc[-1], freq="Y")
).dt.year 
    print('end of csv\n\n', df['Year'].tail())
    print('years_added\n\n', years_added)
    print('concat\n\n',pd.concat([df['Year'],years_added], ignore_index=True, axis=0))
    new_x = pd.concat([df['Year'],years_added], ignore_index=True, axis=0)
    bf_line = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    ax.plot(new_x, bf_line.intercept + bf_line.slope*new_x, c='cornflowerblue')

    # Create second line of best fit
    #start from 2000 
    print('newX', df.loc[df['Year'] > 1999, 'Year'].value_counts())
    print('newY', df.loc[df['Year'] > 1999, 'CSIRO Adjusted Sea Level'].value_counts())
    bf2 = linregress(x=df.loc[df['Year'] > 1999, 'Year'], y=df.loc[df['Year'] > 1999, 'CSIRO Adjusted Sea Level'])
    newx = pd.concat([df.loc[df['Year'] > 1999, 'Year'],years_added], ignore_index=True, axis=0)
    ax.plot(newx, bf2.intercept + bf2.slope*newx, c='lightgreen', label='From 2000')
    

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
