### Backend build and run
```
docker build -t weeklypulls_backend .
sudo docker run \
  -e DATABASE_URL="FILL IN" \
  -e DJANGO_SECRET_KEY="FILL IN" \
  -e MAPI_PUBLIC_KEY="FILL IN" \
  -e MAPI_PRIVATE_KEY="FILL IN" \
  -p 8000:8000 \
  weeklypulls_backend
```

### Frontend build and run
```
docker build -t weeklypulls_frontend .
docker rm wp_front
sudo docker run \
  -t \
  -i \
  -p 8080:8080 \
  --name wp_front \
  weeklypulls_frontend
```
