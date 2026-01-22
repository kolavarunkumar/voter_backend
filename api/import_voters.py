import pandas as pd
from api.models import Voter

def run():
    df = pd.read_excel('voters.xlsx')

    count = 0
    for _, row in df.iterrows():
        Voter.objects.create(
            ward_no=int(row['Ward No']),
            ac_no=int(row['AC No']),
            ps_no=int(row['PS No']),
            sl_no=int(row['SL No']),
            name=str(row['Name']).strip(),
            relation_name=str(row['Relation Name']).strip(),
            relation=str(row['Relation']).strip(),
            age=int(row['Age']),
            gender=str(row['Gender']).strip(),
            door_no=str(row['Door No']).strip(),
            epic_no=str(row['EPIC No']).strip(),
        )
        count += 1

    print(f"Imported {count} voters")
