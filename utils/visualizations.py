import plotly.express as px

def create_plot(df, x_column, y_column, plot_type):
    if plot_type == "Line":
        fig = px.line(df, x=x_column, y=y_column, title=f"Line Plot of {y_column} vs {x_column}")
    elif plot_type == "Bar":
        fig = px.bar(df, x=x_column, y=y_column, title=f"Bar Chart of {y_column} vs {x_column}")
    elif plot_type == "Histogram":
        fig = px.histogram(df, x=x_column, title=f"Histogram of {x_column}")
    elif plot_type == "Pie":
        fig = px.pie(df, names=x_column, values=y_column, title=f"Pie Chart of {y_column} by {x_column}")
    elif plot_type == "Density":
        fig = px.density_heatmap(df, x=x_column, y=y_column, title=f"Density Heatmap of {y_column} vs {x_column}")
    else:
        fig = px.line(df, x=x_column, y=y_column, title="Default Line Plot")
    return fig
