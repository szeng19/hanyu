from fastapi import APIRouter, HTTPException
from app.services.ai_service import get_word_explanation

router = APIRouter(prefix="/api")

@router.post("/explain")
async def explain_word(word: str):
    try:
        explanation = await get_word_explanation(word)
        return {"explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 