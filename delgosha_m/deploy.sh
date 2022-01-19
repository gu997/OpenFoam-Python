#!/bin/bash

source $HOME/.bashrc
openFoam
decomposePar -force
mpirun -np 10 interPhaseChangeFoam -parallel
reconstructPar -latestTime
