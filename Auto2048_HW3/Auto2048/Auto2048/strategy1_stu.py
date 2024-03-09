import sys
import math
import random

MAP_FILE_NAME = "MAPFILE.txt"
STEPS_FILE_NAME = "steps.txt"
UP_DOWN_SCORE_HIGHER = True
LEFT_RIGHT_SCORE_HIGHER = False

def readMap():
	
	currentMap = []
	
	# TODO: please read map from MAP_FILE_NAME


	for line in currentMap:
		print('row=' + str(id))
		strTemp = ""
		for item in line:
			strTemp = strTemp + "\t" + item
		print(strTemp)
		id+=1
	return currentMap



def writeStep(_score_higher):
	f = open(STEPS_FILE_NAME, "a")
	res = random.randint(0, 1)

	#TODO: Please decide moving Up Down or Left Right by which will get higher score
	
	f.close()
	return


def sum_up_down(_currentMap):
	
	#Please try to calculate the score added after moving up or down

	return score_add


def sum_left_right(_currentMap):

	#Please try to calculate the score added after moving left or right

	return score_add

def main():
	#print("debug here")
	currentMap = readMap()
	if sum_up_down(currentMap) > sum_left_right(currentMap):
		writeStep(UP_DOWN_SCORE_HIGHER)
	else:
		writeStep(LEFT_RIGHT_SCORE_HIGHER)


if __name__ == '__main__':
    main()
