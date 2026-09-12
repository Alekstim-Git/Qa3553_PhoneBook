import logging

#DEBUG<INFO<WARNING (<ERROR<CRITICAL - не применяем по сути)
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s-%(levelname)s-%(name)s-%(message)s",
        # filename="test.log",
        # filemode="w"
    )