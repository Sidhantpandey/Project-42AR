import httpx

from app.config import settings


async def generate_rag_answer(query: str, contexts: list[str]) -> str:
    if not settings.gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not configured")

    context_block = "\n\n".join(
        [f"Context {idx + 1}:\n{ctx}" for idx, ctx in enumerate(contexts)]
    )

    system_prompt = (
        "You are an AI assistant for log analysis and incident troubleshooting. "
        "Answer using only the provided context. "
        "Do tell appropriate solutions for the problems"
    )

    user_prompt = (
        f"User Query:\n{query}\n\n"
        f"Retrieved Context:\n{context_block}\n\n"
        "Provide a concise, actionable answer."
    )

    request_payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": (
                            f"{system_prompt}\n\n{user_prompt}"
                        )
                    }
                ],
            }
        ],
        "generationConfig": {"temperature": 0.2},
    }

    url = f"{settings.gemini_base_url}/models/{settings.gemini_model}:generateContent"
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            url,
            params={"key": settings.gemini_api_key},
            headers={"Content-Type": "application/json"},
            json=request_payload,
        )
    if response.status_code >= 400:
        raise ValueError(f"Gemini API error {response.status_code}: {response.text}")

    data = response.json()
    return _extract_gemini_text(data)


def _extract_gemini_text(data: dict) -> str:
    candidates = data.get("candidates", [])
    if not candidates:
        return "No response generated."
    content = candidates[0].get("content", {})
    parts = content.get("parts", [])
    texts = [part.get("text", "") for part in parts if isinstance(part, dict)]
    result = "\n".join([text for text in texts if text]).strip()
    return result or "No response generated."
