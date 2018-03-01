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
	rm -rf ./tools/doc_server/templates/api.html
	mkdir api_site
	snowboard html -o ./api_site/index.html ./blueprints/v1.apib
	mv ./api_site/index.html ./tools/doc_server/templates/api.html
	rm -rf api_site

requirement:
	@echo "Generating locked.txt ..."
	rm -f ./requirements/locked.txt
	pipenv lock -r >> ./requirements/locked.txt
