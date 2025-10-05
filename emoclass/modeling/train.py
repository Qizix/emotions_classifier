from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from emoclass.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()



@app.command()
def main(
    train_dataset_path: Path = PROCESSED_DATA_DIR / "train/",
    test_dataset_path: Path = PROCESSED_DATA_DIR / "test/",
    valid_dataset_path: Path = PROCESSED_DATA_DIR / "valid/",
):

    # Model start info
    logger.info("Model training starts")
    logger.info("train/test/val directory pathes")
    logger.info(train_dataset_path)
    logger.info(test_dataset_path)
    logger.info(valid_dataset_path)



if __name__ == "__main__":
    app()
