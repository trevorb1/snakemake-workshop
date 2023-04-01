"""This module sets the emission penalty"""

import sys
import pandas as pd

def main(input_csv: str, output_csv: str, start:float, end:float) -> None:
    """Sets a linear emission penalty 
    
    Args:
        input_csv: str, 
            path to EmissionPenalty.csv
        output_csv: str, 
            path to output csv file 
        start:float
            starting emission penalty 
        end:float
            ending emission penalty 
    """
    df = pd.read_csv(input_csv)
    start_year = df["YEAR"].min()
    end_year = df["YEAR"].max()
    try:
        slope = (end_year - start_year) / (end - start)
        df["VALUE"] = df["YEAR"].map(lambda x: start + (x - start_year) / slope)
    except ZeroDivisionError: 
        df["VALUE"] = 0
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python emission_penalty.py <input_emission_penalty> <output_emission_penalty> <starting_penalty> <ending_penalty>")
    else:
        main(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))