#!/bin/bash
FILES=./faa/faa/*
HMM_pcrA1=./HMMs/pcrA1.hmm
HMM_pcrA2=./HMMs/pcrA1.hmm
HMM_idr=./HMMs/iriA_new.hmm
HMM_ptx=./HMMs/ptxd.hmm

for f in $FILES
do
  echo reading the file $f >> ./JGI_data_output/pcrA1_hits.txt
  hmmsearch --noali --tblout ./JGI_data_output/pcrA1_seq.txt -T 800 $HMM_pcrA1 $f >> ./JGI_data_output/pcrA1_hits.txt
done
grep -B 21 '>>' ./JGI_data_output/pcrA1_hits.txt >> ./JGI_data_output/pcrA1_clean.txt
grep '# target' ./JGI_data_output/pcrA1_clean.txt >> ./JGI_data_output/pcrA1_target.txt

for f in $FILES
do
  echo reading the file $f >> ./JGI_data_output/pcrA2_hits.txt
  hmmsearch --noali --tblout ./JGI_data_output/pcrA2_seq.txt -T 1000 $HMM_pcrA2 $f >> ./JGI_data_output/pcrA2_hits.txt
done
grep -B 21 '>>' ./JGI_data_output/pcrA2_hits.txt >> ./JGI_data_output/pcrA2_clean.txt
grep '# target' ./JGI_data_output/pcrA2_clean.txt >> ./JGI_data_output/pcrA2_target.txt

for f in $FILES
do
  echo reading the file $f >> ./JGI_data_output/idrA_hits.txt
  hmmsearch --noali --tblout ./JGI_data_output/idrA_seq.txt -T 640 $HMM_idr $f >> ./JGI_data_output/idrA_hits.txt
done
grep -B 21 '>>' ./JGI_data_output/idrA_hits.txt >> ./JGI_data_output/idrA_clean.txt
grep '# target' ./JGI_data_output/idrA_clean.txt >> ./JGI_data_output/idrA_target.txt

for f in $FILES
do
  echo reading the file $f >> ./JGI_data_output/ptxD_hits.txt
  hmmsearch --noali --tblout ./JGI_data_output/ptxD_seq.txt -T 350 $HMM_ptx $f >> ./JGI_data_output/ptxD_hits.txt
done
grep -B 21 '>>' ./JGI_data_output/ptxD_hits.txt >> ./JGI_data_output/ptxD_clean.txt
grep '# target' ./JGI_data_output/ptxD_clean.txt >> ./JGI_data_output/ptxD_target.txt



