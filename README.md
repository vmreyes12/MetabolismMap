# Metabolism Map
This code finds proteins based off of the PcrA, PtxD, and IdrA HMMs and maps locations. This code was specifically written to work with metagenome assembled genomes (MAGs) from the Genomes of Earth's Microbiomes (GEM) database provided at:

https://portal.nersc.gov/GEM/genomes/

Be sure to download all MAGs and unpack them into a directory:

```
$ wget https://portal.nersc.gov/GEM/genomes/faa.tar 
$ cd /your/directory/with/genomes/
$ tar -zxvf faa.tar
```
This process is computationally expensive, so running these scripts on a research cluster is recommended. 

## Dependencies


## The Process

### Extract Marker Genes
