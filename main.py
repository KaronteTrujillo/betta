from fastapi import FastAPI
from fastapi.responses import FileResponse
from render_betta import generate_betta_image
import os
import random

app = FastAPI()

@app.get("/generate_betta")
async def generate_betta():
    # Ruta al modelo OBJ
    obj_path = os.path.abspath("assets/betta.obj")
    # Generar un nombre único para la imagen de salida
    output_path = os.path.abspath(f"outputs/betta_{random.randint(1, 10000)}.png")
    # Asegurarse de que la carpeta outputs exista
    os.makedirs("outputs", exist_ok=True)
    # Generar la imagen
    generate_betta_image(obj_path, output_path)
    return FileResponse(output_path, media_type="image/png")
