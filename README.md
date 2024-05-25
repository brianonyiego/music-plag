markdown
Copy code
# Melody Plagiarism Detection System

## Overview

This Python script provides a system for detecting plagiarism in melodies. It calculates the similarity between melodies based on their interval and rhythmic representations using fuzzy logic.

## Dependencies

This script requires `numpy` to be installed. You can install it using pip:

```bash
pip install numpy
Usage
Import the necessary module:
python
Copy code
import numpy as np
Define the melody and example values:
python
Copy code
Mx = [48, 50, 48, 50, 52, 53, 52, 53]
My = [44, 55, 34, 60, 58, 45, 42, 83]

VMx = calculate_vectorial_representation(calculate_interval_representation(Mx))
VMy = calculate_vectorial_representation(calculate_interval_representation(My))
RMx = [3 / 4, 1 / 16, 1 / 16, 1 / 8, 3 / 4, 1 / 16, 1 / 16, 1 / 8]
RMy = [3 / 4, 1 / 16, 1 / 16, 1 / 8, 3 / 4, 1 / 16, 1 / 16, 1 / 8]

alpha = 0.75
Determine plagiarism:
python
Copy code
is_plagiarism = plagiarism_determination(Mx, My, VMx, VMy, RMx, RMy, alpha)
print("Is plagiarism:", is_plagiarism)
Functions
calculate_interval_representation(melody)
Calculates the interval representation of a melody.

calculate_vectorial_representation(interval_representation)
Calculates the vectorial representation of a melody.

calculate_melodic_distance(s1, s2, VM1, VM2)
Calculates the melodic distance between two subvectors.

calculate_rhythmic_distance(s1, s2, RM1, RM2)
Calculates the rhythmic distance between two subvectors.

fuzzy_vectorial_similarity(sy, sx, VMx, VMy, RMx, RMy)
Calculates the fuzzy similarity between two fragments.

fuzzy_vectorial_based_similarity(Mx, My, VMx, VMy, RMx, RMy)
Calculates the fuzzy vectorial-based similarity between two melodies.

plagiarism_determination(Mx, My, VMx, VMy, RMx, RMy, alpha)
Determines plagiarism based on fuzzy similarity and threshold.
