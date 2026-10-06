# Melatonin Project
For this project, I have analyzed a dataset containing social media use and its effects on individuals. About 4500 high school and college students were surveyed. For this project, I wanted to answer the question: Which app should melatonin supplement companies market to? 

First, I had to import the necessary packages (pandas, numerical python (or numpy), and matplotlib) for this analysis.

Next, I had to sort the data by the daily usage hours throughout the entire dataset. I opened the data using pandas and subsequently sorted it that way as well. Immediately afterwards, I filtered it by specific platforms, also using pandas.

Then came the plots. I first needed to specify the figure and axis using matplotlib's subplots feature. Then I created a scatter chart of all platforms, plotting sleep patterns against individual usage hours of the platform. In doing so, I realized I needed a trendline, so I created one using numerical python's polynomial fitting and one-dimension polynomial functions. Then, I plotted that exact trendline onto every plot I had made, proving what I had already noticed: As usage increases, sleep generally decreases.

After carefully examining all plots, I found that Instagram had the most entries in the dataset, although TikTok was not too far behind. So, I had my answer: While Melatonin supplement firms should market to all platforms, a much greater emphasis should be spent on TikTok and Instagram users than users of other platforms.