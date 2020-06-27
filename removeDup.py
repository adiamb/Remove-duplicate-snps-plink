import subprocess
from subprocess import PIPE
import argparse


def processTped(tped):
    snpDict = {}
    dupCounter =0
    makeOut = tped.replace('.tped', 'duprm.tped')
    tpedOut = open(makeOut, 'w')
    with open(tped) as inFile:
        for n, line in enumerate(inFile):
            lineParse = line.strip().split(' ')
            makeKey = lineParse[0]+':'+lineParse[3]
            if makeKey not in snpDict:
                snpDict[makeKey] =''
                tpedOut.write(line)
            else:
                dupCounter += 1
            if n % 10000 == 0:
                print('PROCESSED {} VARIANTS '.format(n))
    print('DUPLICATE {} VARS FOUND'.format(dupCounter))
    tpedOut.close()

def plinkBedconv(duprmTepd, tped):
	makeCommand = 'plink --tfile '+duprmTepd.replace('.tped', '')+' --allow-extra-chr --make-bed --out '+duprmTepd.replace('.tped', '')
	copyFam = subprocess.Popen('cp '+tped.replace('.tped', '.tfam')+' '+ duprmTepd.replace('.tped', '.tfam'), shell=True, stdout=PIPE, stderr=PIPE)
	stdout, stderr = copyFam.communicate()
	if stderr:
		print('ERROR !!! Check if Tfam is in working dir')
	else:
		call_ = subprocess.Popen(makeCommand, shell=True, stdout = PIPE, stderr=PIPE)
		stdout, stderr = call_.communicate()
		if stdout:
			print(stdout)  

def main():
    parser = argparse.ArgumentParser(description='Duplicate Position Removal Script for Pre-Phasing')
    parser.add_argument('-T', help='Tped File to be processed', required=True)
    args=parser.parse_args()
    tped=args.T
    duprmTepd = tped.replace('.tped', 'duprm.tped')
    processTped(tped=tped)
    plinkBedconv(duprmTepd=duprmTepd, tped=tped)
    
if __name__ == "__main__":main()
