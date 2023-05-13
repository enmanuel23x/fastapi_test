start-db:
	docker-compose up -d db
	
start-api-dev:
	cd app && uvicorn main:app --reload --port 5000

start-all:
	docker-compose up --build