# Usage

```sh
docker build -t xxxx/asdf:1415 .
docker run -p 8080:8080 xxx/asdf:1415
```

Then:
```sh
wget http://localhost:8080/ai-ops-ns/flask-app # returns 5 items

# or:

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"horizon":"10"}' \
  http://localhost:8080/ai-ops-ns/flask-app  # returns 10 items
```
