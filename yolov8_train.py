from ultralytics import YOLO


dataset_yaml = "dataset/dataset.yaml" #MUDAR PATH


model = YOLO("yolov8n.yaml")


model.train(
    data=dataset_yaml,
    epochs=50,
    imgsz=640,
    batch=16,
    workers=4,
    name="yolov8_soja_diseases"
)

metrics = model.val()
print(metrics)


img_path = "dataset/images/val/sojaTest" #MUDAR PATH
results = model(img_path)
results.show()
results.save("resultados/")


model.export(format="onnx", path="resultados/modelo_final.onnx")
