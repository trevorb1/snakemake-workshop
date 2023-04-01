"""This module scales demand data"""

import sys
import pandas as pd

def main(input_csv: str, output_csv: str, scaling_factor:float) -> None:
    """Scales annual demand data
    
    Args:
        input_csv: str, 
            path to input AnnualDemand.csv
        output_csv: str, 
            path to output csv file 
        scaling_factor:float
            factor to scale demand data by
    """
    df = pd.read_csv(input_csv)
    df["VALUE"] = df["VALUE"].mul(scaling_factor)
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python demand.py <input_demand_csv> <output_demand_csv> <scaling_factor>")
    else:
        main(sys.argv[1], sys.argv[2], float(sys.argv[3]))