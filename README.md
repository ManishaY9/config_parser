# CPU Usage Monitor

A Python-based API that parses configuration files and serves their content as JSON via a RESTful interface. This tool simplifies configuration management by extracting key-value pairs from .ini files and providing easy access to the data through HTTP endpoints.

## Features
- Efficient parsing of .ini configuration files
- Serves configuration data via RESTful API
- Retrieve the entire configuration or specific sections.

---

## Requirements

- Python 3.6 or higher
- Flask library installed

## Usage

### Running the API Server
Start the server with the following command:
```bash
python config_api.py
```
The server will run on http://127.0.0.1:5000 by default.
1. **Retrieve Full Configuration**  
   Endpoint: `GET /config`  
   Returns the entire configuration file as JSON.  
   Example:
   ```json
   {
       "Database": {
           "host": "localhost",
           "port": "3306",
           "username": "admin",
           "password": "secret"
       },
       "Server": {
           "address": "192.168.0.1",
           "port": "8080"
       }
   }
   ```

2. **Retrieve Specific Section**  
   Endpoint: `GET /config/<section>`  
   Replace `<section>` with the section name from the configuration file.  
   Example:  
   `GET /config/Database`  
   Response:
   ```json
   {
       "host": "localhost",
       "port": "3306",
       "username": "admin",
       "password": "secret"
   }
   ```
