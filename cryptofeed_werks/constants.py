import httpx

CRYPTOFEED_WERKS = "cryptofeed-werks"

GOOGLE_APPLICATION_CREDENTIALS = "GOOGLE_APPLICATION_CREDENTIALS"
FIREBASE_ADMIN_CREDENTIALS = "FIREBASE_ADMIN_CREDENTIALS"
PROJECT_ID = "PROJECT_ID"
SERVICE_ACCOUNT = "SERVICE_ACCOUNT"
BIGQUERY_LOCATION = "BIGQUERY_LOCATION"
BIGQUERY_DATASET = "BIGQUERY_DATASET"
BIGQUERY_TABLES = "BIGQUERY_TABLES"
SENTRY_DSN = "SENTRY_DSN"

GCP_APPLICATION_CREDENTIALS = (
    GOOGLE_APPLICATION_CREDENTIALS,
    FIREBASE_ADMIN_CREDENTIALS,
)

LOCAL_ENV_VARS = (
    GOOGLE_APPLICATION_CREDENTIALS,
    FIREBASE_ADMIN_CREDENTIALS,
    PROJECT_ID,
    SERVICE_ACCOUNT,
    BIGQUERY_LOCATION,
    BIGQUERY_DATASET,
)


PRODUCTION_ENV_VARS = (
    PROJECT_ID,
    BIGQUERY_LOCATION,
    BIGQUERY_DATASET,
    SENTRY_DSN,
)


HTTPX_ERRORS = (
    httpx.ConnectError,
    httpx.ConnectTimeout,
    httpx.ReadError,
    httpx.ReadTimeout,
)