"""
sorting algoithm for hw10
"""

def selection_sort(values):
    for i in range(len(values)):
        low = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < low:
                low = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]
    return values
