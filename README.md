# MicologyBack

Cocktails REST API created with [FastAPI](https://fastapi.tiangolo.com)

## Debugin locally

To run FastAPI on your intranet IP with [Uvicorn](https://www.uvicorn.org), first determine your IP address by executing 'ifconfig' in your terminal and locating it in the 'en0' section. Then, execute the following command to run and listen for any changes in your project, updating it locally: 'uvicorn app.main:app --reload --host 0.0.0.0'.
If you want to stop this process, simply press 'control' + 'C'.

### Common issues:

**[Errno 48] Address already in use**
If you receive an 'Address already in use' error, it may be because there is already a process running on the same port.
To identify any conflicting processes, you can use the 'lsof -i:8000' command and terminate them with the 'kill -9 $PID' command. 

## Debugin remotly

Currently we have a demo project working in [Railway](https://fastapi-production-6595.up.railway.app)

## Release
- WIP