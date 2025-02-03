import os
import subprocess
from DataVisuals_CaseStudy.scripts.data_preprocessing import save_clean_data

save_clean_data()

path = str(os.path.abspath('../CaseStudyOstrica/DataVisuals_CaseStudy/scripts/interactive_dashboard.py'))

subprocess.run(["streamlit", "run", path])