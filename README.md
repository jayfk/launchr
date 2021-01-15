<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://raw.githubusercontent.com/jayfk/launchr/master/logo.png" alt="Launchr"></a>
</p>

<h3 align="center">Launchr</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![codecov](https://codecov.io/gh/jayfk/launchr/branch/master/graph/badge.svg)](https://codecov.io/gh/jayfk/launchr)
[![GitHub Issues](https://img.shields.io/github/issues/jayfk/launchr.svg)](https://github.com/jayfk/launchr/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/jayfk/launchr.svg)](https://github.com/jayfk/launchr/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 
    Launchr is an open source SaaS starter kit.<br> 
</p>

## Getting Started <a name = "getting_started"></a>

Launchr is at an early stage. It's fully functional, but missing documentation. If you want to try it out, follow the
examples below.

### Prerequisites

Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

### Installing

To create a new project, open up a terminal and clone Launchr to your current working directory:

```
git clone https://github.com/jayfk/launchr.git
```

Move the repository you just cloned to the one your are going to use for your project:

```
mv launchr project_name
```

Switch to your newly created project directory and start the stack:

```
cd project_name
docker-compose up
```

Once Docker is finished downloading and building, open up a second terminal and run the initial migrations for the
project:

```
docker-compose run app python manage.py migrate
```

You should now be able to reach your local development server by
visiting [http://localhost:8000/](http://localhost:8000/).

### Where to go from here?

I'm currently still writing the Documentation. If you get stuck at any point, open up an issue on GitHub.

## Documentation

Click here to find the [Documentation](https://getlaunchr.com/docs/). 


