# Metabolism Map
This code finds proteins based off of the PcrA, PtxD, and IdrA HMMs and maps locations. This code was specifically written to work with metagenome assembled genomes (MAGs) from the Genomes of Earth's Microbiomes (GEM) database provided at:

https://portal.nersc.gov/GEM/genomes/

Be sure to download all MAGs and unpack them into a directory:

```
$ wget https://portal.nersc.gov/GEM/genomes/faa.tar 
$ wget https://portal.nersc.gov/GEM/genome_metadata.xlsx 
$ cd /your/directory/with/genomes/
$ tar -zxvf faa.tar
```
Keep the genome metadata in your working directory. It will be needed later.

This process is computationally expensive, so running the shell script on a research cluster is recommended. 
If done on a cluster, you must modify the shell scripts to make them executable on the cluster. 
The python script can be run on the cluster, however, a step requires your favorite spreadsheet viewer, so downloading your results is recommended.

## Dependencies
Install [HMMER](hmmer.org)
```
$ wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2.tar.gz
$ tar -zxvf hmmer-3.1b2.tar.gz
$ cd hmmer-3.1b2
$ ./configure && make && sudo make install
$ cd easel && make check && sudo make install
```

Install Python and make sure you have the following packages.
- [Python 3.7](https://www.python.org/downloads/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Cartopy](https://scitools.org.uk/cartopy/docs/latest/installing.html)


## The Process

### 1. Extract Marker Genes
The first step will iterate through every file in the faa directory and search iteratively through each HMM provided in the HMM folder. 
```
$ chmod +x ./HMMMetSearch.sh
$ ./HMMMetSearch.sh
```

This will create multiple files with the prefix of your metabolism of interest:
- __hits.txt__: This contains the raw output for the HMM search of each faa file. It includes empty hits. Useful for troubleshooting.
- __clean.txt__: This file takes out hits from the hits file and lists the raw HMM output of positive results. Again, useful for troubleshooting. 
- __target.txt__: This contains all the cleaned data, along with the source of each hit. This file is necessary for your code later on. 

### 2. Delimit your target.txt files
This step is manual. I may work on a script depending on how others adopt this script. For now, you have to open the target files in the saved directory with your favorite spreadsheet viewer. Set "./" as your custom delimiter and open your file. Add an additional row on top, and label row G (which is your numeric row) as "genome_id".  

Save each file as the in the format of MetabolismName_target_file.xlsx, where Metabolism Name stands in for the HMM you used to search for a metabolism (e.g., idrA_target_file.xlsx

### 3. Generate Fun Graphs
This step, you just need to run the script 
```
$ python Metabolism Finder.py
```
Ensure that dependencies are installed.
Running this script will put out svg files of various datatypes.
Examples below:

_Taxonomic Distribution_
![image](https://user-images.githubusercontent.com/27031932/142695925-c9a8ef5b-49f0-46e1-a73b-e0e9936f0f02.png)

_Another way of viewing the same data_
![image](https://user-images.githubusercontent.com/27031932/142695969-251c1016-2126-4521-b94f-da3df63f3634.png)

_Distribution Map_
![image](https://user-images.githubusercontent.com/27031932/142696004-ae30f930-65b4-41ec-8daf-dd2bdd4dd047.png)


