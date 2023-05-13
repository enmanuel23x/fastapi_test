help: ## Display available commands and their descriptions
	@echo 'usage: make [target]'
	@echo
	@echo 'targets:'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

start-db: ## Start the database service
	docker-compose up -d db
	
start-api-dev: ## Start the API development server
	cd app && uvicorn main:app --reload --port 5000

start-all: ## Start all services (database and API)
	docker-compose up --build