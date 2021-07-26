# Air Quality Index Monitor

This app prints, sends SMS and sends email if the AQI of cities/states in the USA go beyond a certain 
threshold.

## Prerequisites:

### Setup an account in twilio
Go to twilio.com and follow the instructions there to be setup with an account.

### Setup Pyenv and Poetry
This repo is intended to be used with Pyenv and Poetry, follow the links below if you don't have these tools setup on your machine.

* [Pyenv Install](https://github.com/pyenv/pyenv#installation)
* [Poetry Install]()

### Setup secrets as ENV VARS

A few secrets need to be set as ENV VARS to use your twilio account to send SMS
```shell
    set TWILIO_AUTH_TOKEN="Your auth token"
    set TWILIO_ACCOUNT_SID="Your account_sid"
    set FROM_MOBILE_NUMBER="Your twilio mobile number"
    set TO_MOBILE_NUMBER="Recipient mobile number"
    set AQI_THRESHOLD="Your floating point number"
``` 

### How to run the application

Run these commands in order

```shell
make init
make lint
make test
make set-env-vars
make get-aqi
```
or run 

```shell
make
```

or

```shell
make all
```
## Current bugs and TODOs:

- Send email funcitonality not implemented
