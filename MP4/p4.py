import numpy as np
import matplotlib.pyplot as plt

# print(M)
# team_ranks = ...

# ## Bar plot for the percentage of fan support for each team
# ## (following the order of team_ranks - "best" to "worst" team)
# bar_height = ...
# x_label = ...

xstar = power_iteration(M,tol)
team_vec = list(zip(team_names,xstar))
team_vec.sort(key=lambda x:x[1],reverse=True)
team_ranks = [tup[0] for tup in team_vec]
print(team_ranks)


bar_height = [tup[1] for tup in team_vec]
x_label = team_ranks
xaxis = range(len(team_ranks))
plt.bar(xaxis, bar_height)
plt.xticks(xaxis, x_label , rotation='vertical')
plt.subplots_adjust(bottom=0.4)
plt.show()