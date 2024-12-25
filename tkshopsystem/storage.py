import json

from typing import ContextManager


class Storage(ContextManager):
    def __init__(self, file_name: str = "./goods.json"):
        self._file_name = file_name
        self._inner = None
        pass

    def __enter__(self):
        self._inner = load_goods_data_hn(self._file_name)
        return self._inner

    def __exit__(self, _1, _2, _3):
        save_goods_data_hn(self._file_name, self._inner)


# 简单的辅助函数，用于读取商品数据到self.storage
def load_goods_data_hn(filename: str) -> list[dict]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 如果文件不存在，初始化为空列表


# 简单的辅助函数，用于将self.storage中的数据保存
def save_goods_data_hn(filename: str, data: list[dict]):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
