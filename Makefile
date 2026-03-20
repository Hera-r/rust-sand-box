COMPOSE = docker compose

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up -d
	@echo ""
	@echo "Piscine Rust is running at http://localhost:8000"
	@echo ""

down:
	$(COMPOSE) down

reset:
	$(COMPOSE) down -v --remove-orphans
	$(COMPOSE) build --no-cache
	@echo "Reset complete. Run 'make up' to start fresh."

logs:
	$(COMPOSE) logs -f

shell:
	$(COMPOSE) exec web python manage.py shell

ps:
	$(COMPOSE) ps

clean:
	@echo "WARNING: Radically stopping and removing ALL containers, images, and volumes."
	-docker stop $$(docker ps -a -q) 2>/dev/null || true
	-docker rm -f $$(docker ps -a -q) 2>/dev/null || true
	-docker rmi -f $$(docker images -a -q) 2>/dev/null || true
	-docker volume rm $$(docker volume ls -q) 2>/dev/null || true
	docker system prune -a --volumes -f
	@echo "Radical cleanup complete."

.PHONY: build up down reset logs shell ps