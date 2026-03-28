import lmstudio as lms
from fastapi import FastAPI

app = FastAPI()

model = lms.llm("qwen/qwen3-1.7b")


# print(result)


@app.get("/")
def root():
    return {"message": "Welcome to my LLM based data mining AI"}


@app.get("/analyze")
def analyze():
    result = model.respond(
        """
       IMPORTANT: Provide response text only.
       Do not include any explanations or additional text,
       Do NOT use Markdown, do NOT use asterisks (**),
       do NOT use hashtags (#), and do NOT use bullet points.
       Explain how data mining works integration with LLM based models
       """
    )
    return {"message": result}
