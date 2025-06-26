from ultralytics import YOLO

# Use barras normais (/) para os caminhos de arquivo
dataset_yaml = "PATH/dataset.yaml" 

# Use 'yolov8n.pt' para carregar pesos pré-treinados (transfer learning).
# Isso resulta em um treinamento muito mais rápido e com maior precisão.
model = YOLO("yolov8n.pt") 

# Treina o modelo
model.train(
    data=dataset_yaml,
    epochs=50,
    imgsz=640,
    batch=16,
    workers=4,
    name="yolov8_soja_diseases"
)

# Valida o modelo treinado
metrics = model.val() 
print(metrics)

# Corrija o caminho da imagem de teste
img_path = "IMG_Path"  
results = model(img_path) 
results.show() 
results.save("resultados/")

# Exporta o modelo final
model.export(format="onnx", path="resultados/modelo_final.onnx")