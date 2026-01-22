import pandas as pd
from django.core.management.base import BaseCommand
from api.models import Voter

class Command(BaseCommand):
    help = "Import voter data from Excel file"

    def handle(self, *args, **kwargs):
        file_path = "api/data/voters.xlsx"

        df = pd.read_excel(file_path)

        created = 0
        updated = 0

        for _, row in df.iterrows():
            obj, is_created = Voter.objects.update_or_create(
                epic_no=str(row["EPIC No"]).strip(),
                defaults={
                    "ward_no": int(row["Ward No"]),
                    "ac_no": int(row["AC No"]),
                    "ps_no": int(row["PS No"]),
                    "sl_no": int(row["SL No"]),
                    "name": str(row["Name"]).strip(),
                    "relation_name": str(row["Relation Name"]).strip(),
                    "relation": str(row["Relation"]).strip(),
                    "age": int(row["Age"]),
                    "gender": str(row["Gender"]).strip(),
                    "door_no": str(row["Door No"]).strip(),
                }
            )

            if is_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import completed. Created: {created}, Updated: {updated}"
            )
        )
