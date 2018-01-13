'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
'''
import sys
import cv2
import numpy as np
import pickle
from getCellVal import *

N_images=int(sys.argv[1])
grid_line_x = 7
grid_line_y = 7
m=600/(grid_line_x-1)
n=600/(grid_line_y-1)
###Stores the numbers detected for all the tested images, maximum images 7 only
grid_map_result = [ [ [0 for i in range(grid_line_y-1)] for j in range(grid_line_x-1) ] for k in range(7) ]

def testCases(grid_map_result):
	grid_map_solution = pickle.load( open( "grid_map_solution.p", "rb" ) )
	error=0
	for l in range(0, N_images):
		print 'Testing task1_img_',l+1,'.jpg'
		for i in range(0, grid_line_y-1):
			if(grid_map_solution[l][i]==grid_map_result[l][i]):
				print "Row ",i+1,"is correct"
			else:
				print "Row ",i+1,"is wrong"
				error=error+1
	if(error>0):
		print "Test Cases verification completed with ",error,"errors"
	else:
		print "Test Cases verification completed successfully. \n You can upload your submissions now"
######################end of method###############################

#########################Test images are passed here#########################
for k in range(1,N_images+1):
	grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]
	imgpath='task1sets/task1_img_'+str(k)+'.jpg'
	img_rgb = cv2.imread(imgpath)
	grid_map=detectCellVal(img_rgb,grid_map)
	#print the grid_map
	print grid_map
	grid_map_result[k-1]=grid_map## store it in the 3 dimensional array
	######################your code here###################################
	
	img_rgb=draw(img_rgb,grid_map) ## this function is defined in detectCellVal() .This function writes the result of the expression in last column of the grid
	
	#print the output of the each expression on the input image, similar to what shown in the output.jpg image
	cv2.imshow('task1_img_'+str(k),img_rgb)
	cv2.imwrite('output/task1_img_'+str(k)+'.jpg',img_rgb)
	cv2.waitKey()
########################Test Cases are verified here, do not edit this code#########################
print "<--------------Starting Test Cases verification-------------->"
testCases(grid_map_result)
#=============================================================
