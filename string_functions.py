import numpy as np

"""
String functions in NumPy
Why do we need to do String manipulation during data analysis?

Data Cleaning:
Whitespace Removal: String data often contains leading or trailing spaces that can cause issues in data analysis. Cleaning up these spaces ensures consistency.
Case Consistency: Ensuring uniform case (all lowercase or uppercase) can help in consistent data matching and comparison.

Data Transformation:
Concatenation: Combining multiple string fields into one can be useful in creating composite keys or merging columns.
Replacement and Substitution: Correcting typos or replacing certain parts of strings with new values is common in data cleaning.

Data Parsing and Extraction:
Splitting: Breaking down a string into parts (like splitting a full name into first and last names) helps in organising data better.
Pattern Matching: Extracting specific patterns from strings (like extracting dates or email addresses) is often needed in data preprocessing.
"""

arr1 = np.array([['hello', 'good'], ['morning', 'night']])
arr2 = np.array([['world', 'morning'], ['everyone', 'moon']])

concatenated = np.char.add(arr1, arr2)
print(concatenated)

capitalize = np.char.capitalize(concatenated)
print(capitalize)

multiple = np.char.multiply(capitalize,2)
print(multiple)


