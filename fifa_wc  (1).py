#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd

directory = 'Fifa_wc'
dataframes_list = []
for file in os.listdir(directory):
    if file.endswith('.csv'):
        df = pd.read_csv(os.path.join(directory, file))
        dataframes_list.append(df)


# In[2]:


df1 = dataframes_list[0]
df2 = dataframes_list[1]
df3 = dataframes_list[2]


# In[3]:


combined_df = pd.concat(dataframes_list, axis=0, join='outer', ignore_index=True)


# In[4]:


combined_df.head(5)


# In[5]:


import plotly.graph_objects as go
import pandas as pd

# load the data from the CSV file
df = pd.read_csv('Fifa_wc/WorldCups.csv')

fig = go.Figure(data=[go.Bar(name=country, x=df['Year'], y=df['GoalsScored'])
                       for country in df['Country'].unique()])

fig.update_layout(barmode='stack')

fig.show()


# In[6]:


import plotly.graph_objects as go
import pandas as pd

# load the data from the CSV file
df = pd.read_csv('Fifa_wc/WorldCups.csv')

fig = go.Figure(data=[go.Bar(name=country, x=df['Year'], y=df['MatchesPlayed'])
                       for country in df['Country'].unique()])

fig.update_layout(barmode='stack')

fig.show()


# In[7]:


import plotly.graph_objects as go
import pandas as pd

# load the data from the CSV file
df = pd.read_csv('Fifa_wc/WorldCups.csv')

fig = go.Figure(data=[go.Bar(name=country, x=df['Year'], y=df['QualifiedTeams'])
                       for country in df['Country'].unique()])

fig.update_layout(barmode='stack')

fig.show()


# In[8]:


import plotly.graph_objects as go
import pandas as pd

# load the data from the CSV file
df = pd.read_csv('Fifa_wc/WorldCups.csv')

# Create a list to store the data traces
data_traces = []

# Define the columns to be used for y-axis in each plot
y_columns = ['QualifiedTeams', 'MatchesPlayed', 'GoalsScored']

# Loop through the y_columns to create Bar traces for each plot
for y_col in y_columns:
    traces = [go.Bar(name=country, x=df['Year'], y=df[y_col]) for country in df['Country'].unique()]
    data_traces.extend(traces)

# Create the figure with the combined data traces
fig = go.Figure(data=data_traces)

# Update layout for stacked bars
fig.update_layout(barmode='stack')

# Show the figure
fig.show()


# In[9]:


import plotly.graph_objects as go
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('Fifa_wc/WorldCups.csv')

# Group by 'Year' and sum the values for each column
total_values = df.groupby('Year')[['GoalsScored', 'QualifiedTeams', 'MatchesPlayed']].sum()

# Create a list to store the data traces
data_traces = []

# Define the columns to be used for the y-axis in each plot
y_columns = ['QualifiedTeams', 'MatchesPlayed', 'GoalsScored']

# Loop through the y_columns to create Bar traces for each plot
for y_col in y_columns:
    traces = [go.Bar(x=total_values.index, y=total_values[y_col], name=y_col)]
    data_traces.extend(traces)

# Create the figure with the combined data traces
fig = go.Figure(data=data_traces)

# Update layout for stacked bars
fig.update_layout(barmode='stack')

# Show the figure
fig.show()


# In[10]:


import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv('Fifa_wc/WorldCups.csv')

# Group the data by winner and count the number of occurrences
grouped_data = df.groupby('Winner').size().reset_index(name='count')

# Create the pie chart
fig = px.pie(grouped_data, values='count', names='Winner', title='Winners by Category')

# Show the pie chart
fig.show()


# In[11]:


import pandas as pd
import plotly.express as px
df = pd.read_csv('Fifa_wc/WorldCups.csv')
fig = px.choropleth(df,
                   locations='Country',
                   locationmode='country names',
                   color='Attendance',
                   title='Attendance by Country',
                   color_continuous_scale=['blue'])
fig.show()


# In[12]:


import pandas as pd
import plotly.express as px

# Load the data from a CSV file
df = pd.read_csv('Fifa_wc/WorldCups.csv')

# Group by 'Country' and calculate the sum of counts
grouped_df = df.groupby('Country').size().reset_index(name='Count of Country')

# Create a bar chart using plotly express
fig = px.bar(grouped_df, x='Count of Country', y='Country', orientation='h', title='Count of Country by Country')

# Show the plot
fig.show()


# In[13]:


import pandas as pd
import plotly.express as px

# Load the data from a CSV file
df = pd.read_csv('Fifa_wc/WorldCupMatches.csv')

