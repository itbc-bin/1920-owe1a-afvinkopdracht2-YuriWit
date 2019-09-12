#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FASTAanalyzer.py
#  
#  Copyright 2019 Yuri Wit <yuriwit0@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Import tkinter for file selectionj
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print ("Please select the FASTA file you want to analyze")

# Store file location in var file, open it and then store 
# the contents without header and spaces in var dna 
file = filedialog.askopenfilename()
dna = ""
with open(file) as inFile:
    for line in inFile:
        if not line.startswith(">"):
            dna += line.strip()
            
# prints the sequence
print(dna)
    
#dna = file.read()

#print (dna)
# Calculate percentages and store then in vars a, g, t, c and whole
def percentage(a, g, t, c, whole):
    return 100 * float(a)/float(whole)


a = dna.count("A")
g = dna.count("G")
t = dna.count("T")
c = dna.count("C")
u = dna.count("U")
whole = a+g+t+c+u

# Print the results
if u == 0:
	print ("Er zitten geen uracil nucleotiden in deze sequentie dus dit is een DNA sequentie")
if t == 0:
	print ("Er zitten geen thymine nucleotiden in deze sequentie dus dit is een mRNA sequentie")
	
print ("Het aantal adenine nucleotiden in deze sequentie is:", a)
print ("Het aantal guanine nucleotiden in deze sequentie is:", g)
if t != 0:
	print ("Het aantal thymine nucleotiden in deze sequentie is:", t)
print ("Het aantal cytosine nucleotiden in deze sequentie is:", c)
if u != 0:
	print ("Het aantal uracil nucleotiden in deze sequentie is:", u)
print ("Het totaal aantal nucleotiden is:", whole)

print ("Het percentage adenine nucleotiden in deze sequentie is:", round(float(100*a/whole),1),"%")
print ("Het percentage guanine nucleotiden in deze sequentie is:", round(float(100*g/whole),1),"%")
print ("Het percentage cytosine nucleotiden in deze sequentie is:", round(float(100*c/whole),1),"%")
if t != 0:	
	print ("Het percentage thymine nucleotiden in deze sequentie is:", round(float(100*t/whole),1),"%")
if u != 0:
	print ("Het percentage uracil nucleotiden in deze sequentie is:", round(float(100*u/whole), 1),"%")
print ("Het percentage GC nucleotiden paren is:", round(float(100*(t+c)/whole),1),"%")
print ("Het percentage AT nucleotiden paren is:", round(float(100*(t+c)/whole),1),"%")
