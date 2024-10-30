# nginxLoadBalancerPythonFlask

This is a simple example nginx load balancer on Docker containers.

The load_driver makes JSON requests with "flips":n where n is an integer.
Then a server makes pseudo-randomly coin flips until there is a run of n heads.
The server returns JSON indicating the total number of coin flips required to get
the run of n heads.

The nginx load balancer sends these load_driver requests to
the backend Docker containers to do the work. Nginx distributes the load in a round-robin fashion.

TO get this working:

1. docker-compose up
2. python3 load_driver.py
3. curl -v -X GET "http://localhost:8080/"
4. curl -H "Content-Type: application/json" -d "{\\"heads\\":6 }" -X POST "http://localhost:8080/compute"

# NOTE clear docker containers from the cache
## docker-compose down --rmi all
