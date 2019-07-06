# flask-mysql
### Overview
This is Flask+MySQL RESTful API which is very simple, so it's easy to learn everyone.
### Description
### Usage
#### show users
curl 127.0.0.1:8080/users
[
  {
    "user_email": "hogehoge@xxxx.net", 
    "user_id": 4, 
    "user_name": "kissy1", 
    "user_password": "pbkdf2:sha256:150000$J7k3r9fb$f48004429125b53e17612b9d38e7e8fb3f837d69ad3c550453857abb38d33c79"
  }, 
  {
    "user_email": "fugafuga@xxxx.net", 
    "user_id": 5, 
    "user_name": "kissy2", 
    "user_password": "pbkdf2:sha256:150000$i3eVWxGd$0e1da13a18cee90719e71812e363412089f5704574bb60efb4d30c5f9f673159"
  }, 
  {
    "user_email": "ugeuge@xxxx.net", 
    "user_id": 6, 
    "user_name": "kissy3", 
    "user_password": "pbkdf2:sha256:150000$GV2bxCDm$8468183bb39635c647a5a920777f9b0a7ec817ce5090a863d733315a1fd5b9a0"
  }
]

#### show specific user
curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"user_id":"4"}' 127.0.0.1:8080/user
{
  "user_email": "hogehoge@xxxx.net", 
  "user_id": 4, 
  "user_name": "kissy1", 
  "user_password": "pbkdf2:sha256:150000$J7k3r9fb$f48004429125b53e17612b9d38e7e8fb3f837d69ad3c550453857abb38d33c79"
}
#### update user
curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d  '{"user_id":"4","email":"ukiuki@xxxx.net","name":"kissy4","pwd":"secret4"}' 127.0.0.1:8080/update
"User updated successfully!

#### add user
curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d  '{"email":"hogehoge@xxxx.net","name":"kissy1","pwd":"secret1"}' 127.0.0.1:8080/add

#### delete user
curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"user_id":"3"}' 127.0.0.1:8080/delete
"User deleted successfully!"

### Install
kubectl apply -f https://raw.githubusercontent.com/kissycomjp/flask-mysql/master/k8s-yaml/flask-mysql.yaml

### Contribution
### Licence
### Author
