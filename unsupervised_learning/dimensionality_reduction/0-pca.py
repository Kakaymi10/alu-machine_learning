import numpy as np

def pca(X, var=0.95):
    """
    Performs PCA on a dataset X to maintain a specified fraction of the variance.

    Parameters:
    X (numpy.ndarray): Shape (n, d) dataset with zero-centered dimensions.
    var (float): Fraction of the variance to maintain (default is 0.95).

    Returns:
    numpy.ndarray: Weight matrix W of shape (d, nd).
    """
    # Step 1: Compute the covariance matrix
    cov_matrix = np.cov(X, rowvar=False)

    # Step 2: Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # Step 3: Sort eigenvalues and corresponding eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Step 4: Calculate cumulative variance ratio
    cumulative_variance = np.cumsum(eigenvalues) / np.sum(eigenvalues)

    # Step 5: Select the number of components to maintain desired variance
    num_components = np.argmax(cumulative_variance >= var) + 1

    # Step 6: Construct the weight matrix W with selected eigenvectors
    W = eigenvectors[:, :num_components]

    return W
