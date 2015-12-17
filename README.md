### Collector for IFPRI's Datasets
Collector designed to collect datasets from the IFPRI repository on [Harvard's Dataverse](https://dataverse.harvard.edu/dataverse/IFPRI). The collector took into consideration high level classes to make the process of collecting data from a different repository on a Dataverse easier.

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

You will need to set the environment variable `HDX_KEY` on `bin/run.sh` before running the registering option. That option was created to register datasets on the [Humanitarian Data Exchange](http://data.hdx.rwlabs.org/) project.
