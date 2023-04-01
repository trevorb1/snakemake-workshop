"""This module plots system level capacity"""

import sys
import pandas as pd

def main(annual_capacity: str, output_fig: str, scenario:str) -> None:
    """Scales variable cost data based on demand 
    
    Args:
        annual_capacity: str, 
            path to input AnnualCapacity.csv result
        output_csv: str, 
            path to save plot to
    """
    df = pd.read_csv(annual_capacity)
    df = df.loc[~(df["TECHNOLOGY"].str.startswith("MINE_"))]
    pt = df.pivot_table(
        index="YEAR",
        columns="TECHNOLOGY",
        values="VALUE"
    )
    ax = pt.plot(
        kind="bar",
        title=f"{scenario} Annual Capacity",
        ylabel="Capacity (GW)",
        xlabel="",
        stacked=True
    )
    ax.set_xticks(ax.get_xticks()[::5])
    fig = ax.get_figure()
    fig.savefig(output_fig)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python variable_costs.py <annual_capacity_csv> <output_fig> <scenario>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])