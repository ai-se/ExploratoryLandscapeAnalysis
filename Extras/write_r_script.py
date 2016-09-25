import os
import pandas as pd
# files = ["../SEModels/" + f for f in os.listdir("../SEModels") if ".txt" in f]
# files = ["../FeatureModels/" + f for f in os.listdir("../FeatureModels") if ".txt" in f]
files = ["../scalar_dataset/" + f for f in os.listdir("../scalar_dataset") if ".csv" in f]
for file in files:
    df = pd.read_csv(file)
    nof = len(df.columns)
    print_name = file.split("/")[-1].split(".")[0]
    print "get_landscape_features(\"~/GIT/ExploratoryLandscapeAnalysis/scalar_dataset/" + print_name + ".csv\"," + str(nof-1) + ',' + str(nof)  + ", \"~/GIT/ExploratoryLandscapeAnalysis/Result_scalar_dataset/"+ print_name + "\")"
    # print "get_landscape_features(\"~/GIT/ExploratoryLandscapeAnalysis/SEModels/" + print_name + ".txt\"," + str(nof) + ", \"~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/"+ print_name +".txt\")"
