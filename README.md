# Remove-duplicate-snps-plink
A python script to remove duplicate snps from plink files and recode the resultant files into plink binaries free of duplicate snps
plink needs to be installed and in shell path, A .tped file needs to be given to the script
you can generate a .tped file by
plink --bfile XXX --recode transpose XXX 
will match on the chr:pos so multi-alleleic variants will be explicitly filtered keeping the first instance
# An example command to the script is then
```python removeDup.py -T your_tpedfile.tped``` 
