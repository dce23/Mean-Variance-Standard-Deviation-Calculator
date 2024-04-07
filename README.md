# Mean-Variance-Standard-Deviation-Calculator
## The powerful Numpy library provided advanced statistical analyses on a 3x3 matrix for this project. Numpy is a high-performance library that provides efficient numerical operations on multi-dimensional arrays and matrices. 

### Our analysis will involve computing various statistical measurements, including the mean, variance, standard deviation, maximum value, minimum value, and the sum of each row, column, and element within the matrix. To calculate the mean of the matrix, we will add up all the values and divide by the total number of elements. The variance will tell us how spread out the values are from the mean, while the standard deviation will give us an idea of how much the values deviate from the mean. The maximum and minimum values will provide us with the range of values in the matrix, and the sum of each row, column, and element will give us a better understanding of the distribution of values within the matrix. By generating these statistical measurements, I can gain deeper insights into the underlying data in the matrix, which will help us make more informed decisions based on the data in a 3x3 matrix.

- The function takes a list of 9 digits as input. It converts the list into a 3 x 3 Numpy array and returns a dictionary. The dictionary contains the mean, variance, standard deviation, max, min, and sum along both axes and the flattened matrix.

### The returned dictionary follows this format:

```python
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```
### If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

### For example, calculate([0,1,2,3,4,5,6,7,8]) returns:
```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```
