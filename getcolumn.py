#######################################################################################
## :: Extract specific column data and time from LAMMPS log files ::                 ##
##    Usage: <python getcolumn.py>                                                   ##
##                                                                                   ##
##                                                            Brett Donovan 2011     ##
#######################################################################################

import os
import shutil
import sys
import re

def main(argv):
	if len(argv) < 5:
	        sys.stderr.write("Usage: %s <io_filename> <column> <op_filename> <startn>\n" % (argv[0],))
	        return 1
	if not os.path.exists(argv[1]):
        	sys.stderr.write("ERROR: filename %r was not found!\n" % (argv[1],))
        	return 1
	if os.path.exists(argv[1]):
        	f = open(argv[1], "r")
		w = open(argv[3], "w")

		### Use the 'Step' word to locate the beginning of the rows we are interested in.
		### From LAMMPS format we don't see numbers on the leftmost column after the 'Steps' header

		collect = False
		for line in f:
			if "Step" in line:
				collect = True
			if (re.search('\d+', line)) and collect:
				splitline = line.split()
				if (re.search('\d+', splitline[0])):
					if float(splitline[0]) > float(argv[4]):
						newline = str(splitline[0]) + "   " + str(splitline[int(argv[2])] + "\n")
						w.write(newline)
		f.close()
		w.close()
 		return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
	
	
	

