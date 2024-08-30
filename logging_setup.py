import logging
from config import Config

class logging_:
    @staticmethod
    def setup():
        return logging.basicConfig(
            level = logging.WARNING,
            format= '%(asctime)s | %(name)s | %(levelname)s | %(funcName)s | %(lineno)d | %(message)s | %(pathname)s',
            filename=Config.logging_info.save_file,
            filemode='a'
        )