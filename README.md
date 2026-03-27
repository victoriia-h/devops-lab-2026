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
<img width="1062" height="719" alt="image" src="https://github.com/user-attachments/assets/0c89e92c-addb-405c-bb01-51a43bd78874" />
<img width="1072" height="353" alt="image" src="https://github.com/user-attachments/assets/12eb9579-cf32-46d9-9c4a-1abd193496d0" />


Database Disconnected (503 Service Unavailable):
<img width="1053" height="617" alt="image" src="https://github.com/user-attachments/assets/70628800-454d-43ae-9a1c-7d1e638138bd" />
<img width="1060" height="344" alt="image" src="https://github.com/user-attachments/assets/6e6e2e25-ac21-48e1-a098-5a64e50b3f49" />


## Structured Logging (JSON)
The application uses python-json-logger to output machine-readable logs to STDOUT.
Example of a health check request log:
```json
{"timestamp": "2026-03-20 18:46:14,485", "level": "INFO", "message": "Health check requested"}
