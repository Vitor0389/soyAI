<h1 align="center">🌿 YOLOv8 - Detecção de Pragas e Condição Saudável em Folhas de Soja</h1>

<p align="center">
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=flat-square" />
</p>

---

## 📌 Descrição

Este projeto utiliza **YOLOv8 (You Only Look Once)** para detectar e classificar a condição de folhas de soja a partir de imagens.  
O modelo é treinado para identificar **três classes**:

- `0`: 🐛 Caterpillar  
- `1`: 🪲 Diabrotica speciosa  
- `2`: 🌱 Healthy

🛠️ Instalação

1. **Instale o Python 3.8 ou superior**  
   Você pode baixar do site oficial: https://www.python.org/downloads/

2. **Instale as ultralytics:**

    pip install ultralytics

🧠 Treinamento do Modelo
Para iniciar o treinamento, execute:

  yolo detect train model=yolov8n.pt data=dataset/dataset.yaml epochs=50 imgsz=640

✅ Você pode trocar o modelo para yolov8m.pt, yolov8l.pt ou yolov8x.pt dependendo da potência do seu computador.

⚡ 1. Predição rápida via linha de comando

  Você também pode realizar a predição diretamente pelo terminal executando:
  
  yolo predict model=runs\detect\yolov8_soja_diseases\weights\best.pt source="IMG_PATH"

Status:

✅Dataset anotado e organizado

✅Treinamento com YOLOv8

✅Inferência a partir de imagens externas
