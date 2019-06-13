# drf

**About**

Service for convert html to pdf based on Django and djangorestframework

**Deployment**

Clone repo

`git clone https://github.com/blackshadow608/drf.git`

Run script

`. deployment/build_and_run.sh`

**Usage**

By default service running on port 5010
For convert service uses POST requests. 

Use `localhost:5010/api/convert/url/` for convert url to pdf. Expecting field `url` in request in format `http(s)://example.com`

Use `localhost:5010/api/convert/file/` for convert file to pdf. Expecting field `file` in request
