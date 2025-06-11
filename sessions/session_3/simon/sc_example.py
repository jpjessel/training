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

class Snomed: 

    def __init__(
            self, 
            disease_dict: dict[str, dict]
        ): 
        self.disease_dict = disease_dict
        self.disease_area = disease_dict["disease_name"]
        self.Snomed_map = {}
        self.DatesActive = disease_dict["dates_active"]

    def add_SnomedID(self, disease: str):
        disease = disease.lower() 
        SnomedKeys = {}
        for key,value in self.disease_dict[disease].items():
            SnomedKeys[key] = self.Snomed_map.get(value["SnomedID"])
            
        return SnomedKeys
    
    def add_SnomedTerm(self, filter: str):
        disease = disease.lower() 
        SnomedKeys = {}
        for key,value in self.disease_dict[disease].items():
            SnomedKeys[value["SnomedTerm"]] = key

        return SnomedKeys
