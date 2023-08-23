# DLUHC Datasets

A tool to manage DLUHC's datasets. For example, the listed-building-grade dataset.


## Quick start

Make python virtualenv then:

    make init

Create a postgres db:

    createdb dluhc-datasets

Make the db tables:

    make upgrade

Load the data:

    make load
