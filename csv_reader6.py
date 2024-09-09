import ghhops_server as hs
import rhino3dm
import pandas as pd
from flask import Flask
import os

app = Flask(__name__)
hops = hs.Hops(app)

FILENAME = 'dynamixel-motor-positions.csv'

@hops.component(
    "/read_csv",
    name="Read CSV to Tree",
    description="Reads a CSV file and returns data as a tree structure",
    inputs=[
        hs.HopsBoolean("Refresh", "R", "Set to True to refresh data from CSV")
    ],
    outputs=[
        hs.HopsString("ColumnNames", "CN", "Names of all columns", hs.HopsParamAccess.LIST),
        hs.HopsNumber("DataTree", "DT", "Data from all columns as a tree", hs.HopsParamAccess.TREE)
    ]
)
def read_csv_to_tree(refresh=False):
    try:
        file_path = os.path.abspath(FILENAME)
        if not os.path.exists(file_path):
            return ["Error"], {0: [0.0]}

        df = pd.read_csv(file_path)
        column_names = df.columns.tolist()

        # dictionary to tree structure
        tree_dict = {}
        
        for i, col in enumerate(column_names):
            tree_dict[i] = df[col].astype(float).tolist()

        return column_names, tree_dict

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ["Error"], {0: [0.0]}

if __name__ == "__main__":
    app.run(debug=True)