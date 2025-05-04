
# 🛒 Cloud Native App

A fully containerized cloud-native e-commerce application built with microservices using Kubernetes, Docker, Prometheus, Grafana, Jenkins, PostgreSQL, Redis, FastAPI (Python), and React. Includes observability, health checks, and support for canary deployments.

## 📦 Tech Stack

- **Frontend**: ReactJS
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Cache**: Redis
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: Jenkins
- **Observability**: Prometheus, Grafana
- **Ingress**: NGINX Ingress Controller

---

## 📁 Project Structure

```
cloud-native-app/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routers/
│   │   └── services/
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── components/
│   └── Dockerfile
├── k8s/
│   ├── base/
│   │   └── namespace.yaml
│   ├── backend/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── hpa.yaml
│   ├── postgres/
│   ├── redis/
│   ├── frontend/
│   ├── ingress/
│   │   └── ingress.yaml
│   └── monitoring/
│       ├── prometheus-config.yaml
│       ├── prometheus-deployment.yaml
│       └── grafana-deployment.yaml
├── jenkins/
│   └── Jenkinsfile
├── scripts/
│   └── init-db.sql
└── README.md
```

---

## 🚀 Features

- ✅ Microservices architecture
- ✅ RESTful API with FastAPI
- ✅ UI with React
- ✅ PostgreSQL for data persistence
- ✅ Redis caching
- ✅ Canary deployments ready (Flagger/Istio/Argo optional)
- ✅ Monitoring via Prometheus and Grafana
- ✅ Kubernetes manifests for full deployment
- ✅ Health & metrics endpoints
- ✅ CORS support and frontend-backend integration

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/cloud-native-app.git
cd cloud-native-app
```

### 2. Build Docker Images (Optional if using prebuilt)
```bash
docker build -t your-username/cloud-native-frontend ./frontend
docker build -t your-username/cloud-native-backend ./backend
```

### 3. Deploy to Kubernetes
```bash
kubectl apply -f k8s/base/namespace.yaml
kubectl apply -f k8s/postgres/
kubectl apply -f k8s/redis/
kubectl apply -f k8s/backend/
kubectl apply -f k8s/frontend/
kubectl apply -f k8s/ingress/ingress.yaml
kubectl apply -f k8s/monitoring/
```

> Ensure your ingress controller is installed and running.

---

## 📊 Accessing the App

- **Frontend**: `http://localhost/frontend`
- **Backend API**: `http://localhost/api/items/1`
- **Prometheus**: `http://localhost:9090`
- **Grafana**: `http://localhost:3000`

---

## 🧪 Example API Endpoint

```http
GET /api/items/1
Response:
{
  "item_id": 1,
  "data": "Test Item 1",
  "source": "cache"
}
```

---

## 📈 Monitoring

Prometheus scrapes `/metrics` from the backend service:
```bash
GET /metrics
```

Grafana dashboards can be imported using Prometheus as a data source.

---

## ✅ To-Do / Improvements

- [ ] Add authentication (OAuth 2.0 / Firebase)
- [ ] Enable HTTPS via cert-manager
- [ ] Integrate Flagger for canary deployment strategy
- [ ] Add autoscaling with HPA
- [ ] Configure Grafana alerts

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Aakash Sharma**  
DevOps Engineer • Cloud Native Enthusiast  
[GitHub](https://github.com/sharmaaakash170)
