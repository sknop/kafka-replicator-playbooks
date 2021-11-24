This playbook starts up a docker environment with

* 1 ZooKeeper
* 2 Individual Kafka Brokers (kafka-source:9091 and kafka-target:9092)
* 2 Individual Schema Registries (http://schema-registry-source:8091 and http://schema-registry-target:8092)
* 1 Replicator (running as a single node connect cluster) instance using kafka-target as its backing Kafka broker


Start the environment up with provided shell script `up`:
```shell
$> ./up
```
This fires up docker-compose, waits for Kafka Connect to be ready and then sends a curl command to it to set up the replicator.

We are replicating any topic that starts with `schema.`. 
The (Avro) schema in the source will be replicated in the target as a new schema with potentially a new schema id.

Check the status of the replicator using
```shell
curl http://localhost:8083/connectors/replicate-with-schema/status
```

Metrics export via http is enabled, you can use
```shell
curl http://localhost:8083/ReplicatorMetrics
```
and
```shell
curl http://localhost:8083/WorkerMetrics/replicate-with-schema
```
to see replication lag. Keep in mind that it takes 30-60 seconds before the first replication starts.
