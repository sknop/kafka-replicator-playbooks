
function wait_for_connect {
  docker-compose logs connect | grep "Kafka Connect started"
  while (( $? == 1 ))
  do
    sleep 1
    echo "Waiting for connect to be started ..."
    docker-compose logs connect | grep "Kafka Connect started"
  done
}