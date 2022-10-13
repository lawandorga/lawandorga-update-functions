pipenv requirements > requirements.txt
pipenv run pip install -r requirements.txt --target ./package
serverless deploy
docker run --rm -v $(pwd):/home/app/function --workdir /home/app/function rg.fr-par.scw.cloud/scwfunctionsruntimes-public/python-dep:3.10 pip install -r requirements.txt --target ./package