import os
import httpx

USER_SERVICE_HOST_URL="http://docker.for.mac.localhost:8002/api/v1/jobs/"

def is_jobs_present(id: int):
    url = os.environ.get('CAST_SERVICE_HOST_URL') or USER_SERVICE_HOST_URL
    r = httpx.get(f'{url}{id}')
    print("R: ", r)
    return True if r.status_code == 200 else False