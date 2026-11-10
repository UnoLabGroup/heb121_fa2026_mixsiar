# HEB 121: Stable Isotope Methods in Modern and Paleo Ecology
# Histogram of C3 and C4 plant d13C values from Cerling & Harris (1999) Appendix 1

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


ch99_df = pd.read_csv("C:/Users/kul362/GitHub/heb121_mixsiar/cerling_1999_plants.csv")
c3 = ch99_df[ch99_df['c3c4'] == "c3"].reset_index(drop=True)
c4 = ch99_df[ch99_df['c3c4'] == "c4"].reset_index(drop=True)


# Figure script
fig, axs  = plt.subplots(1,1,layout='constrained')

ax = axs
sns.histplot(
    ax=ax, data=c3, x="d13c", stat='count', binwidth=0.5, kde=False,
    color='C0', legend=True, zorder=0
)
sns.histplot(
    ax=ax, data=c4, x="d13c", stat='count', binwidth=0.5, kde=False,
    color='C2', legend=True, zorder=1
)
ax.set_xlabel(u"\u03B4$^{13}$C (\u2030 VPDB)")
ax.set_ylabel("Counts")


figure_plant_hist = plt.gcf()
figure_plant_hist.savefig('plots/plant_hist.png', dpi=300)