class ClinicalCodes:
    def __init__(self, disease):
        self.disease = disease
        self.identifier = self.generate_identifier()
        self.generate_date_range()

    def generate_identifier():
        pass

    def generate_date_range():
        pass

class Snomed(ClinicalCodes):
    def __init__(self, disease):
        super().__init__(disease)

    def generate_identifier():
        pass