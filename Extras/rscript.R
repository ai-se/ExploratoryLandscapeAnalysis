get_landscape_features <- function(filename, indep_no, dep_no, result_file){
  set.seed(1)
  raw_dataset <- as.matrix(read.csv(filename))
  columns <- colnames(raw_dataset)
  length((raw_dataset))
  for (i in 1:10) {
    sample_dataset <- raw_dataset[sample(nrow(raw_dataset), size=100, replace=FALSE),]
    x <- sample_dataset[, columns[c(1:indep_no)]]
    y <- sample_dataset[, columns[c(dep_no)]]

    feat.object = createFeatureObject(X = x, y = y)
    results=list()
    results <- c(results, calculateFeatureSet(feat.object, set = "ela_distr"))
    results <- c(results, calculateFeatureSet(feat.object, set = "ela_meta"))
    results <- c(results, calculateFeatureSet(feat.object, set = "nbc"))
    results <- c(results, calculateFeatureSet(feat.object, set = "ic"))
    lapply(results, write, paste(result_file,(dep_no-indep_no), '_', i,".txt",   sep = ""), append=TRUE)}}

library(flacco)
# The following calls can be generated from ./rscript.R

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_100-p1000-d50-o3-dataset.txt",50, 51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_100-p1000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_100-p1000-d50-o3-dataset.txt",50, 52, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_100-p1000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_100-p1000-d50-o3-dataset.txt",50, 53, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_100-p1000-d50-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_110-p1000-d50-o3-dataset.txt",50, 51,, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_110-p1000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_110-p1000-d50-o3-dataset.txt",50, 52,, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_110-p1000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_110-p1000-d50-o3-dataset.txt",50, 53, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_110-p1000-d50-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_120-p10000-d50-o3-dataset.txt",50, 51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_120-p10000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_120-p10000-d50-o3-dataset.txt",50, 52, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_120-p10000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_120-p10000-d50-o3-dataset.txt",50, 53, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_120-p10000-d50-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_90-p1000-d50-o3-dataset.txt",50, 51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_90-p1000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_90-p1000-d50-o3-dataset.txt",50, 52, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_90-p1000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_0_90-p1000-d50-o3-dataset.txt",50, 53, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_0_90-p1000-d50-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_5_120-p10000-d50-o3-dataset.txt",50, 51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_5_120-p10000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_5_120-p10000-d50-o3-dataset.txt",50, 52, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_5_120-p10000-d50-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/MONRP_50_5_5_5_120-p10000-d50-o3-dataset.txt",50, 53, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/MONRP_50_5_5_5_120-p10000-d50-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_0_100-p10000-d50-o1-dataset.txt",50,5, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_0_100-p10000-d50-o1-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_0_110-p10000-d50-o1-dataset.txt",50,51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_0_110-p10000-d50-o1-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_0_120-p10000-d50-o1-dataset.txt",50,51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_0_120-p10000-d50-o1-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_0_90-p10000-d50-o1-dataset.txt",50,51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_0_90-p10000-d50-o1-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_5_100-p1000-d50-o1-dataset.txt",50,51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_5_100-p1000-d50-o1-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_5_110-p1000-d50-o1-dataset.txt",50,51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_5_110-p1000-d50-o1-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_5_120-p1000-d50-o1-dataset.txt",50,51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_5_120-p1000-d50-o1-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_5_80-p1000-d50-o1-dataset.txt",50,51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_5_80-p1000-d50-o1-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/NRP_50_5_5_5_90-p1000-d50-o1-dataset.txt",50,51, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/NRP_50_5_5_5_90-p1000-d50-o1-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3A-p10000-d9-o3-dataset.txt",9,10, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3A-p10000-d9-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3A-p10000-d9-o3-dataset.txt",9,11, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3A-p10000-d9-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3A-p10000-d9-o3-dataset.txt",9,12, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3A-p10000-d9-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3B-p10000-d9-o3-dataset.txt",9,10,"~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3B-p10000-d9-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3B-p10000-d9-o3-dataset.txt",9,11,"~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3B-p10000-d9-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3B-p10000-d9-o3-dataset.txt",9,12,"~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3B-p10000-d9-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3C-p10000-d9-o3-dataset.txt",9,10, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3C-p10000-d9-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3C-p10000-d9-o3-dataset.txt",9,11, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3C-p10000-d9-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3C-p10000-d9-o3-dataset.txt",9,12, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3C-p10000-d9-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3D-p10000-d9-o3-dataset.txt",9,10, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3D-p10000-d9-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3D-p10000-d9-o3-dataset.txt",9,11, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3D-p10000-d9-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/POM3D-p10000-d9-o3-dataset.txt",9,12, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/POM3D-p10000-d9-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_all-p10000-d27-o3-dataset.txt",27,28, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_all-p10000-d27-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_all-p10000-d27-o3-dataset.txt",27,29, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_all-p10000-d27-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_all-p10000-d27-o3-dataset.txt",27,30, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_all-p10000-d27-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_flight-p10000-d27-o3-dataset.txt",27,28, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_flight-p10000-d27-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_flight-p10000-d27-o3-dataset.txt",27,29, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_flight-p10000-d27-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_flight-p10000-d27-o3-dataset.txt",27,30, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_flight-p10000-d27-o3-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_ground-p10000-d27-o4-dataset.txt",27,28, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_ground-p10000-d27-o4-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_ground-p10000-d27-o4-dataset.txt",27,29, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_ground-p10000-d27-o4-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_ground-p10000-d27-o4-dataset.txt",27,30, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_ground-p10000-d27-o4-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_osp-p10000-d27-o4-dataset.txt",27,28, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_osp-p10000-d27-o4-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_osp-p10000-d27-o4-dataset.txt",27,29, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_osp-p10000-d27-o4-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomo_osp-p10000-d27-o4-dataset.txt",27,30, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomo_osp-p10000-d27-o4-dataset")

get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomoo2-p10000-d27-o3-dataset.txt",27,28, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomoo2-p10000-d27-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomoo2-p10000-d27-o3-dataset.txt",27,29, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomoo2-p10000-d27-o3-dataset")
get_landscape_features("~/GIT/ExploratoryLandscapeAnalysis/SEModels/xomoo2-p10000-d27-o3-dataset.txt",27,30, "~/GIT/ExploratoryLandscapeAnalysis/Result_SEModels/xomoo2-p10000-d27-o3-dataset")


