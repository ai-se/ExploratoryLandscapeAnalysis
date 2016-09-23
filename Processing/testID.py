from __future__ import division
import pandas as pd
from intrinsicD import intrinsic_dimenstionality

filename = "../SEModels/MONRP_50_5_5_0_90-p1000-d50-o3-dataset.txt"

content = pd.read_csv(filename)
dcontent_subsample = content.sample(2000) if len(content) > 1000 else content.sample(len(content))


dcolumns = [c for c in content.columns if ">>" not in c]
ocolumns = [c for c in content.columns if ">>" in c]
ocontent = dcontent_subsample[ocolumns]

onorm = (ocontent - ocontent.min()) / (ocontent.max() - ocontent.min() + 0.000001 )

import pdb
pdb.set_trace()
print onorm
print intrinsic_dimenstionality(dcontent_subsample[dcolumns])
print intrinsic_dimenstionality(onorm)