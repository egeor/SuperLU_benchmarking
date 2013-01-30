#!/usr/bin/python
import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	it_bound = 0
	
	try:
		opts, args = getopt.getopt(argv,"hi:o:b:",["ifile=","ofile=","iterbound="])
	except getopt.GetoptError:
		print 'tau_parser.py -i <inputfile> -b <iteration_bound>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'tau_parser.py -i <inputfile> -b <iteration_bound>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-b", "--iterbound"):
			it_bound = int(arg)

	in_file = open(inputfile, 'r')
	lines = in_file.readlines()

	found_mean = 0
	total_fact_time = 0.0
	update2_total = 0.0
	update1_total = 0.0
	u_comp_and_send_total = 0.0
	l_panel_fact_total = 0.0
	partial_sum = 0.0
	partial_sum2 = 0.0
	max_iteration = 0
		
	for line in lines:
		if "mean" in line:
			found_mean = 1
		if found_mean == 0:
		# Find number of iterations (essentially number of super-columns)
			if "Update_trailing_2 " in line:
				parsed_line = line.split()
				iteration = int(parsed_line[7].translate(None,'[]'))
				if iteration > max_iteration:
					max_iteration = iteration
			continue
		
		# Different dynamic timer cases
		if "LU_factorization_call " in line:
			parsed_line = line.split()
			time = float(parsed_line[2])
			total_fact_time = time
		
		if "Update_trailing_2 " in line:
			parsed_line = line.split()
			time = float(parsed_line[2])
			update2_total += time 
			iteration = int(parsed_line[7].translate(None,'[]'))
			if iteration >= it_bound:
				partial_sum += time 

		if "Update_trailing_1 " in line:
			parsed_line = line.split()
			time = float(parsed_line[2])
			update1_total += time
			iteration = int(parsed_line[7].translate(None,'[]'))
			if iteration >= it_bound:
				partial_sum2 += time 
				
		if "U_compute_and_send " in line:
			parsed_line = line.split()
			time = float(parsed_line[2])
			u_comp_and_send_total += time

		if "L_panel_factorization_loop " in line:
			parsed_line = line.split()
			time = float(parsed_line[2])
			l_panel_fact_total += time

	total_trailing_update = update2_total + update1_total
	trailing_percentage = total_trailing_update / total_fact_time * 100
	l_fact_percentage = l_panel_fact_total / total_fact_time * 100
	u_comp_and_send_percentage = u_comp_and_send_total / total_fact_time * 100
	trailing_perc_after_bound = (partial_sum + partial_sum2) / total_fact_time * 100
	rest = 100 - trailing_percentage - l_fact_percentage - u_comp_and_send_percentage;

	print "Total execution time in seconds:", total_fact_time/1000
	print "Trailing matrix update as percentage ", trailing_percentage, "%"
	print "L factorization as percentage ", l_fact_percentage, "%"
	print "U compute and send as percentage ", u_comp_and_send_percentage, "%"
	print "Rest (horizontal send of L that is overlapped with trailing)", rest, "%"
	print "******************************************"
	print "Supernode count is ", max_iteration
	print "Pecentage spent in trailing updatre after iteration ", it_bound ," is", trailing_perc_after_bound 
					

if __name__ == "__main__":
	main(sys.argv[1:])