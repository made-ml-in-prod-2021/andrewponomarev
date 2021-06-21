Homework-4
==============================

Project is based on google cloud system:  
https://console.cloud.google.com/


------------
Create docker image
```
cd online_inference
docker build -t terysy/online_inference:v1 .
docker run -p 8000:8000 terysy/online_inference:v1
cd ./..
```

Check if cluster works
```
kubectl cluster-info
```

Run pods:
```
kubectl apply -f kubernetes/online-inference-pod.yaml
kubectl apply -f kubernetes/online-inference-pod-resources.yaml
kubectl apply -f kubernetes/online-inference-pod-probes.yaml
kubectl apply -f kubernetes/online-inference-replicaset.yaml
kubectl apply -f kubernetes/online-inference-deployment-blue-green.yaml
kubectl apply -f kubernetes/online-inference-deployment-rolling-update.yaml
```

Enable port forwarding
```
kubectl port-forward pod/online-inference-pod 8000:8000
kubectl apply -f kubernetes/online-inference-pod-probes 8000:8000
...
```

Get logs
```
kubectl describe pod online-inference-pod
kubectl describe pod online-inference-pod-probes
...
```


Homework estimation
----------
20 points

Criterion
------------
№ | Description | Points
--- | --- | ---
1 | ~~Убедитесь, с кластер поднялся (kubectl cluster-info)~~  | 5
2 | ~~Напишите простой pod manifests для вашего приложения, назовите его online-inference-pod.yaml (https://kubernetes.io/docs/concepts/workloads/pods/). Задеплойте приложение в кластер (kubectl apply -f online-inference-pod.yaml), убедитесь, что все поднялось (kubectl get pods). Приложите скриншот, где видно, что все поднялось~~ | 4
2a | ~~Пропишите requests/limits и напишите зачем это нужно в описание PR закоммитьте файл online-inference-pod-resources.yaml~~ | 2
3 | ~~Модифицируйте свое приложение так, чтобы оно стартовало не сразу(с задержкой секунд 20-30) и падало спустя минуты работы. Добавьте liveness и readiness пробы , посмотрите что будет происходить. Напишите в описании -- чего вы этим добились. Закоммититьте отдельный манифест online-inference-pod-probes.yaml (и изменение кода приложения)~~ | 3
4 | ~~Создайте replicaset, сделайте 3 реплики вашего приложения. (https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) Ответьте на вопрос, что будет, если сменить докер образа в манифесте и одновременно с этим. а) уменьшить число реплик б) увеличить число реплик. Поды с какими версиями образа будут внутри будут в кластере?~~ | 3
5 | ~~Опишите деплоймент для вашего приложения. (https://kubernetes.io/docs/concepts/workloads/controllers/deployment/). Играя с параметрами деплоя(maxSurge, maxUnavaliable), добейтесь ситуации, когда при деплое новой версии. a) Есть момент времени, когда на кластере есть как все старые поды, так и все новые (опишите эту ситуацию) (закоммититьте файл online-inference-deployment-blue-green.yaml). б) одновременно с поднятием новых версии, гасятся старые (закоммитите файл online-inference-deployment-rolling-update.yaml)~~ | 3