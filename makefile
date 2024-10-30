clean:
	pre-commit run --all-files

build:
	docker-compose up -d --build

up:
	docker-compose up -d

logs:
	docker-compose logs -f
