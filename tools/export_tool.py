import json
import os

def save_json(data, filename):

    os.makedirs(
        "output",
        exist_ok=True
    )

    file_path = os.path.join(
        "output",
        filename
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    return file_path
