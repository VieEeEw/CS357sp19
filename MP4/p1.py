import numpy as np
print(len(home_team),len(home_score))
matches = list(zip(home_team, away_team, home_score, away_score))
# print(matches)
team_names = list(set(home_team).union(set(away_team)))
A = np.zeros((len(team_names), len(team_names)))
for i in range(len(A)):
    for j in range(len(A)):
        for m in matches:
            if m[0] == team_names[i] and m[1] == team_names[j]:
                if  m[2] - m[3] > 0:
                    A[i][j] += m[2] - m[3]
                else:
                    A[j][i] += m[3] - m[2]
# print(team_names)
print(A)