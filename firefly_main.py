from fireflies import *
import random
import matplotlib.pyplot as plt
from City import *
import tsplib95


def draw(points):
	# Adding the title
	plt.title("position of cities")

	# Adding the labels
	plt.ylabel("y coordinate of cities")
	plt.xlabel("x coordinate of cities")
	points = list(points)
	points = points + points[:1]
	cities = map(lambda i: (i.x, i.y), points)
	(x, y) = zip(*cities)
	plt.scatter(x, y)
	plt.plot(x, y)
	plt.show()

if __name__ == '__main__':
	problem = tsplib95.load('archives/problems/vrp/eil22.vrp')

	##randomyl making a graph
	number_of_points = int(input('Number of cities: '))
	next_random = lambda: random.random() * 100
	answer=[]


	locations = [ City(problem.node_coords[i+1][0] , problem.node_coords[i+1][1] , i ) for i in range(number_of_points) ]
	#n = int(input("Enter number of stops: "))
	x = []
	y = []
	sites = {}
	#for i in range(n):
		#a = input("Enter Stop-name, X-Coordinate, Y-Coordinate ")
		#ele = list(map(str, a.split()))
		#x.append(int(ele[1]))
		#y.append(int(ele[2]))

		#sites[i] = ele[0]
	#locations = [City(x[i],y[i], i) for i in range(n)]

	draw(locations)
	solver = TSPSolver(locations)
	new_order = solver.run()

	new_locations = [locations[i] for i in new_order]
	for i in new_locations :

		answer.append(i.number)
	draw(new_locations)
	print(answer)
	#for i in range (0,n):
		#print(sites[answer[i]])



