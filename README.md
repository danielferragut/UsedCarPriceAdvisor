# UsedCarPriceAdvisor
This was a specific project for the Numerical Calculus course, it involves suggesting a price for a used car given a .csv file with informations about prices,mileages and model years of other similar cars. If a .csv with the data needed is not available, you can use one of my web crawlers to get some data for cars in the most famous brazilian used cars sites.
## How to use

If you already have a .csv file, then just run:

```
octave preco_carro.m yourFile.csv
```

The preco_carro.m can be found in the Price Advisor folder

However, if you don't have any data, you can use one of the web crawlers available at the Web Crawlers folder.

The web crawlers are not as easy to use as the Octave file, as they require a little bit of Python knowlodge to understand (and I have yet to comment them). Basically, you are going to have to change the headers to match yours and change "PreSite" to the site you searched your car in, but just until the part about web pages.

For example, if the site that I searched my car was:

```
www.someUsedCarSite/search/idCarPage=2CarModel=654
```

Then Presite is "www.someUsedCarSite/search/idCarPage=" and Possite is "CarModel=654"


## Authors

* **Daniel Ferragut** - *Web Crawlers and assistance on multiple regression*
* **Gabriel Pellegrino** - *Web Craler for "Autoline"(not present in this repo) and  data analys*
* **Matheus  Rotta** - *Main work on multiple regression Octave program* 

