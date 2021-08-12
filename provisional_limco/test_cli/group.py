class IngestionStage(object):
    def run(self):
        return "Ingesting! Nom nom nom..."


class DigestionStage(object):
    def run(self, volume=1):
        return " ".join(["Burp!"] * volume)

    def status(self):
        return "Satiated."


class Pipeline(object):
    def __init__(self):
        self.ingestion = IngestionStage()
        self.digestion = DigestionStage()

    def run(self):
        value = list()
        result = self.ingestion.run()
        value.append(result)
        result = self.digestion.run()
        value.append(result)
        return value


if __name__ == "__main__":
    import fire

    fire.Fire(Pipeline)
