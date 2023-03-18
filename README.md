## Get started
```shell
cp example.env .env
docker compose up
```
You can find a `swagger` documentation by the following link: `http://localhost:8000/api/v1/swagger/`

## Authentication API
- `POST /api/v1/auth/login/phone/courier/`  
  Request:
  ```json
  {
    "phone": "+36863943434"
  }
  ```
  Response:
  ```json
  {
      "resend_time": 59,
      "is_new_user": false,
      "debug": {
          "cache_exists": true,
          "phone": "+36863943434",
          "test": true,
          "resend_time": 59,
          "check_success": false,
          "_last_send": "2022-03-18T16:55:02.125596Z",
          "_cache_name": "+36863943434otp",
          "_code": "7725",
          "_send": 4,
          "_temporary_blocked": false,
          "_blocked_time": null,
          "_failed_retries_count": 0
      }
  }
  ```
  **Note**: `_code` is a one-time code so-called OTP.
- `POST /api/v1/auth/login/phone/customer/`  
  See above.
- `POST /api/v1/auth/login/phone/verify/`  
  Request:
  ```json
  {
    "phone": "+5928834501",
    "otp_code": "2262"
  }
  ```
  **Note**: you can request the OTP from the endpoints described above.  
  Response:
  ```json
  {
    "access": "access_token",
    "refresh": "refresh_token",
    "debug": {
      "cache_exists": true,
      "phone": "+5928834501",
      "test": true,
      "resend_time": null,
      "check_success": true,
      "_last_send": "2022-03-18T16:55:14.521143Z",
      "_cache_name": "+5928834501otp",
      "_code": "2262",
      "_send": 2,
      "_temporary_blocked": false,
      "_blocked_time": null,
      "_failed_retries_count": 0
    }
  }
  ```
- `POST /api/v1/auth/login/username/`  
  Request:  
  ```json
  {
    "username": "admin",
    "password": "123"
  }
  ```  
  Response:
  ```json
  {
    "refresh": "refresh_token",
    "access": "access_token"
  }
  ```
- `POST /api/v1/auth/login/username/store_worker/`  
  Request:
  ```json
  {
    "username": "worker",
    "password": "123"
  }
  ```  
  Response:
  ```json
  {
    "refresh": "refresh_token",
    "access": "access_token"
  }
  ```
- `POST /api/v1/auth/token/refresh/`  
  Request:
  ```json
  {
    "refresh": "refresh_token"
  }
  ```  
  Response:
  ```json
  {
    "refresh": "refresh_token",
    "access": "access_token"
  }
  ```
