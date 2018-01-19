#!/usr/bin/env python
#
#  Raw file to VBA array generator
#  Stuart Morgan (@ukstufus) <stuart.morgan@mwrinfosecurity.com> 2018
#  MWR InfoSecurity, MWR Labs
# 
#  This tool is designed to allow you to specify a file which is convered to a chr() array
#  for inclusion in a VBA script.
#
#  Usage:
#   file2vb.py -s sourcefile.txt > output.txt
#
#  This will take the source file and:
#  1) Convert it to a Chr() expression
#  2) Split it up into multiple functions if it is too large
#
#  Improvements:
#  - Use arrays and compress data rather than writing it so verbosely
#
import sys
import hashlib
import argparse

def writeout(originalvarname, data):
    overallcounter = 0

    varname = originalvarname + str(overallcounter)
    linecounter = 0
    sys.stdout.write("Function " + varname + "() As String\n" + varname+" = ")

    for c in data:
        if linecounter and not linecounter % 600:
            overallcounter += 1
            varname = originalvarname + str(overallcounter)
            sys.stdout.write("\nEnd Function\nFunction " + varname + "() As String\n")
            sys.stdout.write(varname+" = ")
        elif linecounter % 15:
            sys.stdout.write(' & ')
        elif linecounter:
            sys.stdout.write("\n" + varname + " = " + varname + " & ")
    
        individual_char = ord(c)
        sys.stdout.write("chr(" + str(individual_char) + ")")
        linecounter += 1

    sys.stdout.write("\n\n")

    sys.stdout.write("Dim " + originalvarname + "As String\n")
    sys.stdout.write(originalvarname + " = ")
    for x in range(0, overallcounter + 1):
        if x:
            sys.stdout.write(" & ")
        sys.stdout.write(originalvarname + str(x) + "()")

    sys.stdout.write("\n\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File to VBA string converter')
    parser.add_argument('-s', '--sourcefile', action='store', help='The filename containing the source data.')
    args = vars(parser.parse_args())

    if 'sourcefile' in args and args['sourcefile'] != None:
        # Read the source file information
        with open(args['sourcefile'], 'rb') as s:
            datafile = s.read()
            s.close()

        writeout('MSBuildData', datafile)
