import numpy as np

def calculate(data):
  # A check to see if a list containing less than 9 elements is passed into the function
  if len(data) < 9:
    raise ValueError("List must contain nine numbers.")

  # Converts the list into a 3 x 3 Numpy array
  matrix = np.array(data).reshape(3, 3)

  '''
  A dictionary containing the mean, variance, standard deviation, max, min, 
  and sum along both axes and for the flattened matrix
  '''
  calc_dict = {
    'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), np.mean(matrix.flatten())],
    'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)), np.var(matrix.flatten())],
    'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), np.std((matrix.flatten()))],
    'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), np.max(matrix.flatten())],
    'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), np.min(matrix.flatten())],
    'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), np.sum(matrix.flatten())]
  }

  return calc_dict