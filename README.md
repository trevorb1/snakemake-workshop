# Snakemake Workshop

This repository provides an example on how to implement a Snakemake workflow 
in an OSeMOSYS model. 

All workshop information can be found in the Jupyter Notebook, `workshop.ipynb`. 
Solutions to all examples are in the `workshop/solutions/` folder. 

The workflow has only been tested on Linux and UNIX machines. If you plan to 
run the code, install the conda environment using the command:

```bash
conda env create -f workflow/envs/env.yaml 
```

To view the Jupyter Notebook as slides, run the command

```bash 
jupyter nbconvert workshop.ipynb --to slides --post serve
```
