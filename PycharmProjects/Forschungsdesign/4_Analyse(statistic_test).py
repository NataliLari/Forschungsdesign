import scipy.stats as stats

t_statistic, p_value = stats.ttest_ind(average_lengths_w, average_lengths_m)

print("T-Statistik:", t_statistic)
print("P-Wert:", p_value)