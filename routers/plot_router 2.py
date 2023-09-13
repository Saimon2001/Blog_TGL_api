from config.database import Session, engine, Base
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
from fastapi import FastAPI, Body, Depends, HTTPException, Path, Query, status, Request, BackgroundTasks, Response
from fastapi import APIRouter

plot_router = APIRouter()

#retriving data
query = f'SELECT * FROM users'
df = pd.read_sql(query, engine)

def create_plot():
    data = df
    fig = plt.figure()
    sns.countplot(x='country', data = df)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    plt.close(fig)
    return img_buf

@plot_router.get("/plot", tags=['plot'])
def plot_data(background_tasks: BackgroundTasks):
    """Plot the data from the API endpoint."""
    img_buf = create_plot()
    background_tasks.add_task(img_buf.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img_buf.getvalue(), headers=headers, media_type='image/png')
