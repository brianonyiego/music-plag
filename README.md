# README: Melody Plagiarism Detection System

This program is designed to detect plagiarism between two melodies using a fuzzy vectorial-based similarity method. The system calculates melodic and rhythmic distances between the two melodies and determines if the similarity exceeds a given threshold (alpha).

## Steps Overview

### Step 1: Interval Representation
The function `calculate_interval_representation(melody)` converts a melody into a sequence of intervals (differences between consecutive notes). This representation helps capture the structure of the melody.

### Step 2: Vectorial Representation
The function `calculate_vectorial_representation(interval_representation)` converts the interval representation into a vector format, which is easier to compare mathematically.

### Step 3: Melodic Distance Calculation
The function `calculate_melodic_distance(s1, s2, VM1, VM2)` computes the melodic distance between two subvectors (fragments) from the vector representations of the two melodies. It uses the absolute difference between the subvectors and squares the result.

### Step 4: Rhythmic Distance Calculation
The function `calculate_rhythmic_distance(s1, s2, RM1, RM2)` computes the rhythmic distance between subvectors of two rhythms. Similar to melodic distance, it calculates the difference between rhythms.

### Step 5: Fuzzy Vectorial Similarity
The function `fuzzy_vectorial_similarity(sy, sx, VMx, VMy, RMx, RMy)` combines melodic and rhythmic distances to determine the similarity between two fragments. It calculates a similarity score, with higher values indicating greater similarity.

### Step 6: Fuzzy Vectorial-Based Similarity Between Two Melodies
The function `fuzzy_vectorial_based_similarity(Mx, My, VMx, VMy, RMx, RMy)` compares two entire melodies by summing the similarity scores of all possible pairs of fragments. It returns an overall fuzzy similarity score between the two melodies.

### Step 7: Plagiarism Determination
The function `plagiarism_determination(Mx, My, VMx, VMy, RMx, RMy, alpha)` determines if two melodies are considered plagiarized based on the similarity score and the threshold value `alpha`. If the similarity exceeds the threshold, plagiarism is flagged as true.



```python
Mx = [48, 50, 48, 50, 52, 53, 52, 53]
My = [44, 55, 34, 60, 58, 45, 42, 83]

VMx = calculate_vectorial_representation(calculate_interval_representation(Mx))
VMy = calculate_vectorial_representation(calculate_interval_representation(My))

RMx = [3 / 4, 1 / 16, 1 / 16, 1 / 8, 3 / 4, 1 / 16, 1 / 16, 1 / 8]
RMy = [3 / 4, 1 / 16, 1 / 16, 1 / 8, 3 / 4, 1 / 16, 1 / 16, 1 / 8]

alpha = 0.75
is_plagiarism = plagiarism_determination(Mx, My, VMx, VMy, RMx, RMy, alpha)
print("Is plagiarism:", is_plagiarism)
