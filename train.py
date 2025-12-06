from TTS.bin.train import train
import json

with open("config.json") as f:
    config = json.load(f)

train(
    config_path="config.json",
    dataset_path=config["dataset"]["path"],
    output_path="output"
)
