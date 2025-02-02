# import os, sys, glob
# import pandas as pd
# import os
# # import numpy as np
# ####
# import matplotlib.pyplot as plt
# import seaborn as sns
from DataVisuals_CaseStudy.scripts.data_preprocessing import save_clean_data, preprocessing

customer_df, sales_df, quarterly_sales, monthly_sales, manager_sales, merged_df = preprocessing()