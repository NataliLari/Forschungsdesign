import matplotlib.pyplot as plt

# Boxplots
plt.boxplot([average_lengths_m], positions=[1], labels=['Männer'], boxprops=dict(color='blue'))
plt.boxplot([average_lengths_w], positions=[2], labels=['Frauen'], boxprops=dict(color='red'))

plt.ylabel('Durchschnittliche Satzlänge')
plt.title('Boxplots der durchschnittlichen Satzlängen für Männer und Frauen')
plt.show()

# Histogramm
plt.hist(average_lengths_m, bins=20, alpha=0.5, label='Männer', color='blue')
plt.hist(average_lengths_w, bins=20, alpha=0.5, label='Frauen', color='red')
plt.xlabel('Durchschnittliche Satzlänge')
plt.ylabel('Häufigkeit')
plt.legend()
plt.title('Histogramm der Durchschnittlichen Satzlängen für Männer und Frauen')
plt.show()