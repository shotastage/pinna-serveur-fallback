#
# This makefile is not for building!
#

clean:
	@echo "Cleaning source tree..."
	rm -rf ./shell/node_modules/
	rm -rf site/

before:
	@echo "Installing dependencies..."
	cd ./shell/
	yarn install


#######
# NEW #
#######

pyclean:
	find ./mirage -name '*.pyc' -delete -not -path './mirage/scaffold/static/'

apib:
	mkdir api_site
	snowboard html -o ./api_site/index.html ./blueprints/v1.apib
