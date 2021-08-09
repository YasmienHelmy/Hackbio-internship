#!/usr/bin/python
print ("Yasmien")
print ("yasmeenkhedry2020@gmail.com")
print ("@sam")
print ("GenomicsTranscriptomicsvaccineinformatics")
print ("@Jaz")
#calculating hamming distance 
def h_d_loop(str_1,str_2) :
     h_distance = 0
     for position in range(len(str_1)):
         if str_1[position] != str_2[position] :
            h_distance += 1 
     return h_distance
 
str_1= "Jaz"
str_2= "Sam"
print (h_d_loop(str_1,str_2))
