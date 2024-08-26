import ghhops_server as hs
import pandas as pd
import numpy as np
from flask import Flask
import logging
import os

# Initialize Flask and Hops
app = Flask(__name__)
hops = hs.Hops(app)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def clean_data(df):
    """Replace dashes with NaN and convert columns to numeric."""
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].replace('-', np.nan, inplace=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# maximum number of outputs
MAX_OUTPUTS = 25

FILENAME = 'joint_states.csv'


@hops.component(
    "/process_csv2",
    name="Process CSV",
    inputs=[],  # no inputs
    outputs=[
        hs.HopsString(f"Output{i+1}", f"O{i+1}", f"Data from column {i+1}", hs.HopsParamAccess.LIST)
        for i in range(MAX_OUTPUTS)
    ]
)
def process_csv():

    file_path = os.path.join(os.path.dirname(__file__), FILENAME)
    logger.debug(f"File path: {file_path}")

    df = pd.read_csv(file_path)
    df = clean_data(df)


    #output lists based on available columns
    output_data = [df[col].dropna().tolist() for col in df.columns]

    # number of outputs should not exceed the maximum number defined
    num_outputs = min(len(output_data), MAX_OUTPUTS)
    while len(output_data) < MAX_OUTPUTS:
        output_data.append([]) 

    return tuple(output_data[:MAX_OUTPUTS])

if __name__ == "__main__":
    app.run(debug=True)
