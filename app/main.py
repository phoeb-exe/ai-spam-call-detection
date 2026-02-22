import tempfile
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.database.database import init_db, SessionLocal, CallLog
from asr.asr_model import ASRModel
from models.spam_model import SpamModel

app = FastAPI(title="AI Spam Call Detection API")

init_db()

asr_model = ASRModel()
spam_model = SpamModel()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        shutil.copyfileobj(file.file, temp_audio)
        temp_path = temp_audio.name

    transcript = asr_model.transcribe(temp_path)

    pred, prob = spam_model.predict(transcript)

    label = "spam" if pred == 1 else "legitimate"

    db = SessionLocal()

    new_log = CallLog(
        filename=file.filename,
        transcript=transcript,
        prediction=int(pred),
        probability=float(prob),
        label=label
    )

    db.add(new_log)
    db.commit()
    db.close()

    return JSONResponse({
        "prediction": int(pred),
        "probability": float(prob),
        "label": label,
        "transcript": transcript
    })

@app.get("/history")
def get_history():
    db = SessionLocal()
    logs = db.query(CallLog).order_by(CallLog.created_at.desc()).all()

    result = []
    for log in logs:
        result.append({
            "filename": log.filename,
            "label": log.label,
            "probability": log.probability,
            "created_at": log.created_at
        })

    db.close()
    return result