"""This module scales capital cost data"""

import sys
import pandas as pd

def main(input_csv: str, output_csv: str, technology:str, scaling_factor:float) -> None:
    """Scales capital cost data
    
    Args:
        input_csv: str, 
            path to input CapitalCosts.csv
        output_csv: str, 
            path to output csv file 
        technology:float
            technology to scale 
        scaling_factor:float
            factor to scale demand data by
    """
    df = pd.read_csv(input_csv)
    
    tech_df = df.loc[df["TECHNOLOGY"] == technology].copy()
    tech_df["VALUE"] = tech_df["VALUE"].mul(scaling_factor)

    df = pd.concat([df, tech_df]).drop_duplicates(subset=["REGION","TECHNOLOGY","YEAR"], keep="last")
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python capital_costs.py <input_capex_csv> <output_capex_csv> <technology> <scaling_factor>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]))