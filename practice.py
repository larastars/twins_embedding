import pandas as pd
from twins_embedding import TwinsEmbeddingModel
from twins_embedding import TwinsEmbeddingAnalysis
import pickle
from idrtools import Dataset, math
import os



# input to the model is a dictionary (from a pickle file) with the following keys
#'wave', 'mean_flux', 'color_law', 'phase_slope', 'phase_quadratic', 'phase_dispersion_coefficients', 'phase_range', 'gp_parameters', 'ref_coordinates', 'ref_values', 'ref_uncertainties'
# and have values of array 

#open the pickle file 
#with open('models/twins_embedding_1.pkl', 'rb') as f:
 #   data = pickle.load(f)

#print(data.keys())

#run analysis 
model = TwinsEmbeddingAnalysis()
a= model.load_dataset()
print(a)
model.run_analysis()
#model.dataset = Dataset.from_idr(
#     os.path.join(model.settings['idr_directory'], model.settings['idr']),
#      load_both_headers=True)

#model = TwinsEmbeddingModel()
#load the data into the model 
#model.__init__(data)

