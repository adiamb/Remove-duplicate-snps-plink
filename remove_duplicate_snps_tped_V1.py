import re
import time
import sys
import subprocess 
from subprocess import PIPE


def remove_dups(in_file):
	snp_dic={}
	line_ =0
	line_buffer =0
	duplicate_counter =0
	valid_snps =0
	make_out_f = in_file.replace('.tped', 'duprm.tped')
	tped_out = open(make_out_f, 'wr')
	with open(in_file) as tped_in:
		for line in tped_in:
			line_ += 1
			if line_ == 1000:
				line_buffer += 1000
				line_ =0
				print " PROCESSED LINES ", line_buffer
			if line:
				line_parse = line.strip().split(' ')
				make_key = '$'.join(line_parse[:4])
				if make_key not in snp_dic:
					snp_dic[make_key] = line
					valid_snps += 1
					tped_out.write(line)

				else:
					duplicate_counter += 1
		tped_out.close()
		print "FOUND DUPLICATES ", str(duplicate_counter), "VALID SNPS FOUND ", str(valid_snps)

def plink_bed_conv(duprmtepd, in_file):
	make_command = 'plink --tfile '+duprmtepd.replace('.tped', '')+' --allow-extra-chr --make-bed --out '+duprmtepd.replace('.tped', '')
	copy_fam = subprocess.Popen('cp '+in_file.replace('.tped', '.tfam')+' '+ duprmtepd.replace('.tped', '.tfam'), shell=True, stdout=PIPE, stderr=PIPE)
	stdout, stderr = copy_fam.communicate()
	if stderr:
		print 'ERROR !!!'
	else:
		call_ = subprocess.Popen(make_command, shell=True, stdout = PIPE, stderr=PIPE)
		stdout, stderr = call_.communicate()
		if stdout:
			print stdout



def main(argv):
	in_file = sys.argv[1]
	duprmtepd=in_file.replace('.tped', 'duprm.tped')
	remove_dups(in_file)
	plink_bed_conv(duprmtepd, in_file)

if __name__ == '__main__': main(sys.argv)





















#DEBUGGING
# snp_dic={}
# line_ =0
# line_buffer =0
# duplicate_counter =0
# valid_snps =0
# with open('Plate98QC.tped') as tped_in:
# 	for line in tped_in:
# 		line_ += 1
# 		if line_ == 1000:
# 			line_buffer += 1000
# 			line_ =0
# 			print " PROCESSED LINES ", line_buffer
# 		if line:
# 			line_parse = line.strip().split(' ')
# 			make_key = '$'.join(line_parse[:4])
# 			if make_key not in snp_dic:
# 				snp_dic[make_key] = line
# 				valid_snps += 1
# 			else:
# 				duplicate_counter += 1

# 	print "FOUND DUPLICATES ", str(duplicate_counter), "VALID SNPS FOUND ", str(valid_snps)
