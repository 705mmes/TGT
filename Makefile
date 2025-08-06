all : 
	python3 backend/run.py

up:
	docker compose up --build -d

stop:
	docker compose stop

down:
	docker compose down

ps:
	docker compose ps

logs:
	docker compose logs

fclean:
	docker compose down --remove-orphans -v --rmi all