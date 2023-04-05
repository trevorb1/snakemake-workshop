Below are the steps to run the workflow manually from the root directory

1. mkdir scenarios

2. cp resources/data scenarios/data

3. python workflow/scripts/capital_costs.py scenarios/data/CapitalCosts.csv scenarios/data/CapitalCosts.csv "SPV" 1.5

4. python workflow/scripts/emission_penalty.py scenarios/data/EmissionsPenalty.csv scenarios/data/EmissionsPenalty.csv 0 100

5. python workflow/scripts/demand.py scenarios/data/SpecifiedAnnualDemand.csv scenarios/data/SpecifiedAnnualDemand.csv 2

6. python workflow/scripts/variable_costs.py scenarios/data/SpecifiedAnnualDemand.csv scenarios/data/VariableCosts.csv scenarios/data/VariableCosts.csv

7. otoole convert csv datafile scenarios/data scenarios/data.txt resources/config.yaml

8. mkdir scenarios/results

9. cd scenarios

10. glpsol -m ../resources/osemosys.txt -d scenarios/

11. cd ..

12. python plot_capacity.py scenarios/results/AnnualCapacity.csv scenarios/AnnualCapacity.png