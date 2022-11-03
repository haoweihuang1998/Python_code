import matplotlib.pyplot as plt
def plotData(plt, data):
  x = [p[0] for p in data]
  y = [p[1] for p in data]
  plt.plot(x, y, '-o')
data_1 = [(1,2), (3,4), (5,2), (7,5), (9,8)]
data_2 = [(1,1), (3,6), (3,9), (7,9), (9,3)]
plotData(plt, data_1)
plotData(plt, data_2)
plt.show()
