#!/bin/bash

collectionid=$1
port=$2

#echo "removing workingdir"
#rm -rf workingdir
#
#ls -l workingdir

#echo "moving logs and output from old runs"
#mv *.out *.log old_runs 

echo "executing"
python ./generate_story.py -d workingdir -i ${collectionid} -o story-output-${collectionid}-default-`date '+%Y%m%d%H%M%S'`.out -md http://127.0.0.1:${port}/api/damage/ > story-output-${collectionid}-default-`date '+%Y%m%d%H%M%S'`.log 2>&1

echo "done"
