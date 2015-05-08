#!/usr/bin/python
import sys
import os
from os import path, access, remove

#Prompt for input file path
inputFilePath = raw_input('Path to wordlist <*default is /pentest/password/wordlists/darkc0de.lst*>')

#Open original wordlist 
if str(inputFilePath) == '':
   inputFilePath = '/pentest/password/wordlists/darkc0de.lst'
if path.exists(inputFilePath) and path.isfile(inputFilePath):
  print 'File found lets do this thing'
else:
   print 'That either isn\'t a file or doesn\'t exist. Exiting'
   exit()

inputWordList = open(inputFilePath, 'rb').readlines()

#Prompt for output file path
print 'WARNING: IF FILE ALREADY EXISTS IT WILL BE DELETED'
outputFilePath = raw_input('Path to save wordlist <*default is /root/Desktop/lengthsortedlist.txt*>')

#Open original wordlist 
if str(outputFilePath) == '':
   outputFilePath = '/root/Desktop/lengthsortedlist.txt'
if path.exists(outputFilePath):
   remove(outputFilePath)
outputFile = open(outputFilePath, 'w')

#Prompt for minimum word length
inputMinLen = raw_input('Minimum word length: ')
outCount = 0

#Read in line and check length, write to file if greater than or equal to inputMinLen
for line in inputWordList:
   line = line.rstrip()
   
   #Debug stuff
   #print line, len(line.rstrip()), len(line) >= int(inputMinLen)
   #raw_input('pause')
   if len(line.rstrip()) >= int(inputMinLen):
      outString = line+'\n'
      outputFile.write(outString)
      outCount += 1

#Clean up
print (str(outCount)) + ' written to file  at ' + outputFilePath
outputFile.close()



