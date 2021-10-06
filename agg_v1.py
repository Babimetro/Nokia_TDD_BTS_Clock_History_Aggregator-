
hello="""#=============================================================================#
#                                Hello                                        #
#                                 AGG V1                                      #
# This program is written by Babak Izadpanah to make your life easier.        #
# This code is covertor and aggregator of Nokia clock history xml format file.#
#                                                                             #
#       please let me know any bugg you found by babak.izadpanah@gmail.com    #
#                     find a bug and win new version!                         #
#                                                                             #
#                                                                             # 
#                           Enjoy your life!                                  #
#                                                                             #
#=============================================================================#"""

print(hello)
 
import os
import fnmatch
import pandas as pd
import xml.etree.ElementTree as ET
from tkinter import *
import tkinter as tk
from tkinter import StringVar
 
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


 
def progressBar(count,total,suffix=''):
    barlenght=60
    filledlenght=int(round(barlenght*count/float(total)))
    percent=round(100.0*count/float(total),1)
    bar='O'*filledlenght+'-'*(barlenght-filledlenght)
    sys.stdout.write('[%s] %s%s...%s\r' %(bar,percent,'%',suffix))
    sys.stdout.flush()
 
window = tk.Tk()

window.title("No hang PPM aggregator")
 
label1 = tk.Label(window, text='Hello,find a bug and win new version!', borderwidth=50)
label1.grid(row=0, column=1)

label3 = tk.Label(window, text='Enter PPM folder like "D:\PPM Folder"', borderwidth=5)
label3.grid(row=2, column=1)
input_folder_box = tk.Entry (window,borderwidth=5)
input_folder_box.grid(row=3, column=1)


 



exit_button = tk.Button (window, text='Exit Application',borderwidth=10, command=window.destroy)
exit_button.grid(row=10, column=1)

 
global infolder
global outfolder


   
 
def action():
    infolder =str(input_folder_box.get())
    print(infolder)
    os.chdir(infolder)
    logg=pd.read_csv('logg.csv', encoding='utf8', header=0)
     
    i=0
    for root, dir, files in os.walk("."):
            print( root)
            print ()
            for items in fnmatch.filter(files, "*"):
                l=len(items)
                l=l-3
                if(items[l:]=='xml'):
                    i=i+1
    print("Number of files=",str(i))

      
    i=0
    for root, dir, files in os.walk("."):
            print( root)
            print ()
            for items in fnmatch.filter(files, "*"):
                li=len(items)
                l=li-3
                if(items[l:]=='xml'):
                     
                    print(items)
                    tree = ET.parse(items)
                    EnodB=items
                    print()
                    root = tree.getroot()

                    #for child in root:
                        #print(child.tag, child.attrib)

                    d = [elem.tag for elem in root.iter()]

                    dff = pd.DataFrame(d)
                    dff.columns = ['name']
                    dff['name'].value_counts()
                    attribute_list = ['_clockFrequencyDiff', '_gpsSatelliteAmount',
                    '_dacWord','_observationTime', '_rejectedSamplePc','FrequencyHistoryData', '_unitId',
                    '_tuningMode', '_referenceSource','_possibleHoldoverTime']

                    dff = pd.DataFrame(columns=attribute_list)
                    for j in attribute_list:

                        for n,i in enumerate(root.iter(j)):#,'_dacWord'):
                            #print(n,i)
                            #dff[j].at[i] = i.text
                            dff.at[n,j] = i.text
                            #dff.ix[i, j] = i.text
                            #df['col'].at['row']

                        #print(i.attrib,i.text) #(i.attrib,i.text)

                    dff['EnodB']=EnodB[:6]
                    logg=logg.append(dff,sort=False)#1
    logg.to_csv('ppm result.csv')
    #tkMessageBox.showinfo( "babimetro", "Finished")

start_button = tk.Button (window, text='       Start         ',borderwidth=20, command=action)
start_button.grid(row=8, column=1)


window.mainloop()
#===========================================