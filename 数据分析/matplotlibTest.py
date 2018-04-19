from numpy import *
from matplotlib import pyplot

def main():
	x = linspace(-pi, pi,256,endpoint=True)
	c,s=cos(x),sin(x)
	pyplot.figure(1)
	pyplot.plot(x, c, color='blue', linewidth=1.0, linestyle='-', label='COS', alpha=0.5)
	pyplot.plot(x, s, 'b*', label='SIN')
	pyplot.title('COS & SIN')
	pyplot.gca().spines['right'].set_color('none')
	pyplot.gca().spines['top'].set_color('none')
	pyplot.gca().spines['left'].set_position(('data', 0))
	pyplot.gca().spines['bottom'].set_position(('data', 0))
	pyplot.gca().xaxis.set_ticks_position('bottom')
	pyplot.gca().yaxis.set_ticks_position('left')
	pyplot.xticks([-pi, pi/2, 2, pi/2, pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
	pyplot.yticks(linspace(-1, 1, 5, endpoint=True))
	for label in pyplot.gca().get_xticklabels() + pyplot.gca().get_yticklabels():
		label.set_fontsize(16)
		label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.2))
	pyplot.legend(loc='upper left')
	# pyplot.grid()
	# pyplot.axis([-pi, pi, -1, 1])
	pyplot.fill_between(x, abs(x)<0.5, c, c>0.5, color='g', alpha=0.25)
	pyplot.plot([1,1], [0, cos(1)], 'y', linewidth=3, linestyle='--')
	pyplot.annotate('cos(1)', xy=(1, cos(1)), xycoords='data', xytext=(+10, +30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
	pyplot.show()

if __name__ == '__main__':
	main()