# Variables
PYTHON=python3
PIP=pip3
FLASK_APP=app.py
FLASK_ENV=development

# Dependencies
REQUIREMENTS=requirements.txt

# Install dependencies
install:
	$(PIP) install -r $(REQUIREMENTS)

# Run Flask server
run:
	$(PYTHON) -m flask run --host=0.0.0.0 --port=5000

# Build Docker image
build:
	docker build -t game-sales-app .

# Run Docker container
run-container:
	docker run -p 5000:5000 game-sales-app

# Clean up
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache

# Set up development environment
dev: clean install run

# Set up production environment
prod: clean install build run-container