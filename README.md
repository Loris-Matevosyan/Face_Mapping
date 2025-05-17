<!-- markdownlint-disable MD033 -->

# Facial Mapping Application

<img src="https://static.tildacdn.com/tild3661-3264-4364-a463-313132336335/image.png" alt="Bank System Image" width="550" height="400">

## This project is currently being maintained but is available for use

<br>

## Setup Instructions

This project contains two applications: client-side application and server-side application. Client-side application communicates with the server-side application through a RESTful API. Below is a guide on how to run both applications locally. They will be use localhost IP address(127.0.0.1) and port 5001, so make sure that this port is available.
Make sure to follow the steps below in the correct order. For example running client-side application before the server-side application will result in an error, as the client will have no server available at the specified IP address and port to connect to.

The required Python version is 3.12.<br>
The project was created on Windows OS.
<br><br>

## Steps to run the project

### The project includes client-side application and server-side application

### 1. Create Client-side Application

- __Enter Client_Side directory__
- __Create virtual environment__
  - `py -3.12 -m venv .venv`
- __Install dependencies__
  - `pip install -r requirements.txt`
<br>

### 2. Create Server-side Application

- __Enter Application directory__
- __Create virtual environment__
  - `py -3.12 -m venv .venv`
- __Install dependencies__
  - `pip install -r requirements.txt`

### 3. Run Server-Side Application

- __Enter Application directory__
- __Run application__
  - `python app_api_init`

### 4. Run Client_Side Application

- __Enter Client_Side directory__
- __Run application__
  - `python app.py`
