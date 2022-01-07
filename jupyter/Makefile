build:
	docker build -t af/lp-jupyter .

run:
	docker run -p 8889:8889 --mount type=bind,source="$(CURDIR)",target=/src af/lp-jupyter
