import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
social_media_data = pd.read_csv('Social_media_impact_on_life.csv')
print(social_media_data)
plt.plot(social_media_data, x = "Perceived_Stress_Score", y = "Academic_Performance_GPA")