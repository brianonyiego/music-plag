import numpy as np


# Step 1: Calculate the interval representation of a melody
def calculate_interval_representation(melody):
    interval_representation = []
    for i in range(len(melody) - 1):
        interval = melody[i + 1] - melody[i]
        interval_representation.append(interval)
    return interval_representation


# Step 2: Calculate the vectorial representation of a melody
def calculate_vectorial_representation(interval_representation):
    vectorial_representation = interval_representation.copy()
    return vectorial_representation


# Step 3: Calculate melodic distance between two subvectors
def calculate_melodic_distance(s1, s2, VM1, VM2):
    melodic_distance = np.sum(np.abs(np.array(VM1[s1]) - np.array(VM2[s2]))) ** 2
    return melodic_distance


# Step 4: Calculate rhythmic distance between two subvectors
def calculate_rhythmic_distance(s1, s2, RM1, RM2):
    rhythmic_distance = np.sum(np.abs(np.array(RM1[s1]) - np.array(RM2[s2]))) ** 2
    return rhythmic_distance


# Step 5: Calculate fuzzy similarity between two fragments
def fuzzy_vectorial_similarity(sy, sx, VMx, VMy, RMx, RMy):
    melodic_distance = calculate_melodic_distance(sy, sx, VMx, VMy)
    rhythmic_distance = calculate_rhythmic_distance(sy, sx, RMx, RMy)

    fragment_similarity = 1 - np.sqrt(melodic_distance + rhythmic_distance)
    return fragment_similarity


# Step 6: Calculate fuzzy vectorial-based similarity between two melodies
def fuzzy_vectorial_based_similarity(Mx, My, VMx, VMy, RMx, RMy):
    total_similarity = 0
    for sy in range(len(VMy)):
        for sx in range(len(VMx)):
            fragment_similarity = fuzzy_vectorial_similarity(sy, sx, VMx, VMy, RMx, RMy)
            total_similarity += fragment_similarity

    fuzzy_similarity = total_similarity / len(VMy)
    return fuzzy_similarity


# Step 7: Determine plagiarism based on fuzzy similarity and threshold
def plagiarism_determination(Mx, My, VMx, VMy, RMx, RMy, alpha):
    fuzzy_similarity = fuzzy_vectorial_based_similarity(Mx, My, VMx, VMy, RMx, RMy)

    if min(fuzzy_similarity, fuzzy_vectorial_based_similarity(My, Mx, VMy, VMx, RMy, RMx)) >= alpha:
        return True
    else:
        return False


# Example values
Mx = [48, 50, 48, 50, 52, 53, 52, 53]
My = [44, 55, 34, 60, 58, 45, 42, 83]

VMx = calculate_vectorial_representation(calculate_interval_representation(Mx))
VMy = calculate_vectorial_representation(calculate_interval_representation(My))
RMx = [3 / 4, 1 / 16, 1 / 16, 1 / 8, 3 / 4, 1 / 16, 1 / 16, 1 / 8]
RMy = [3 / 4, 1 / 16, 1 / 16, 1 / 8, 3 / 4, 1 / 16, 1 / 16, 1 / 8]

alpha = 0.75
is_plagiarism = plagiarism_determination(Mx, My, VMx, VMy, RMx, RMy, alpha)
print("Is plagiarism:", is_plagiarism)
