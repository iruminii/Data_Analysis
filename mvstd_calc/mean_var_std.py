import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
    
  arr = np.reshape(list, (3,3))
  m = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)]
  v = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)]
  s = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)]
  max = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max()]
  min = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min()]
  sum = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum()]
  return { 'mean' : m, 'variance' : v, 'standard deviation' : s, 'max' : max, 'min': min, 'sum':sum }
