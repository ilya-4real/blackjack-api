PC = podman-compose
EXEC = podman-compose exec -it
APP_FILE = compose/app.yaml
PD = podman
APP_CONTAINER = main-app
ENV = --env-file .env


.PHONY: app
app:
	${PC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${PC} -f ${APP_FILE} down

.PHONY: app-logs
app-logs:
	${PD} logs -f ${APP_CONTAINER} 