import matplotlib.pyplot as plt

modes = ['Sequential', 'xdist load', 'xdist no', 'run-parallel']
speedups = [1.0, 0.608, 0.602, 0.088]

plt.bar(modes, speedups, color=['gray', 'blue', 'green', 'orange'])
plt.xlabel('Parallelization Mode')
plt.ylabel('Speedup (Tseq/Tpar)')
plt.title('Speedup Ratios for Different Parallelization Modes')
plt.ylim(0, max(speedups) + 1)
plt.show()