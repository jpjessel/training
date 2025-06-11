# Please create a class that is responsible for representing coding systems, specifically snomed codes.
# The class should
#   - Generate a unique identifier
#   - Have an active date range
# The snomed class should have the identifier and date range as an attribute assigned by the classes method
# The snomed class should inherit from a generic ClinicalCodes class and any attributes and methods you deem worthy
# Consider whether it is applicable to apply overriding.
# 
# Note: no need to add implementation - I want the shell of the classes.  

class ClinicalCodes:
    def __init__(self, identifier, disease):
        self.identifier = identifier
        self.disease = disease

    def method_name(self):
        print(f"this code {self.identifier} is part of {self.disease}")

ClinicalCodes_entry = ClinicalCodes("123456", "Flu")
ClinicalCodes_entry.method_name()


class SNOMED(ClinicalCodes):
    def __init__(self, identifier, date_range):
        self.identifier = identifier
        self.date_range = date_range

    def method_name(self):
        # do something
        print(f"identifier is {self.identifier} and Date is {self.date_range}")


snomed_entry = SNOMED("123456", "2020-01-01 to 2020-12-31")
snomed_entry.method_name()

testing = ClinicalCodes("1","super flu")
print(testing.method_name())




import hashlib
hash_object = hashlib.sha256("Luisa".encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)
 
 #etl
 #elt