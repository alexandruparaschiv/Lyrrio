# Lyrrio



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


Lyrrio is an web-application that can predict the musical genre of some given lyrics. Lyrrio was built by scraping song lyrics using the Python library BeautifulSoup. The algorithm behind Lyrrio's classification is simple TF-IDF (term frequency-inverse term frequency) coupled with a regularised logistic regression. Pull requests and suggestions are welcome. 

### Set-up
### Docker
Lyrrio is easy to set-up locally using docker-compose. Both the front-end and the back-end are served from their respective Docker containers.

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

### Todos

 - Add back-end tests
 - Acquire more data
 - Perform a K-fold Grid search Crossvalidation on 
 - Deploy to GCP using Kubernetes

License
----

MIT
