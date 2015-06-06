# Catastrophe

# THIS IS WORK IN PROGRESS! DO NOT JUDGE, BUT FEEL FREE TO HELP/SHARE etc. ;)





## Requirements

- [NuPIC](https://github.com/numenta/nupic)
- [Redis](http://redis.io/) running locally
- Python, and [dependencies](requirements.txt)
- [Google Maps Javascript API Key](https://developers.google.com/maps/documentation/javascript/tutorial#api_key)
- Possibly: 
- [Cerebro2](https://github.com/numenta/nupic.cerebro2)
- [MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html)
- [PapaParse](http://papaparse.com/)

## Usage

- Start redis

  ```bash
  $ redis-server
  ```

- Start `run.py`

  ```bash
  $ python run.py
  ```

- Start webapp

  ```bash
  $ cd webapp
  $ API_KEY=<insert API key here> python serve.py
  ```

- Open [http://localhost:8080](http://localhost:8080) in browser

## Usage via VM:

Include your API-Keys in webapp/API_KEYS.py Download and install Docker client, Virtualbox, and Vagrant, and then:

```
source env.sh
vagrant up
docker build -t catastrophe .
docker run --name catastrophe-redis -d -p 0.0.0.0:6379:6379 redis
docker run \
  --name catastrophe-server \
  --link catastrophe-redis:broker \
  -e REDIS_HOST=broker \
  -d \
  -p 0.0.0.0:8080:8080 \
  -w /opt/numenta/catastrophe/webapp \
  catastrophe \
  python serve.py
docker run \
  --link catastrophe-redis:broker \
  -e REDIS_HOST=broker \
  catastrophe \
  python run.py
```

Redis, the catastrophe web service, and the catastrophe entry point are now running
in separate containers in a vm.  You should be able to access the web service
in a browser at [http://localhost:8080](http://localhost:8080)

_________________________________________________________________________________
Thanks to the NuPIC-Community, Austin, Lab75 and many more for help!

This is part of a [TEDx-Project](http://datanauts.tedxrheinmain.de/contest-submissions/natural-catashtrophies-prediction-system/). 
I hope to make the world a saver place by making catastrophe-prediction more efficient.
This may also lead to a nice tool for visualizing all kinds of natural phenomena...  