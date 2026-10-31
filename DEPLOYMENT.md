# Deployment Guide: College Knowledge Assistant

This repository is pre-configured and production-ready for deployment across multiple cloud platforms.

---

## 1. Streamlit Community Cloud (Recommended & Free)

Streamlit Community Cloud is the fastest and easiest way to deploy this application for free.

### Step-by-Step Instructions:
1. **Push your code to GitHub**:
   Ensure this repository is pushed to your GitHub account (see the GitHub instructions below).
2. **Go to Streamlit Community Cloud**:
   Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. **Click "New app"**:
   - **Repository**: Select `your-username/your-repo-name`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. **Deploy**:
   Click **"Deploy!"**.
   Streamlit Cloud will automatically install dependencies from `requirements.txt` and launch the app with a public URL!

---

## 2. Docker Container Deployment

You can deploy anywhere that runs Docker containers (e.g. AWS ECS, Google Cloud Run, Fly.io, DigitalOcean, or your local machine).

### Build and Run with Docker:
```bash
# Build the Docker image
docker build -t college-rag-assistant .

# Run the container
docker run -d -p 8501:8501 --name college-rag college-rag-assistant
```
Visit `http://localhost:8501` in your browser.

### Using Docker Compose:
```bash
docker compose up -d
```
To stop the application:
```bash
docker compose down
```

---

## 3. Render / Railway Deployment

The repository includes `render.yaml` and `Procfile` for automated cloud deployment on Render or Railway.

### Deploying to Render:
1. Go to [render.com](https://render.com) and connect your GitHub repository.
2. Choose **Web Service**.
3. Render automatically detects `render.yaml` or you can configure:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
4. Click **Create Web Service**.

---

## 4. Hugging Face Spaces

1. Create a new Space at [huggingface.co/spaces](https://huggingface.co/spaces).
2. Choose the **Streamlit** SDK.
3. Push or sync this repository to your Space.
4. Hugging Face Spaces will automatically build and serve the application.

