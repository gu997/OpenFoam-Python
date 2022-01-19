#!/bin/bash


decomposePar -force
mpirun -np 10 interPhaseChangeFoam -parallel
reconstructPar -latestTime
