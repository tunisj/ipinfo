# ipinfo
_A simple script to interact with ipinfo.io api_


### Getting Started

You'll need an IPinfo API access token, which you can get by singing up for a free account at [https://ipinfo.io/signup](https://ipinfo.io/signup?ref=lib-Python).

The free plan is limited to 1,000 requests a day, and doesn't include some of the data fields such as IP type and company data. This script will output ipaddress, location, city, region, country, and organization to output.csv. 

#### Installation

```
pip install ipinfo
```

#### Quick Start

```
>>> python ./getipinfo.py
```
#### Usage  
Short Form    | Long Form     | Description
------------- | ------------- |-------------
-i            | --input       | List of IP Addresses to use
-o            | --output      | Save the results to output file
-h            | --help        | Show the help message and exit
-v            | --version     | Show program's version number and exit
