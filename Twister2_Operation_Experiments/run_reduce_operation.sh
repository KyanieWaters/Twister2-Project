size=$1
./bin/twister2 submit standalone jar examples/libexamples-java.jar edu.iu.dsc.tws.examples.task.ExampleTaskMain -itr 1 -workers 1 -size ${size} -op "reduce" -stages 8,1 -verify -stream
