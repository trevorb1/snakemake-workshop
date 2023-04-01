"""This module generates variable cost data"""

import sys
import pandas as pd

def main(input_demand: str, input_var_cost: str, output_csv: str) -> None:
    """Scales variable cost data based on demand 
    
    Args:
        input_demand: str, 
            path to input AnnualDemand.csv
        input_var_cost: str, 
            path to input VariableCosts.csv
        output_csv: str, 
            path to output csv file 
    """
    demand = pd.read_csv(input_demand)
    var_cost = pd.read_csv(input_var_cost)
    scaling_factor = demand["VALUE"].max() / demand["VALUE"].min()
    
    var_cost["VALUE"] = var_cost["VALUE"].mul(scaling_factor)
    var_cost.to_csv(output_csv, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python variable_costs.py <input_demand_csv> <input_variable_costs_csv> <output_variable_costs_csv>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])