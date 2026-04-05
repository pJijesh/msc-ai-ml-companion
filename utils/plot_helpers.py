"""
Shared plotting utilities for the MSc AI & ML companion notebooks.
Jijesh Puliyappottammal — Digichange Publication, 2026
"""
import matplotlib.pyplot as plt
import numpy as np


# Colour palette matching the book's callout box scheme
COLOURS = {
    'navy':   '#1F3864',
    'blue':   '#2E75B6',
    'teal':   '#1F7D6E',
    'amber':  '#C7770A',
    'red':    '#C0392B',
    'purple': '#5B2C9E',
    'green':  '#1A7A4A',
    'lgray':  '#F2F4F7',
    'dgray':  '#4A4A4A',
}


def book_style():
    """Apply the book's matplotlib style."""
    plt.rcParams.update({
        'font.family':        'sans-serif',
        'axes.spines.top':    False,
        'axes.spines.right':  False,
        'axes.grid':          True,
        'grid.alpha':         0.3,
        'axes.titlesize':     12,
        'axes.titleweight':   'bold',
        'axes.titlecolor':    COLOURS['navy'],
        'figure.dpi':         100,
    })


def confusion_matrix_plot(cm, labels, ax=None, title='Confusion Matrix'):
    """Plot a labelled confusion matrix."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(cm, interpolation='nearest', cmap='Blues')
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(len(labels)), yticks=np.arange(len(labels)),
           xticklabels=labels, yticklabels=labels,
           xlabel='Predicted', ylabel='True', title=title)
    thresh = cm.max() / 2
    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha='center', va='center',
                    color='white' if cm[i, j] > thresh else 'black')
    return ax


def learning_curve_plot(train_losses, val_losses=None, title='Training Curve'):
    """Plot training (and optional validation) loss over epochs."""
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(train_losses, label='Train loss', color=COLOURS['blue'], lw=2)
    if val_losses is not None:
        ax.plot(val_losses, label='Val loss', color=COLOURS['red'], lw=2, linestyle='--')
    ax.set_xlabel('Epoch'); ax.set_ylabel('Loss')
    ax.set_title(title, color=COLOURS['navy'], fontweight='bold')
    ax.legend(); ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig, ax
