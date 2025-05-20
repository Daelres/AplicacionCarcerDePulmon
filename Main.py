from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib

app = FastAPI(
    title="API de Detección de Cáncer de Pulmón",
    version="1.0"
)

class InputData(BaseModel):
    GENDER: int = Field(..., ge=0, le=1, description="1=M, 0=F")
    AGE: int = Field(..., ge=30, le=90, description="Edad en años (30-90)")
    SMOKING: int
    YELLOW_FINGERS: int
    ANXIETY: int
    PEER_PRESSURE: int
    CHRONIC_DISEASE: int = Field(..., alias="CHRONIC DISEASE")
    FATIGUE_: int = Field(..., alias="FATIGUE ")
    ALLERGY_: int = Field(..., alias="ALLERGY ")
    WHEEZING: int
    ALCOHOL_CONSUMING: int = Field(..., alias="ALCOHOL CONSUMING")
    COUGHING: int
    SHORTNESS_OF_BREATH: int = Field(..., alias="SHORTNESS OF BREATH")
    SWALLOWING_DIFFICULTY: int = Field(..., alias="SWALLOWING DIFFICULTY")
    CHEST_PAIN: int = Field(..., alias="CHEST PAIN")

    class Config:
        allow_population_by_field_name = True
        allow_population_by_alias = True

# Cargo el modelo una sola vez
try:
    modelo = joblib.load("Recursos/Modelos/decision_tree_model.pkl")
except Exception as e:
    raise RuntimeError(f"No se pudo cargar el modelo: {e}")

@app.post("/predict")
def predict(input_data: InputData):
    # Normalizar la edad con la fórmula definida
    raw_age = input_data.AGE
    normalized_age = (raw_age - 30) / (90 - 30)

    # Construir payload usando alias, reemplazando AGE por el valor normalizado
    payload = input_data.dict(by_alias=True)
    payload["AGE"] = normalized_age

    df = pd.DataFrame([payload])

    # chequeo rápido de columnas
    expected = list(modelo.feature_names_in_)
    missing = set(expected) - set(df.columns)
    extra   = set(df.columns) - set(expected)
    if missing or extra:
        raise HTTPException(
            status_code=400,
            detail={
                "missing_columns": sorted(missing),
                "extra_columns": sorted(extra),
            }
        )

    # predicción
    try:
        pred = modelo.predict(df)[0]
        if isinstance(pred, str):
            pred = 1 if pred.upper() == "YES" else 0
        return {"prediction": int(pred)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en predicción: {e}")