# flask-mysql
### Overview
This is Flask+MySQL RESTful API which is very simple, so it's easy to learn everyone.
### Description
### Usage
Firslty, you need to verify the flask-mysql clusterIP(i.e 10.101.20.201)
<pre>kubectl get svc
NAME          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
flask-mysql   ClusterIP   10.101.20.201    <none>        8080/TCP         79s
</pre>

#### add user
<pre>
curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d  '{"email":"hogehoge@xxxx.net","name":"kissy1","pwd":"secret1"}' [clusterIP]:8080/add
"User added successfully!"</pre>

#### show users
<pre>
curl [clusterIP]:8080/users
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
</pre>

#### show specific user
<pre>
curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"user_id":"4"}' [clusterIP]:8080/user
{
  "user_email": "hogehoge@xxxx.net", 
  "user_id": 4, 
  "user_name": "kissy1", 
  "user_password": "pbkdf2:sha256:150000$J7k3r9fb$f48004429125b53e17612b9d38e7e8fb3f837d69ad3c550453857abb38d33c79"
}
</pre>

#### update user
<pre>
curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d  '{"user_id":"4","email":"ukiuki@xxxx.net","name":"kissy4","pwd":"secret4"}' [clusterIP]:8080/update
"User updated successfully!</pre>

#### delete user
<pre>
curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"user_id":"3"}' [clusterIP]:8080/delete
"User deleted successfully!"</pre>

### Install
1.Make sure to make directory for pv on master and worker node
<pre>hogeuser@k8s-master:~/flask-mysql$ sudo mkdir /mnt/data</pre>
2.make pods
<pre>kubectl apply -f https://raw.githubusercontent.com/kissycomjp/flask-mysql/master/k8s-yaml/flask-mysql.yaml</pre>

### Blockquotes
https://www.serverlab.ca/tutorials/containers/kubernetes/how-to-run-flask-docker-containers-in-kubernetes/

### Licence
### Author
