PY?=
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif

TIMESTAMP := $(shell date +"%s")

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make devserver-global               regenerate and serve on 0.0.0.0    '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver-global:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b 0.0.0.0

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

docker-build:
	pdm sync --no-editable
	pdm update
	docker build --build-arg CACHEBUST=$(TIMESTAMP) -t 202092910073.dkr.ecr.us-east-1.amazonaws.com/codebuild/dltj-pelican-runner\:latest -t dltj-pelican-runner\:latest .
	pdm run python -m pip install -e ../pelican-personal
	pdm run python -m pip install -e ../pelican-dltj-plugin
	pdm run python -m pip install -e ../pelican-papyrus-theme

docker-serve:
	docker run --rm -v "$(CURDIR)/assets:/app/assets" -v "$(CURDIR)/content:/app/content" -v "$(CURDIR)/output:/app/output" -v "$(CURDIR)/root-content:/app/root-content" -p 8000\:8000 dltj-pelican-runner -lr content -s pelicanconf.py -o output -t /app/pelican-themes/pelican-papyrus-theme -b 0.0.0.0

docker-push:
	aws --profile dltj-admin ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 202092910073.dkr.ecr.us-east-1.amazonaws.com
	docker push 202092910073.dkr.ecr.us-east-1.amazonaws.com/codebuild/dltj-pelican-runner:latest

.PHONY: html help clean regenerate serve serve-global devserver devserver-global publish docker-build docker-serve docker-push