#!/usr/bin/env bash

export HOME
export FREESURFER_HOME
export SUBJECTS_DIR
source ${FREESURFER_HOME}/FreeSurferEnv.sh

f=$PWD

recon-all -autorecon3 -T2 $2 -T2pial -parallel -openmp $3 -s $1

cd ${SUBJECTS_DIR}/$1/mri
cp aparc+aseg.mgz $f

cd ../surf
cp lh.pial $f
cp rh.pial $f

cd ../label
cp lh.aparc.annot $f
cp rh.aparc.annot $f