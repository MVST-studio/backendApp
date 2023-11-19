from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get("/")
def read_root():
    return Response(status_code=status.HTTP_200_OK, content="OK")