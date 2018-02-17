clean:
	@echo "Cleaning source tree..."
	rm -rf ./shell/node_modules/
	rm -rf site/

before:
	@echo "Installing dependencies..."
	cd ./shell/
	yarn install
