import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb

def plot_correlation_heatmap(dataframe, selected_columns):
    correlation_matrix = dataframe[selected_columns].corr(numeric_only=True)
    plt.figure(figsize=(10, 6))
    sb.heatmap(data=correlation_matrix, vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.8)
    st.pyplot(plt)

def plot_pairplot(dataframe, selected_columns):
    pairplot_fig = sb.pairplot(data=dataframe, vars=selected_columns)
    st.pyplot(pairplot_fig)

def plot_histogram(dataframe, column):
    plt.figure(figsize=(10, 6))
    sb.histplot(dataframe[column], bins=30, kde=True)
    plt.title(f'Histogram of {column}')
    st.pyplot(plt)

def plot_scatter(dataframe, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sb.scatterplot(data=dataframe, x=x_column, y=y_column)
    plt.title(f'Scatter plot of {x_column} vs {y_column}')
    st.pyplot(plt)