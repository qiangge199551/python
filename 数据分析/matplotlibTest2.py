from numpy import *
from matplotlib import pyplot

def main():
	pyplot.figure().add_subplot(3,3,1)
	n = 128
	X = random.normal(0, 1, n)
	Y = random.normal(0, 1, n)
	T = arctan2(Y, X)
	pyplot.axes([0.025, 0.025, 0.95, 0.95])
	pyplot.scatter(X, Y, s=75, c=T, alpha=0.5)
	pyplot.xlim(-1.5, 1.5), pyplot.xticks([])
	pyplot.ylim(-1.5, 1.5), pyplot.yticks([])
	pyplot.axis()
	pyplot.title('scatter')
	pyplot.xlabel('x')
	pyplot.ylabel('y')

	ax = pyplot.figure().add_subplot(3,3,2)
	n = 10
	X = arange(n)
	Y1 = (1-X/float(n))*random.uniform(0.5,1.0,n)
	Y2 = (1-X/float(n))*random.uniform(0.5,1.0,n)
	ax.bar(X, +Y1, facecolor='#9999ff', edgecolor='w')
	ax.bar(X, +Y2, facecolor='#ff9999', edgecolor='w')
	for x,y in zip(X, Y1):
		pyplot.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va='bottom')
	for x,y in zip(X, Y2):
		pyplot.text(x+0.4, -y-0.05, '%.2f' % y, ha='center', va='top')

	pyplot.show()



if __name__ == '__main__':
	main()