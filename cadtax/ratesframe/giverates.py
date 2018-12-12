import pandas as pd
from pandas import DataFrame

class taxrates():
    def displayrates():
        ind = ["Alberta", "British Columbia", "Manitoba", "New-Brunswick", "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut","Ontario", "Prince Edward Island(PEI)", "Quebec", "Saskatchewan", "Yukon"]

        df = pd.DataFrame({"Provincial rate(PST)" : [str(0) + "%", str(7) + "%",str(8) + "%",str(10) + "%",str(10) + "%",str(0) + "%",str(10) + "%",str(0) + "%",str(8) + "%",str(10) + "%",str(9.975) + "%",str(6) + "%",str(0) + "%"],
                  "Canada rate(GST)" : [str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%",str(5)+ "%"],
                  "Total" : [str(5) + "%",str(12)+ "%",str(13)+ "%",str(15)+ "%",str(15)+ "%",str(5)+ "%",str(15)+ "%",str(5)+ "%",str(13)+ "%",str(15)+ "%",str(14.975)+ "%",str(11)+ "%",str(5) + "%"]}, index = ind)
        return df
