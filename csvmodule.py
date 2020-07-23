import csv

##### Take in monster names from 'one.csv' and output the codenames without altering 'one.csv'

# There may be a more efficient and dynamic way to code this, but this was my 
# best attempt with my current limited knowledge of CSV scripting with Python

def codenamegenerator(filename, filename_2):
    with open(filename, 'r+', newline='') as csvfile:
        # converting the iterable csv.DictReader object returned into a list of dicts to loop through and update values 
        monster_names = list(csv.DictReader(csvfile))

        # updating monster field values with new codenames in our duplicate list of 'one.csv' rows
        for row in monster_names:

            if row['monster'] == "Bigfoot":
                row['monster'] = "FuzzyHuman"
            elif row['monster'] == "Lake Monster":
                row['monster'] = "GoodSwimmer"
            elif row['monster'] == "Forest Ghost":
                row['monster'] = "TransparentCamper"
            elif row['monster'] == "Talking Cactus":
                row['monster'] = "DesertBuddy"
            elif row['monster'] == "Ice Dragon":
                row['monster'] = "ColdBird"

        fieldnames = ['#timestamp', 'researcher', 'codename', 'latitude', 'longitude']
        
        # writing new csv file with updated monster codenames
        with open(filename_2, 'w', newline='') as newcsvfile:
            writer = csv.DictWriter(newcsvfile, fieldnames=fieldnames)

            writer.writeheader()
            
            # writing in each row from updated data in monster_names list
            for row in monster_names:
                writer.writerow(
                    {'#timestamp': row['#"timestamp"'], 'codename': row['monster'], 'researcher': row['researcher'], 'latitude': row['latitude'], 'longitude': row['longitude']}
                )

codenamegenerator('one.csv', 'codenames.csv')

# Sources used: https://docs.python.org/3/library/csv.html
