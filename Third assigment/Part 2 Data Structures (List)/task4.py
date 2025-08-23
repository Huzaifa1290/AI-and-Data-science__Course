# Task 4: Get first and second best scores
Scores_list = [40, 89, 90, 89, 23, 90, 50]

unique_scores = list(set(Scores_list))
unique_scores.sort(reverse=True)

first_best = unique_scores[0]
second_best = unique_scores[1]

print("First best score:", first_best)
print("Second best score:", second_best)
