from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import logging

logging.basicConfig()
logging.root.setLevel(logging.INFO)

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

def extract_dominant_colors_from_palette(palette, num_colors=5):
    logging.info(f"Start clustering, number of centers: {num_colors}")
    # Use K-Means clustering to extract dominant colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(palette)

    # Get the RGB values of the cluster centers (dominant colors)
    dominant_colors = kmeans.cluster_centers_
    labels = kmeans.labels_

    label_data = {}
    for label, center in enumerate(dominant_colors):
        # Find points (colors) belonging to the current cluster
        points_for_cluster = [palette[i] for i in range(len(palette)) if labels[i] == label]
        label_data[label] = {'center': center, 'points': points_for_cluster}

    dominant_colors = [tuple([int(e) for e in c]) for c in dominant_colors]

    return dominant_colors, label_data


def avg_similatiry(color, dominant_labels):
    pass

def get_nearest_dominant_swap(color, dominant_colors):
    for dc,labels in dominant_colors:
        pass
    pass