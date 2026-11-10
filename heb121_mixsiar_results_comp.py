# HEB 121: Stable Isotope Methods in Modern and Paleo Ecology
# MixSIAR results vs. Cerling et al. (2003)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


ch03_df = pd.read_csv("C:/Users/kul362/GitHub/heb121_mixsiar/cerling_2003_bovids.csv")

one2one_line = np.linspace(0,100,10)


# Figure script
fig, axs = plt.subplots(2,2,layout='constrained')

ax = axs[0,0]
ax.plot(
    ch03_df.per_c4, ch03_df.c4_u*100,
    marker='o', linewidth=0, markeredgecolor='k',
    zorder=5
)
ax.plot(
    one2one_line, one2one_line,
    color='k', linewidth=1,
    zorder=1
)
ax.set_xlim([-5,105])
ax.set_ylim([-5,105])
ax.set_xlabel(u"Cerling 2003 % C$_{4}$")
ax.set_ylabel(u"MixSIAR Mean % C$_{4}$")

ax = axs[0,1]
ax.plot(
    ch03_df.per_c4, ch03_df.c4_sd*100,
    marker='o', linewidth=0, markeredgecolor='k'
)
ax.set_xlim([-5,105])
ax.set_ylim([0,15])
ax.set_xlabel(u"Cerling 2003 % C$_{4}$")
ax.set_ylabel(u"MixSIAR SD % C$_{4}$")
ax.yaxis.set_ticks_position("right")
ax.yaxis.set_label_position("right")


fig.delaxes(axs[1,0])
fig.delaxes(axs[1,1])

figure_mixsiar_comp = plt.gcf()
figure_mixsiar_comp.savefig('plots/mixsiar_comp.png', dpi=300)