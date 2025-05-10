## AI-Powered STEM Problem Solver

An AI-powered web application that solves **math and physics problems** using the LLaMA 3 model via **Groq API**, featuring a FastAPI backend and Streamlit frontend. It is containerized using Docker and orchestrated with Docker Compose. Continuous Integration and Docker image deployment to Docker Hub are managed using GitHub Actions.

---

## 🚀 Features

* ✅ Step-by-step solutions to STEM problems
* 📘 Optimized prompt design for math/physics tutoring
* ⚡ Powered by LLaMA 3 via Groq API
* 🔁 Frontend (Streamlit) + Backend (FastAPI)
* 🐳 Dockerized for production
* 🔄 CI/CD with GitHub Actions
* ☁️ Deployed on AWS EC2

---

## 🗂️ Project Structure

```
AI-Powered-STEM-Problem-Solver/
├── .github/workflows/deploy.yml       # GitHub Actions Workflow
├── prompt_research/                   # Prompt experiments
├── tests/                             # Unit tests for FastAPI backend
│   └── test_app.py
├── venv/                              # Virtual environment (excluded from repo)
├── .env                               # Contains GROQ_API_KEY
├── .gitignore
├── app.py                             # Optional entrypoint
├── backend.Dockerfile                 # Dockerfile for FastAPI backend
├── docker-compose.yml                 # Docker Compose for managing backend/frontend
├── frontend.Dockerfile                # Dockerfile for Streamlit frontend
├── main.py                            # FastAPI application
├── README.md
├── requirements.txt                   # Python dependencies
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🐍 Backend (FastAPI)

### 📦 Install & Run Locally

```bash
# Clone the repo
https://github.com/ka1817/AI-Powered-STEM-Problem-Solver.git
cd AI-Powered-STEM-Problem-Solver

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run backend
uvicorn main:app --host 0.0.0.0 --port 2003
```

### 🔎 Test the API

```bash
pytest tests/
```

---

## 🌐 Frontend (Streamlit)

The frontend is built with Streamlit and connects to the FastAPI backend at port `2003`.

### 🔧 To Run Locally:

```bash
streamlit run app.py --server.port 8502
```

> Make sure the backend is running at `http://localhost:2003`

---

## 🐳 Docker

### 🏗️ Build Docker Images

```bash
# Backend
docker build -t pranavreddy123/stem-backend:latest -f backend.Dockerfile .

# Frontend
docker build -t pranavreddy123/stem-frontend:latest -f frontend.Dockerfile .
```

### 📤 Push to Docker Hub

```bash
docker push pranavreddy123/stem-backend:latest
docker push pranavreddy123/stem-frontend:latest
```

### ▶️ Run with Docker Compose

```bash
docker-compose up --build
```

---

## ⚙️ GitHub Actions - CI/CD

Defined in `.github/workflows/deploy.yml`. It performs:

* ✅ Checkout & install dependencies
* ✅ Run Pytest
* ✅ Build & Push Docker images to Docker Hub

Update secrets in GitHub repo settings:

* `DOCKER_USERNAME = pranavreddy123`
* `DOCKER_PASSWORD = <your-dockerhub-password>`
* `GROQ_API_KEY = <your-api-key>`

---

## ☁️ Deployment on EC2

1. SSH into your EC2 instance.
2. Pull latest Docker images:

```bash
docker pull pranavreddy123/stem-backend:latest
docker pull pranavreddy123/stem-frontend:latest
```

3. Run containers using Docker Compose:

```bash
docker-compose up -d
```

Make sure ports `2003` (backend) and `8502` (frontend) are open in your EC2 security group.

---

## ✅ Sample API Usage

**POST** `/solve/`

```json
{
  "problem": "What is the derivative of x^2?"
}

Response:
{
  "solution": "✅ The derivative of x^2 is 2x."
}
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 📎 Useful Links

* GitHub Repo: [https://github.com/ka1817/AI-Powered-STEM-Problem-Solver](https://github.com/ka1817/AI-Powered-STEM-Problem-Solver)
* Docker Hub: [https://hub.docker.com/u/pranavreddy123](https://hub.docker.com/u/pranavreddy123)

---

## 🙌 Contributing

Feel free to fork the repo, create a branch, and submit a PR. For any questions, open an issue.

---

## 📄 License

MIT License

Developed By Pranav Reddy