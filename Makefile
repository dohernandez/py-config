NO_COLOR=\033[0m
COLOR=\033[32;01m

PROJECT_NAME = pyconfig
IMAGE_NAME = dohernandez/$(PROJECT_NAME)
CONTAINER_NAME = $(PROJECT_NAME)

# do not edit the following lines
# for shell usage

all: usage

usage:
	@echo "build:  Build the docker image for the project."
	@echo "freeze:  Print all the python package installed in the docker image."

build:
	@printf "$(COLOR)==> Building docker image ...$(NO_COLOR)\n"
	@docker build -t $(IMAGE_NAME) .

freeze:
	@printf "$(COLOR)==> Checking python dependencies installed in the image ...$(NO_COLOR)\n"
	@docker run -it --rm --name $(CONTAINER_NAME) $(IMAGE_NAME) pip freeze

tests:
	@printf "$(COLOR)==> Checking python dependencies installed in the image ...$(NO_COLOR)\n"
	@docker run -it --rm --name $(CONTAINER_NAME) -v $(PWD):/src/py-config $(IMAGE_NAME) \
	nosetests --nocapture --nologcapture --detailed-errors --verbosity=2 --traverse-namespace \
	--with-coverage --cover-erase --cover-package=pyconfig --rednose /src/py-config/tests


.PHONY: all usage build tests
