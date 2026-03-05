"""
eda_utils.py
Shared EDA utilities for Group 013 COGS 108 project.
"""
from scipy import stats


def compute_correlations(x, y, label=''):
    """
    Compute and print Pearson and Spearman correlations between x and y.

    Args:
        x (array-like): First variable.
        y (array-like): Second variable.
        label (str): Optional label to prefix the output (e.g. 'Raw' or 'First-difference').

    Returns:
        dict: Keys 'pearson_r', 'pearson_p', 'spearman_r', 'spearman_p'.
    """
    pearson_r,  pearson_p  = stats.pearsonr(x, y)
    spearman_r, spearman_p = stats.spearmanr(x, y)

    prefix = f'[{label}] ' if label else ''
    print(f'{prefix}Pearson  r = {pearson_r:.4f}  (p = {pearson_p:.2e})')
    print(f'{prefix}Spearman r = {spearman_r:.4f}  (p = {spearman_p:.2e})')

    return {
        'pearson_r':  pearson_r,
        'pearson_p':  pearson_p,
        'spearman_r': spearman_r,
        'spearman_p': spearman_p,
    }
