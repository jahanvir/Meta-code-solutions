Reverse to Make Equal
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
Signature
bool areTheyEqual(int[] arr_a, int[] arr_b)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if B can be made equal to A, return false otherwise.
Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output = true
After reversing the subarray of B from indices 1 to 3, array B will equal array A.


""" Brute force Method """

def are_they_equal(array_a, array_b):
  
  if len(array_a)!=len(array_b):
    return False
  if array_a==array_b:
    return True
  
  for sp in range(0, len(array_b)):
    for i in range(1, len(array_b)-sp+1):
      array_b[sp:sp+i]=array_b[sp:sp+i][::-1]
      if array_a==array_b:
        return True
      array_b[sp:sp+i]=array_b[sp:sp+i][::-1]
  return False
  
  
  
  
