# Redis Credentials tests

Runs a simple loopback test

## Usage

example shows default values

```
docker run -it --rm \
-e REDIS_HOST="localhost" \
-e REDIS_PORT="6379" \
-e REDIS_PASSWORD="password"  \
-e REDIS_DB="0"  \
jonaseck/redis-credentials-test
```