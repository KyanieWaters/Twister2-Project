#!/bin/bash
size=$1
op=$2
echo "Size: "${size}", Operation: "${op}""

./bin/twister2 submit standalone jar examples/libexamples-java.jar edu.iu.dsc.tws.examples.task.ExampleTaskMain -itr 1 -workers 1 -size ${size} -op ${op} -stages 8,1 -verify -stream

