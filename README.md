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

## Sample Twilio SMS message with threshold > 100:

```
Sent from your Twilio trial account - -

1. State: California
   City: Paradise
   Pollutant: PM2.5
   AQI: 137

2. State: California
   City: Portola
   Pollutant: PM2.5
   AQI: 267

3. State: California
   City: Quincy
   Pollutant: PM2.5
   AQI: 255

4. State: California
   City: Truckee
   Pollutant: PM2.5
   AQI: 209

5. State: Nevada
   City: Carson City
   Pollutant: PM2.5
   AQI: 207

6. State: Nevada
   City: Gardnerville
   Pollutant: PM2.5
   AQI: 192

7. State: Nevada
   City: Reno-Sparks
   Pollutant: PM2.5
   AQI: 198

8. State: Utah
   City: Salt Lake City
   Pollutant: PM2.5
   AQI: 131

9. State: Washington
   City: Omak
   Pollutant: PM2.5
   AQI: 146

10. State: Washington
   City: Twisp
   Pollutant: PM2.5
   AQI: 155

11. State: Washington
   City: Winthrop
   Pollutant: PM2.5
   AQI: 200

12. State: Oregon
   City: Klamath Falls
   Pollutant: PM2.5
   AQI: 105

```

