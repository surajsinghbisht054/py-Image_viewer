#!/usr/bin/python
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.com
# This Script is Written By
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
import os
from config import *

def get_list():
	Images=[]
	for ImageP in ImageDir:
		for i in os.listdir(ImageP):
			Image = os.path.join(ImageP,i)
			ext = Image.split('.')[::-1][0].upper()
			if ext in Extension:
				Images.append(Image)
	return Images