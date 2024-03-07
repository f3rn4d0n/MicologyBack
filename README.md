# MixologyBackend

[![FastApi](https://img.shields.io/badge/FastApi-009485?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)

Cocktails REST API created with [FastAPI](https://fastapi.tiangolo.com)

## Debugin locally

To run FastAPI on your intranet IP with [Uvicorn](https://www.uvicorn.org), first determine your IP address by executing 
```sh
ifconfig
```
 in your terminal and locating it in the `en0` section. Then, execute the following command to run and listen for any changes in your project, updating it locally: 
```sh
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

If you want to stop this process, simply press `control` + `C`.

### Common issues:

**[Errno 48] Address already in use** <br>
If you receive an _Address already in use_ error, it may be because there is already a process running on the same port.
To identify any conflicting processes, you can use the `lsof -i:8000` command and terminate them with the `kill -9 $PID` command. 

## Debugin remotly

Currently we have a demo project working in [Railway](https://fastapi-production-6595.up.railway.app)

## Release
- WIP

## Requirements
- CRUD Cocktails :+1:
- Pagination :+1:
- Resume cocktails :+1:
- Improve list of cocktails
- Sign in and sign up
- Authorization token managment
- Availability of edit only your cocktails or creat a author's cocktails
- Manage app launched version and app state
- Data base connection 
- Migrate all cocktails to database 
- Improve general cocktail managment and adjust cocktails reference to database 
- Home 
- Docker 
- CI/CD 
- Analitics of most importants cocktails 
- Cocktails by seasons 
- Recommended cocktails 
- Favorite cocktails 
Follow people 
Criptography 
Middelware 
Disaster recovery plan 