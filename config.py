import os
import utils

dirname: str = os.path.dirname(__file__)


def create_datapaths(dirname: str) -> dict:
    datasets: list = []
    with os.scandir(utils.normabspath(dirname, 'data/')) as d:
        for f in d:
            if f.is_file():
                datasets.append(f.name)

    keys: list = [dataset[:-4] for dataset in datasets]

    return {k: utils.normabspath(dirname, f"data/{v}") for k, v in zip(keys, datasets)}


datapaths: dict = create_datapaths(dirname)