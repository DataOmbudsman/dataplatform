# dataplatform

My progress through the Manning LiveProject course [Create a Data Platform for Real-time Anomaly Detection](https://www.manning.com/liveproject/create-a-data-platform-for-real-time-anomaly-detection).

## Notes

Some useful commands:
```
docker build -t af/lp-jupyter .  # build image

docker run -p 8889:8889 af/lp-jupyter  # create container from image

docker run -p 8889:8889 --mount type=bind,source="$(pwd)",target=/src af/lp-jupyter  # ... with bind mount
```

```
docker-compose up --build  # boot with building image

docker-compose up --build  # boot with building image and detached mode

docker-compose ps  # list of running containers

docker-compose stop  # stops containers

docker-compose down  # stops and removes containers

docker-compose down && docker-compose up --build  # reboot

ADMIN_USER=admin ADMIN_PASSWORD=admin docker-compose down && docker-compose up --build -d  # start with setting default username/password
```

## Components

- FastAPI: web framework
- Prometheus: monitoring system
- Grafana: dashboard
- Caddy: reverse proxy service used for authentication 

### Access

- http://localhost:8000/metrics/ — Prometheus raw metrics
- http://localhost:9090/graph — Prometheus console
- http://localhost:8000/docs  — API docs
- http://localhost:3000/?orgId=1 — Grafana
