

> Publish-subscibe from HTML <br /><br />
---
> curl http://localhost:5000/list-subscribers <br />
> <br />
> curl -X POST   -H "Content-Type: application/json"   -d '{"name":"Bob","URI":"http://other.good.site.com"}'   http://localhost:5000/add-subscriber <br />
> curl -X DELETE  -H "Content-Type: application/json" -d '{ "name":"Bob" }'  https://localhost:5000 <br />
> curl -X POST -H "Content-Type: application/json"  -d '{ "subject-update": "buy IBM"}' https://obscure-space-halibut-v6q6x5w9r9w2w5jg-5000.app.github
.dev/update-and-notify <br />