# Count the occurrences of each 'Home Team Name' per year
home_team_counts = df.groupby(['Year', 'Home Team Name']).size().reset_index(name='Home Team Count')

# Count the occurrences of each 'Away Team Name' per year
away_team_counts = df.groupby(['Year', 'Away Team Name']).size().reset_index(name='Away Team Count')

# Merge the two counts on 'Year'
merged_counts = pd.merge(home_team_counts, away_team_counts, how='outer', left_on=['Year', 'Home Team Name'], right_on=['Year', 'Away Team Name'])

# Fill NaN values with 0 and sum 'Home Team Count' and 'Away Team Count'
merged_counts['Total Count'] = merged_counts[['Home Team Count', 'Away Team Count']].sum(axis=1)

# Create a horizontal bar chart using plotly express
fig = px.bar(merged_counts, x='Total Count', y='Year', orientation='h', 
             title='Count of Matches per Year with Home and Away Teams')

# Show the plot
fig.show()


# In[14]:


import plotly.graph_objects as go
import pandas as pd

# Assuming your dataset is a CSV file named "WorldCups.csv"
df = pd.read_csv('Fifa_wc/WorldCups.csv')

# Select the columns you want to include in the table
columns_to_display = ['Winner', 'Runners-Up', 'Third', 'Year']

# Create a table with the selected columns
fig = go.Figure(data=[go.Table(header=dict(values=columns_to_display),
                               cells=dict(values=[df[col] for col in columns_to_display]))])

# Update layout to improve table aesthetics
fig.update_layout(title='FIFA World Cup Winners and Runners-Up')

# Display the table
fig.show()


# In[15]:


import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data from a CSV file
df_world_cups = pd.read_csv('Fifa_wc/WorldCups.csv')
df_world_cup_matches = pd.read_csv('Fifa_wc/WorldCupMatches.csv')

# Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("FIFA World Cup Dashboard"),
    
    # Bar chart 1: Goals Scored per Year
    dcc.Graph(
        id='goals-scored-per-year',
        figure=px.bar(df_world_cups, x='Year', y='GoalsScored', title='Goals Scored per Year')
    ),
    
    # Bar chart 2: Matches Played per Year
    dcc.Graph(
        id='matches-played-per-year',
        figure=px.bar(df_world_cups, x='Year', y='MatchesPlayed', title='Matches Played per Year')
    ),
    
    # Bar chart 3: Qualified Teams per Year
    dcc.Graph(
        id='qualified-teams-per-year',
        figure=px.bar(df_world_cups, x='Year', y='QualifiedTeams', title='Qualified Teams per Year')
    ),
    
    # Stacked Bar chart: Goals Scored, Matches Played, Qualified Teams per Year
    dcc.Graph(
        id='stacked-bar-chart',
        figure=go.Figure(data=[
            go.Bar(name='Goals Scored', x=df_world_cups['Year'], y=df_world_cups['GoalsScored']),
            go.Bar(name='Matches Played', x=df_world_cups['Year'], y=df_world_cups['MatchesPlayed']),
            go.Bar(name='Qualified Teams', x=df_world_cups['Year'], y=df_world_cups['QualifiedTeams'])
        ]).update_layout(barmode='stack')
    ),
    
    # Pie chart: Winners
    dcc.Graph(
        id='winners-pie-chart',
        figure=px.pie(df_world_cups['Winner'].value_counts().reset_index(), 
                      values='Winner', names='index', title='World Cup Winners')
    ),
    
    # Choropleth map: Attendance by Country
    dcc.Graph(
        id='choropleth-map',
        figure=px.choropleth(df_world_cups,
                             locations='Country',
                             locationmode='country names',
                             color='Attendance',
                             title='Attendance by Country',
                             color_continuous_scale=['blue'])
    ),
    
    # Bar chart: Count of Matches per Country
    dcc.Graph(
        id='matches-per-country-bar-chart',
        figure=px.bar(df_world_cup_matches.groupby('Home Team Name').size().reset_index(name='Count of Matches'),
                       x='Count of Matches', y='Home Team Name', orientation='h',
                       title='Count of Matches per Country')
    ),

    
    # Bar chart: Count of Matches per Year with Home and Away Teams
    dcc.Graph(
        id='matches-per-year-with-teams-bar-chart',
        figure=px.bar(merged_counts, x='Total Count', y='Year', orientation='h', 
                      title='Count of Matches per Year with Home and Away Teams')
    ),
    
    # Table: FIFA World Cup Winners and Runners-Up
    dcc.Graph(
        id='winners-and-runners-table',
        figure=go.Figure(data=[go.Table(header=dict(values=columns_to_display),
                                       cells=dict(values=[df_world_cups[col] for col in columns_to_display]))])
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




