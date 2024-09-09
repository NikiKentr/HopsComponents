import ghhops_server as hs
import pandas as pd
import numpy as np
from flask import Flask
import logging
import os

app = Flask(__name__)
hops = hs.Hops(app)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

FILENAME = 'joint_states.csv'

def clean_data(df):
    """Replace dashes with NaN and convert columns to numeric."""
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].replace('-', np.nan, inplace=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

@hops.component(
    "/process_csv2",
    name="Process CSV2",
    description="Reads a CSV file, cleans the data, and returns it as a tree structure",
    inputs=[
        hs.HopsBoolean("Refresh", "R", "Set to True to refresh data from CSV")
    ],
    outputs=[
        hs.HopsString("ColumnNames", "CN", "Names of all columns", hs.HopsParamAccess.LIST),
        hs.HopsNumber("DataTree", "DT", "Data from all columns as a tree", hs.HopsParamAccess.TREE)
    ]
)
def process_csv(refresh=False):
    try:
        file_path = os.path.join(os.path.dirname(__file__), FILENAME)
        logger.debug(f"File path: {file_path}")
        
        if not os.path.exists(file_path):
            logger.error(f"Error: The file {FILENAME} does not exist.")
            return ["Error"], {0: [0.0]}

        df = pd.read_csv(file_path)
        df = clean_data(df)
        
        column_names = df.columns.tolist()
        
        # dictionary to tree structure
        tree_dict = {}
        
        for i, col in enumerate(column_names):
            tree_dict[i] = df[col].dropna().tolist()

        logger.debug("Data processing completed successfully")
        return column_names, tree_dict

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return ["Error"], {0: [0.0]}

if __name__ == "__main__":
    app.run(debug=True)
