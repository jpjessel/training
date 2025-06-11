# Please create a class that is responsible for representing coding systems, specifically snomed codes.
# The class should
#   - Generate a unique identifier
#   - Have an active date range
# The snomed class should have the identifier and date range as an attribute assigned by the classes method
# The snomed class should inherit from a generic ClinicalCodes class and any attributes and methods you deem worthy
# Consider whether it is applicable to apply overriding.
# 
# Note: no need to add implementation - I want the shell of the classes.  

from collections import defaultdict

class ClinicalCodes: 
    def __init__(
            self, 
            disease,
            disease_dict: dict[str, dict]
        ):
        self.disease_dict = disease_dict
        self.disease_area = disease
        self.codelist_schema = disease_dict["clinical_code_type"]
        self.codelist_map = {}
        self.StartDate = disease_dict["active_start_date"]
        self.EndDate = disease_dict["active_end_date"]
    
    try: 
        if 
    except: 
        KeyError
    
    def add_ClinicalCodeTerm(self, code_type: str):
        code_type = code_type.lower()
        ClinicalCodeKeys = {}
        for key,value in self.disease_dict[code_type].items():
            ClinicalCodeKeys[key] = self.codelist_map.get(value["CodeID"])

        return ClinicalCodeKeys
    
    def add_ClinicalCodeTerm(self, code_type: str):
        code_type = code_type.lower()
        ClinicalCodeKeys = {}
        for key,value in self.disease_dict[code_type].items():
            ClinicalCodeKeys[value["CodeTerm"]] = key

        return ClinicalCodeKeys

InfluenzaCodes = ClinicalCodes("Influenza", 
                               {"clinical_code_type": "ICD10", 
                                "active_start_date": "2020-01-01", 
                                "active_end_date": "2025-06-01", 
                                "ICD10": {"ID": "13456", 
                                          "Term": "Influenza"}})

class Snomed(ClinicalCodes): 

    def __init__(
            self, 
            disease
        ): 
        super().__init__(disease)
        self.codelist_schema = "Snomed"
    
    def add_SnomedTerm(self, code_type: str):
        code_type = code_type.lower()
        SnomedKeys = {}
        for key,value in self.disease_dict[code_type].items():
            SnomedKeys[key] = self.codelist_map.get(value["SnomedID"])

        return SnomedKeys
    
    def add_SnomedTerm(self, code_type: str):
        code_type = code_type.lower()
        SnomedKeys = {}
        for key,value in self.disease_dict[code_type].items():
            SnomedKeys[value["SnomedTerm"]] = key

        return SnomedKeys

    
