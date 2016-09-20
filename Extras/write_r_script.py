import os
import pandas as pd
files = ["../SEModels/" + f for f in os.listdir("../SEModels") if ".txt" in f]
for file in files:
    df = pd.read_csv(file)
    nof = len(df.columns)
    print_name = file.split("/")[-1].split(".")[0]
    # print "get_landscape_features(\"~/GIT/ExploratoryLandscapeAnalysis/FeatureModels/" + print_name + ".csv\"," + str(nof) + ", \"~/GIT/ExploratoryLandscapeAnalysis/Result_FeatureModels/"+ print_name +".txt\")"
    print "get_landscape_features(\"~/GIT/ExploratoryLandscapeAnalysis/SEModels/" + print_name + ".txt\"," + str(nof) + ", \"~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/"+ print_name +".txt\")"
