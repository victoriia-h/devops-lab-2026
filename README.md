# Robot Dialogue Subsystem

This is a Commerce-Ready FastAPI application for a Robot Speech-to-Text dialogue subsystem.

## Configuration (Environment Variables)
To run the application, create a .env file in the root directory with the following variables:
* DB_HOST
* DB_PORT
* DB_NAME
* DB_USER
* DB_PASSWORD

## Health Check Verification

Database Connected (200 OK):
<img width="861" height="285" alt="image" src="https://github.com/user-attachments/assets/83887639-f092-4c45-9f33-d647d15e0426" />
<img width="855" height="580" alt="image" src="https://github.com/user-attachments/assets/7191a4e0-b9e1-468f-928e-e9f836c7865b" />

Database Disconnected (503 Service Unavailable):
<img width="854" height="282" alt="image" src="https://github.com/user-attachments/assets/606cc6d5-efb3-4f10-9f49-2f4426fd72ec" />
<img width="847" height="497" alt="image" src="https://github.com/user-attachments/assets/b6e86af0-a941-4911-8c89-824d111c3eff" />

## Structured Logging (JSON)
The application uses python-json-logger to output machine-readable logs to STDOUT.
Example of a health check request log:
```json
{"timestamp": "2026-03-20 18:46:14,485", "level": "INFO", "message": "Health check requested"}
