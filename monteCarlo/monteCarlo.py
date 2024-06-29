import random

RADIUS=10000
TOTAL_POINTS=1000000

def monteCarloPi(totalPoints):
	xs = []
	ys = []
	pt = 0

	for i in range(totalPoints):
		xs.append(random.randint(0, RADIUS))
		ys.append(random.randint(0, RADIUS))



	for i in range(totalPoints):
		if(xs[i]*xs[i] + ys[i]*ys[i]) < RADIUS*RADIUS:
			pt = pt + 1
	return pt
		




def main():
	p1=monteCarloPi(int(TOTAL_POINTS/4))
	p2=monteCarloPi(int(TOTAL_POINTS/4))
	p3=monteCarloPi(int(TOTAL_POINTS/4))
	p4=monteCarloPi(int(TOTAL_POINTS/4))


	Pi = 4 * float(p1+p2+p3+p4)/TOTAL_POINTS

	print("pi: "+ str(Pi))




if __name__ == '__main__':
	main()