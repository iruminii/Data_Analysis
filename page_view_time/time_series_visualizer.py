import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
#df = df.drop(df[df['value'] < df['value'].quantile(0.025)].index)
#df = df.drop(df[df['value'] > df['value'].quantile(0.975)].index)
df = df[(df['value'] >= df['value'].quantile(0.025))&(df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14,4))
    ax.plot(df)
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    fig, ax = plt.subplots(figsize=(14,10))
    missing = pd.DataFrame({'date':[pd.to_datetime('2016-01-01'), pd.to_datetime('2016-02-01'),pd.to_datetime('2016-03-01'),pd.to_datetime('2016-04-01')], 'value':[0,0,0,0]})
    
    df_bar = df.copy().reset_index()
    df_bar = pd.concat([missing, df_bar])
    #monthly['year'] = monthly.index.year
    df_bar['year'] = df_bar['date'].dt.strftime('%Y')
    df_bar['month'] = df_bar['date'].dt.strftime('%m')
    #monthly['month'] = monthly.index.month
    df_bar = (df_bar.groupby(['year','month'])['value'].mean().reset_index(drop=False))
    df_bar['month'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()

    # Draw bar plot
    fig = sns.catplot(data=df_bar, x='year', y='value', hue='month', kind='bar', palette=sns.color_palette(), legend_out=False)

    fig.set_ylabels('Average Page Views')
    fig.set_xlabels('Years')
    plt.legend(title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    print('box\n\n', df_box.head())
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=(25,5))

    sns.boxplot(data=df_box, x=df_box['year'],y=df_box['value'], ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')
    sns.boxplot(data=df_box, x=df_box['month'],y=df_box['value'], ax=ax[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
