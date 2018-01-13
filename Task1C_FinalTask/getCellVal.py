# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task1C
*  Filename: getCellVal.py
*  Version: 1.0.0  
*  Date: October 13, 2016
*  
*  Author: Jayant Solanki, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""
# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)

# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
import cv2
import numpy as np

# short of time due To examinations hence please consider the tedious code, no time to optimize it.Thanks

## THIS CODE FIRST LOADS ALL THE IMAGES FROM THE DIGIT FOLDER AND READ THEM IN DIFFERENT MATRIX
## THEN WE CROPED THE SPECIFIC PART OF THE DEMO.JPG(BASICALLY A SUB-SQUARE) AND COMPARED IT WITH ALL THE MATRIX OF THE DIGIT FOLDER
## THE LIST X[ ] IS HELPING US TO FIND THE VALUE OF THE EXPRESSION 
def detectCellVal(img_rgb,grid_map):
        img_rgb=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
        x=[0 for i in range(0,6)]
       
        img0= cv2.imread('digits\\0.jpg')
        img_0=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
        img1= cv2.imread('digits\\1.jpg')
        img_1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img2= cv2.imread('digits\\2.jpg')
        img_2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        img3= cv2.imread('digits\\3.jpg')
        img_3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
        img4= cv2.imread('digits\\4.jpg')                                                  ## loading all the images from the digit folder
        img_4=cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
        img5= cv2.imread('digits\\5.jpg')
        img_5=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
        img6= cv2.imread('digits\\6.jpg')
        img_6=cv2.cvtColor(img6,cv2.COLOR_BGR2GRAY)
        img7= cv2.imread('digits\\7.jpg')
        img_7=cv2.cvtColor(img7,cv2.COLOR_BGR2GRAY)
        img8= cv2.imread('digits\\8.jpg')
        img_8=cv2.cvtColor(img8,cv2.COLOR_BGR2GRAY)
        img9= cv2.imread('digits\\9.jpg')
        img_9=cv2.cvtColor(img9,cv2.COLOR_BGR2GRAY)
        img10= cv2.imread('digits\\minus.jpg')
        img_minus=cv2.cvtColor(img10,cv2.COLOR_BGR2GRAY)
        img11= cv2.imread('digits\\plus.jpg')
        img_plus=cv2.cvtColor(img11,cv2.COLOR_BGR2GRAY)
        threshold=0.6
        col_start=0
        col_end=100
        for i in range(0,6):
           row_start=0
           row_end=100
           for j in range(0,6):    
                  template=img_rgb[col_start:col_end,row_start:row_end]      ##croping a specific part of dem0.jpg(a sub-square of 100*100 pixel) and making it the template
                  
                   ## NOW MATCING THE CROPED TEMPLATE, ONE BY ONE , WITH EACH DIGIT AND OPERATOR
                  
                  res=cv2.matchTemplate(img_1,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:  ## match is found
                      grid_map[i][j]=1

                  res=cv2.matchTemplate(img_2,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                         grid_map[i][j]=2

                  res=cv2.matchTemplate(img_3,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                        grid_map[i][j]=3

                  res=cv2.matchTemplate(img_4,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                    grid_map[i][j]=4
      
                  res=cv2.matchTemplate(img_5,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                    grid_map[i][j]=5
     
                  res=cv2.matchTemplate(img_6,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                    grid_map[i][j]=6

                  res=cv2.matchTemplate(img_7,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                    grid_map[i][j]=7

                  res=cv2.matchTemplate(img_8,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                    grid_map[i][j]=8                  

                  res=cv2.matchTemplate(img_9,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                    grid_map[i][j]=9

                  res=cv2.matchTemplate(img_0,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                    grid_map[i][j]=0
                  threshold=0.5       

                  res=cv2.matchTemplate(img_1,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:  ## match is found
                   grid_map[i][j]=1

                  res=cv2.matchTemplate(img_minus,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:  ## match is found
                   grid_map[i][j]='-'
                  threshold=0.6 

                  res=cv2.matchTemplate(img_plus,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:  ## match is found
                   grid_map[i][j]='+'

                  row_start=row_start+100
                  row_end=row_end+100
                  x[j]=grid_map[i][j]   ## this x[ j ] will store all the numbers and operators and hence will help us to find the value of the expression
                  
           if x[1] is '+':
                   x[2]=x[0]+x[2]
           elif x[1] is '-':
                   x[2]=x[0]-x[2]
           if x[3] is '+':                  ### evaluating the expression and storing it in x[ 4 ]
                   x[4]=x[2]+x[4]
           elif x[3] is '-':
                   x[4]=x[2]-x[4]

           grid_map[i][j]=x[4]    ## x[ 4 ] will contain the answer of the expression
           col_end=col_end+100
           col_start=col_start+100
        return grid_map


def draw(img_rgb,grid_map):  ## for putting the text in the output image i.e the result of the expression
        x_c=550   ## defining x and y coordinates to locate the top most left corner and later passing  it in putText() function
        y_c=50    
        for i in range(0,6):
                if grid_map[i][5]<0:  ## if the no to write is negative then widening the coordinates of the top most left corner to accomodate the no
                        cv2.putText(img_rgb,str(grid_map[i][5]),(x_c-50,y_c+25),cv2.FONT_HERSHEY_PLAIN,3.5,(0,0,255),3)
                else:
                         cv2.putText(img_rgb,str(grid_map[i][5]),(x_c-25,y_c+25),cv2.FONT_HERSHEY_PLAIN,3.5,(0,0,255),3)
                y_c=y_c+100        
                        
        return img_rgb        ## returning the modified matrix       
