init:
	pipenv install --dev

config:
	@echo "[default]" > config.ini
	@echo "api_url=${SHMENKINS_API_URL}" >> config.ini

test:
	@pipenv run pytest shmenkins
