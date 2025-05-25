from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

# Setup database
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add companies.
company1 = Company(name="C&G Ltd.", founding_year=2011)
company2 = Company(name="Cummins C&G Ltd.", founding_year=1990)
company3 = Company(name="Mantrac Kenya Ltd.", founding_year=1995)
company4 = Company(name="Blackhood Hodge Ltd.", founding_year=2012)

# Add devs
dev1 = Dev(name="Dennis M. Ngui")
dev2 = Dev(name="Hollystone J. Obonyo")
dev3 = Dev(name="Faith M. Musau")
dev4 = Dev(name="Veronica W. Flora")

session.add_all([company1, company2, company3, company4, dev1, dev2, dev3, dev4])
session.commit()

# Give freebies
session.add_all([
    company1.give_freebie(dev1, "Laptop", 1),
    company1.give_freebie(dev2, "Smartphone", 2),
    company2.give_freebie(dev1, "Notebook", 3),
    company2.give_freebie(dev2, "Headphones", 4),
    company3.give_freebie(dev3, "Backpack", 5),
    company4.give_freebie(dev4, "Water Bottle", 6)
])
session.commit()

# Print all freebies
for freebie in session.query(Freebie).all():
    print(freebie.print_details())


