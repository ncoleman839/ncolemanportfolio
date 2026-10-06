#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_media_impact_on_life.csv')
sorted_data = data.sort_values(by="Daily_Usage_Hours")
filtered_data = sorted_data[sorted_data["Primary_Platform"].str.contains('Snapchat', na=False)]
fig, ax = plt.subplots()
coef = np.polyfit(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"], 1)
polynom = np.poly1d(coef)
ax.scatter(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"])
ax.set_xlabel("Daily Usage in Hours")
ax.set_ylabel("Hours Spent Sleeping")
plt.plot(filtered_data["Daily_Usage_Hours"], polynom(filtered_data["Daily_Usage_Hours"]), "r--", linewidth=2, label="Trendline")
ax.set_title("Comparison between Sleep and Daily Usage of Snapchat")
plt.legend()
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_media_impact_on_life.csv')
sorted_data = data.sort_values(by="Daily_Usage_Hours")
filtered_data = sorted_data[sorted_data["Primary_Platform"].str.contains('YouTube', na=False)]
fig, ax = plt.subplots()
coef = np.polyfit(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"], 1)
polynom = np.poly1d(coef)
ax.scatter(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"])
ax.set_xlabel("Daily Usage in Hours")
ax.set_ylabel("Hours Spent Sleeping")
plt.plot(filtered_data["Daily_Usage_Hours"], polynom(filtered_data["Daily_Usage_Hours"]), "r--", linewidth=2, label="Trendline")
ax.set_title("Comparison between Sleep and Daily Usage of YouTube")
plt.legend()
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_media_impact_on_life.csv')
sorted_data = data.sort_values(by="Daily_Usage_Hours")
filtered_data = sorted_data[sorted_data["Primary_Platform"].str.contains('TikTok', na=False)]
fig, ax = plt.subplots()
coef = np.polyfit(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"], 1)
polynom = np.poly1d(coef)
ax.scatter(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"])
ax.set_xlabel("Daily Usage in Hours")
ax.set_ylabel("Hours Spent Sleeping")
plt.plot(filtered_data["Daily_Usage_Hours"], polynom(filtered_data["Daily_Usage_Hours"]), "r--", linewidth=2, label="Trendline")
ax.set_title("Comparison between Sleep and Daily Usage of TikTok")
plt.legend()
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_media_impact_on_life.csv')
sorted_data = data.sort_values(by="Daily_Usage_Hours")
filtered_data = sorted_data[sorted_data["Primary_Platform"].str.contains('Instagram', na=False)]
fig, ax = plt.subplots()
coef = np.polyfit(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"], 1)
polynom = np.poly1d(coef)
ax.scatter(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"])
ax.set_xlabel("Daily Usage in Hours")
ax.set_ylabel("Hours Spent Sleeping")
plt.plot(filtered_data["Daily_Usage_Hours"], polynom(filtered_data["Daily_Usage_Hours"]), "r--", linewidth=2, label="Trendline")
ax.set_title("Comparison between Sleep and Daily Usage of Instagram")
plt.legend()
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_media_impact_on_life.csv')
sorted_data = data.sort_values(by="Daily_Usage_Hours")
filtered_data = sorted_data[sorted_data["Primary_Platform"].str.contains('Reddit', na=False)]
fig, ax = plt.subplots()
coef = np.polyfit(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"], 1)
polynom = np.poly1d(coef)
ax.scatter(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"])
ax.set_xlabel("Daily Usage in Hours")
ax.set_ylabel("Hours Spent Sleeping")
plt.plot(filtered_data["Daily_Usage_Hours"], polynom(filtered_data["Daily_Usage_Hours"]), "r--", linewidth=2, label="Trendline")
ax.set_title("Comparison between Sleep and Daily Usage of Reddit")
plt.legend()
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_media_impact_on_life.csv')
sorted_data = data.sort_values(by="Daily_Usage_Hours")
filtered_data = sorted_data[sorted_data["Primary_Platform"].str.contains('LinkedIn', na=False)]
fig, ax = plt.subplots()
coef = np.polyfit(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"], 1)
polynom = np.poly1d(coef)
ax.scatter(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"])
ax.set_xlabel("Daily Usage in Hours")
ax.set_ylabel("Hours Spent Sleeping")
plt.plot(filtered_data["Daily_Usage_Hours"], polynom(filtered_data["Daily_Usage_Hours"]), "r--", linewidth=2, label="Trendline")
ax.set_title("Comparison between Sleep and Daily Usage of LinkedIn")
plt.legend()
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_media_impact_on_life.csv')
sorted_data = data.sort_values(by="Daily_Usage_Hours")
filtered_data = sorted_data[sorted_data["Primary_Platform"].str.contains("X")]
fig, ax = plt.subplots()
coef = np.polyfit(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"], 1)
polynom = np.poly1d(coef)
ax.scatter(filtered_data["Daily_Usage_Hours"], filtered_data["Sleep_Duration_Hours"])
ax.set_xlabel("Daily Usage in Hours")
ax.set_ylabel("Hours Spent Sleeping")
plt.plot(filtered_data["Daily_Usage_Hours"], polynom(filtered_data["Daily_Usage_Hours"]), "r--", linewidth=2, label="Trendline")
ax.set_title("Comparison between Sleep and Daily Usage of X (formerly Twitter)")
plt.legend()

# %%
