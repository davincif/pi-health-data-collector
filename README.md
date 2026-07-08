# Raspbarry Health Data Collector

The script is meant to be used in a Raspbarry PI with **linux distribution**, preferebly the **Raspbarry PI OS**. If the not in a PI OS the temperature wacher will likely no work.

The system also works on a ThinkPad with linux system.

## run

```sh
pip install requeriments.txt
python3 main.py
```

## Docker

```sh
sudo docker build --network=host -t ldavincif/pi-health-watcher .
sudo docker run -d --name pi-health-watcher ldavincif/pi-health-watcher
```

For running the cointainer

```sh
PORT=7325 ADDR=192.168.1.153 sudo docker compose up -d
```
