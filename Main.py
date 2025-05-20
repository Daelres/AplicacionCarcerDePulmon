from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI(
    title="API de Detección de Cáncer de Pulmón",
    version="1.0"
)

# Defino el esquema de entrada
class InputData(BaseModel):
    GENDER: int = Field(..., ge=0, le=1, description="1=M, 0=F")
    AGE: float = Field(..., description="Edad normalizada entre 30 y 90")
    SMOKING: int; YELLOW_FINGERS: int; ANXIETY: int; PEER_PRESSURE: int
    CHRONIC_DISEASE: int; FATIGUE_: int; ALLERGY_: int
    WHEEZING: int; ALCOHOL_CONSUMING: int; COUGHING: int
    SHORTNESS_OF_BREATH: int; SWALLOWING_DIFFICULTY: int; CHEST_PAIN: int

# Cargo el modelo al arrancar
try:
    modelo = joblib.load("modelos/decision_tree_model.pkl")
except Exception as e:
    raise RuntimeError(f"No se pudo cargar el modelo: {e}")

@app.post("/predict")
def predict(data: InputData):
    # Convierto a DataFrame
    df = pd.DataFrame([data.dict()])
    try:
        pred = modelo.predict(df)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en predicción: {e}")
    # Si el modelo devuelve strings, opcionalmente mapear a 0/1
    if isinstance(pred, str):
        pred = 1 if pred.upper() == "YES" else 0
    return {"prediction": int(pred)}

# Para levantar el servidor:
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
