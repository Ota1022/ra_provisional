from airports import airports


class Airport(object):
    def __init__(self, code):
        self.code = code
        self.name = dict(airports).get(self.code)
        self.city = self.name.split(",")[0] if self.name else None


if __name__ == "__main__":
    import fire

    fire.Fire(Airport)
