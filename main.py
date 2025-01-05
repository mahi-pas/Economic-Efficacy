import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('MyData/final_dataset.csv')

# Create the plotly map
fig = px.choropleth(df, 
                    locations="State Code",  
                    locationmode="USA-states",
                    color="Income Minus Cost for 4",
                    hover_name="State",  # Updated to use a column that exists in the dataset
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Total Cost For Family Of 4 by State",
                    scope="usa",
                    )

# Show the map
fig.show()

