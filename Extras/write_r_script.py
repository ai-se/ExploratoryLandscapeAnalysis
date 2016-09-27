import os
import pandas as pd

# files = ["../scalar_dataset/" + f for f in os.listdir("../scalar_dataset") if ".csv" in f]
# files = ["../scalar_dataset_SE/" + f for f in os.listdir("../scalar_dataset_SE") if ".csv" in f]
files = ["../scalar_dataset_SE/" + f for f in os.listdir("../scalar_dataset_SE_normalized") if ".csv" in f]
for file in files:
    df = pd.read_csv(file)
    nof = len(df.columns)
    print_name = file.split("/")[-1].split(".")[0]
    # print "get_landscape_features(\"~/GIT/ExploratoryLandscapeAnalysis/scalar_dataset/" + print_name + ".csv\"," + str(nof) + ',' + str(1)  + ", \"~/GIT/ExploratoryLandscapeAnalysis/Result_scalar_dataset/"+ print_name + "\")"
    print "get_landscape_features(\"~/GIT/ExploratoryLandscapeAnalysis/scalar_dataset_SE_normalized/" + print_name + ".csv\"," + str(nof) + ',' + str(1)  + ", \"~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels_normalized/"+ print_name + "\")"