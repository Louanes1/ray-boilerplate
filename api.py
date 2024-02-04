import logging

from fastapi.responses import JSONResponse
from fastapi import FastAPI
from ray import serve

import model

app = FastAPI()

logger = logging.getLogger("ray.serve")


@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.5, "num_gpus": 0})
@serve.ingress(app)
class Model:
    def __init__(self):
        # Load model
        logger.info("Initialized model.")

    @app.post("/predict")
    def detect_face(self, img_path: str) -> JSONResponse:
        # Run inference
        logger.info(f"Img path: {img_path}")
        output = model.test_model()
        if output:
            return JSONResponse(output)
        else:
            return JSONResponse({"Error": "Internal Server Error 500"})
    
ray_app = Model.bind()
