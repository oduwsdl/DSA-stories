#!/bin/bash

now=`date +'%Y-%m-%d-%H:%M:%S'`

mdport=$1
coll_id=$2

if [ -z "$mdport" ]; then
    echo "port not set"
    exit 1
fi

if [ -z "$coll_id" ]; then
    echo "collection id not set"
    exit 1
fi

echo "using port ${mdport} for memento damage service"
echo "working on collection ${coll_id}"

outputdatafile="output-ExtractTextFromHTMLFromSeedList-${coll_id}-${now}"
outputlogfile="run-ExtractTextFromHTMLFromSeedList-${coll_id}-${now}"

echo "logging in file ${outputlogfile}"
echo "data in file ${outputdatafile}"

python generate_story.py -md http://localhost:${mdport}/api/damage -d download_dir-ExtractTextFromHTMLFromSeedList -o ${outputdatafile} -i ${coll_id} > ${outputlogfile} 2>&1
