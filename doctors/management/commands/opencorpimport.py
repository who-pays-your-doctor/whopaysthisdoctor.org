from django.core.management.base import BaseCommand, CommandError
from doctors.models import Doctor, ImportedDoctorCompanyLink
import json


class Command(BaseCommand):
    help = 'Import an OpenCorporate query in JSON format. See https://github.com/drcjar/wptd2/blob/master/wptd-opencorporates.ipynb'

    def add_arguments(self, parser):
        parser.add_argument('data', help='JSON data')

    def handle(self, *args, **options):
        with open (args[0], "r") as myfile:
            data=myfile.read()

        datastore = json.loads(data)

        for person in datastore:
            if len(person) == 0:
                continue
            nameParts = person[0]['name'].split()
            drs = Doctor.objects.filter(name__icontains = nameParts[0]).filter(name__icontains = nameParts[len(nameParts) - 1]);
            if len(drs) == 0:
                nameParts = [part.lower() for part in nameParts]
                nameParts = [part[0].upper() + part[1:] for part in nameParts ]
                dr = Doctor(name=" ".join(nameParts),
                            self_created=False,
                            )
                dr.save()
                self.save_directorships(dr, person)
            elif len(drs) > 1:
                self.stdout.write("Identified more than one existing doctor for " + person[0]['name'])
            else:
                self.save_directorships(dr, person)

    def save_directorships(self, dr, directorships):
        for directorship in directorships:
            newLink = ImportedDoctorCompanyLink(
                doctor=dr, 
                company=directorship['company']['name'], 
                officer_link=directorship['opencorporates_url'],
                company_link=directorship['company']['opencorporates_url'])
            newLink.save()