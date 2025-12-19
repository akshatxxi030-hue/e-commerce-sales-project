import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.colors as colors

 
df=pd.read_csv(r"D:\THIS PC\python workspace\Sample - Superstore.csv",encoding="Latin1")
df['Order Date']=pd.to_datetime(df["Order Date"])
df['Ship Date']=pd.to_datetime(df["Ship Date"])
df['Order month']=df["Order Date"].dt.month
df['order year']=df["Order Date"].dt.year
df['order week']=df["Order Date"].dt.dayofweek
print(df.head())

# Monthly Sales Analysis

monthly_sales=df.groupby("Order month")['Sales'].sum().reset_index()
#print(monthly_sales)


fig=px.line(monthly_sales,
            x='Order month',
            y='Sales',
            title='Monthly sales analysis')
fig.show()

# Sales by category

sales_by_category=df.groupby('Category')['Sales'].sum().reset_index()
print(sales_by_category)
fig2=px.pie(sales_by_category,
            names='Category',
            values='Sales',
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Pastel)
fig2.update_traces(textposition='inside',textinfo='percent+label')
fig2.update_layout(title_text='Sales analysis by category',title_font=dict(size=24))
fig2.show()

# Sales by Sub category

sales_by_sub_category=df.groupby('Sub-Category')['Sales'].sum().reset_index()
fig3=px.bar(sales_by_sub_category,x='Sub-Category',y='Sales',title='Sub category sales')
fig3.show()

# Monthly Profit

monthly_profit=df.groupby('Order month')['Profit'].sum().reset_index()

fig4=px.line(monthly_profit,x='Order month',y='Profit',title='Monthly profit')
             
fig4.show()

# Profit analysis by sub category
profit_by_sub_category=df.groupby("Sub-Category")["Profit"].sum().reset_index()
fig5=px.bar(profit_by_sub_category,x='Sub-Category',y='Profit',title='Profit analysis by sub category')
fig5.show()

