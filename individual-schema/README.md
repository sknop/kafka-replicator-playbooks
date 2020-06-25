This playbook starts up a docker environment with

1 ZooKeeper
2 Individual Kafka Brokers (kafka-source:9091 and kafka-target:9092)
2 Individual Schema Registries (http://schema-registry-source:8091 and http://schema-registry-target:8092)
1 Connect instance using kafka-target as its backing Kafka broker

There is a also a replicator instance, but we are just going to use that to nick the jar files we need (thanks to Rick Spurgeon for the idea)

Start the environment up with provided shell script up: 

$> ./up

This fires up docker-compose, waits for Kafka Connect to be ready and then sends a curl command to it to set up the replicator.

We are replicating any topic that starts with "schema." 
The (Avro) schema in the source will be replicated in the target as a new schema with potentially a new schema id.

