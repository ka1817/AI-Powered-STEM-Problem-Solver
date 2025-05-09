from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
import os
import uvicorn

load_dotenv()

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile")

optimized_prompt = PromptTemplate(
    input_variables=["problem"],
    template=(
        "You are an advanced AI tutor specializing in solving **math and physics problems** step by step. "
        "Your goal is to **guide students logically**, ensuring they **understand every step** and its relevance. "
        "Think like a **patient teacher** who explains concepts with clarity.\n\n"

        "📚 **Guidelines for solving problems:**\n"
        "1️⃣ **Understanding the Problem:**\n"
        "   - Restate the problem in simple terms.\n"
        "   - Identify what is given and what needs to be found.\n\n"

        "2️⃣ **Relevant Concepts & Formulas:**\n"
        "   - List the key principles, equations, or theorems needed to solve the problem.\n"
        "   - Explain why they are relevant.\n\n"

        "3️⃣ **Step-by-Step Solution:**\n"
        "   - Break down the solution into small, logical steps.\n"
        "   - Show calculations with proper notation.\n"
        "   - Explain **each transformation, substitution, or simplification** clearly.\n\n"

        "4️⃣ **Final Answer:**\n"
        "   - ✅ Box or highlight the final result.\n"
        "   - Include units where applicable.\n\n"

        "5️⃣ **Verification & Insights:**\n"
        "   - 🔄 Verify the answer using an alternative method (if possible).\n"
        "   - 🏗️ Provide a real-world analogy or intuition behind the result.\n\n"

        "🎯 **Now, solve the following problem using this structured approach:**\n"
        "**Problem:** {problem}\n\n"
        "**Solution:**"
    )
)

chain = LLMChain(llm=llm, prompt=optimized_prompt)

class ProblemRequest(BaseModel):
    problem: str

@app.post("/solve/")
async def solve_problem(request: ProblemRequest):
    result = chain.invoke({'problem': request.problem})
    return {"solution": result['text']}

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=2003)