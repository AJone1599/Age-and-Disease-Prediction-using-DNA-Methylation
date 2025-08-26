import pandas as pd
import h5py
import numpy as np
import gc
import sys

gse_list = sys.argv[3:]
in_dir = sys.argv[2]
output = sys.argv[1]
methylation = None

print("Getting Site List")
for gse_name in gse_list:
 
    gse_methylation = pd.read_csv(F"{in_dir}/{gse_name}_methylation.csv", index_col = 0, usecols=[0])

    # gets first data frame from csv file
    if methylation is None:
        methylation = gse_methylation

    # get methylation pairs 
    methylation = pd.concat([methylation,gse_methylation], axis = 1, join="outer")

    del gse_methylation # reduces memory load
    gc.collect()


print(methylation.head)
print("saving")
methylation.index.to_series().to_csv(output, index = False, header = False)