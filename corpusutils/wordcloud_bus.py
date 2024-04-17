import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from os import path
from wordcloud import WordCloud
from Objectif_ligne import les_plus_frequente

bus_mask = np.array(Image.open(r"Data\bus.png"))
bag = les_plus_frequente('1e-sem-2016.csv',20)
d = {}
for a, x in bag.values:
    d[a] = x

wordcloud = WordCloud(
    width = 1200,
    height = 1200,
    background_color="white",
    max_words=20,
    mask=bus_mask,
    contour_width=3,
    contour_color='steelblue')
wordcloud.generate_from_frequencies(frequencies=d)
fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k')
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()