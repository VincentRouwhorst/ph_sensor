#!/usr/bin/python
#--------------------------------------
#
# Ph calibration script
#
# Author : Vincent Rouwhorst
# Date   : 29/07/2018
#
#--------------------------------------

import statistics
import cvs

ph_range = 0
ph_volt = 0
ph_constante = []
i = 0
   
while True:
    try:
        ph = -1
        while ph not in range(15):
            ph = float(input('Ph : '))
        ph_range = -(ph-7)
        print('Range : ', ph_range)
        ph_volt = float(input('mVolt : '))
        #print(i)
        ph_constante.append(ph_volt/ph_range)
        print('Ph Constant: ', ph_constante[i])
        #print(ph_constante)
        print(statistics.mean(ph_constante))
        i += 1
        # File writer
        with open('ph_config.cvs', 'w', newline='') as f:
            fieldnames = ['ph', 'mvolt', 'ph_const']
            thewriter = cvs.DictWriter(f, fieldnames=fieldnames)
            thewriter.writeheader()
            
            for i_ph in range(15):
                print('Ph : ', i_ph, 'mVolt : ', (-(i_ph-7)*statistics.mean(ph_constante)))
                thewriter.writerow({'ph' : i_ph, 'mvolt' : (-(i_ph-7)*statistics.mean(ph_constante)), 'ph_const' : statistics.mean(ph_constante)})
    except ValueError:
        print('Oops!  That was no valid number.  Try again...')
