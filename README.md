### Collector for IFPRI's Datasets
[![Build Status](https://travis-ci.org/luiscape/hdxscraper-ifpri-dataverse.svg?branch=master)](https://travis-ci.org/luiscape/hdxscraper-ifpri-dataverse) [![Coverage Status](https://coveralls.io/repos/luiscape/hdxscraper-ifpri-dataverse/badge.svg?branch=master&service=github)](https://coveralls.io/github/luiscape/hdxscraper-ifpri-dataverse?branch=master)

Collector designed to collect datasets from the [IFPRI](http://www.ifpri.org/) repository on [Harvard's Dataverse](https://dataverse.harvard.edu/dataverse/IFPRI). The collector took into consideration high level classes to make the process of collecting data from a different repository on a Dataverse easier.

### Usage
Use `Makefile` instructions as follows:

```shell
$  make setup && make test
$  make run
```

If you are interested in also registering datasets on HDX, run:

```shell
$  make register
```

You will need to set the environment variable `HDX_KEY` before running the registering option. That option was created to automatically register datasets on the [Humanitarian Data Exchange](http://data.hdx.rwlabs.org/) project.
