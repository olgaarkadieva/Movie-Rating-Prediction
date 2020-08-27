import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVR



train_data = pd.read_csv("train.csv")
train_data = np.asarray(train_data)
valid_data = pd.read_csv("validation.csv")
valid_data = np.asarray(valid_data)
genome_scores_data = pd.read_csv("genome_scores.csv")
genome_scores_data = np.asarray(genome_scores_data)
test_data = pd.read_csv("test.csv")
test_data = np.asarray(test_data)
# print("Data initialization")
