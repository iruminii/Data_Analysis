import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
#df = pd.read_csv('medical_examination.csv', index_col=0)
df = pd.read_csv('medical_examination.csv')
print(df.head())
# Add 'overweight' column
df['overweight'] = df[['weight', 'height']].apply(lambda x: (1 if (x[0]/(x[1]/100)**2) > 25 else 0), axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: (0 if x == 1 else 1))
df['gluc'] = df['gluc'].apply(lambda x: (0 if x== 1 else 1))
#df['cholesterol'] = 0 if df.loc[df['cholesterol'] == 1] else 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.dropna().melt(id_vars='cardio', value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
    print(df_cat)
  
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    # Draw the catplot with 'sns.catplot()'
    fig, ax = plt.subplots(figsize=(12,7))

    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', kind='count')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])&(df['height'] >= df['height'].quantile(0.025))&(df['height'] <= df['height'].quantile(0.975))&(df['weight'] >= df['weight'].quantile(0.025))&(df['weight'] <= df['weight'].quantile(0.975))]
    print('hear\n', df_heat.head())
    # Calculate the correlation matrix
    corr = round(df_heat.corr(), 1)
    print('corr', corr)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,7))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidth=.5, square=True, annot=True, annot_kws={"fontsize":8}, mask=mask)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
