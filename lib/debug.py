#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie , Base

# Create an SQLite database engine and initialize the database
engine = create_engine('sqlite:///freebies.db')

Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

   
    company1= Company(name = "C&G Ltd.", founding_year = 2011) 
    company2= Company(name = "Cummins C&G Ltd.", founding_year = 1990) 
    company3= Company(name = "Mantrac Kenya Ltd.", founding_year = 1995) 
    company4= Company(name = "Blackhood Hodge Ltd.", founding_year = 2012) 

    dev1= Dev(name= "Dennis M. Ngui")
    dev2= Dev(name= "Hollystone J. Obonyo")
    dev3= Dev(name= "Faith M. Musau")
    dev4= Dev(name= "Veronica W. Flora")

    session.add_all([company1, company2, company3, company4, dev1, dev2, dev3, dev4])
    session.commit()

    # Assign freebies to developers from specific companies
    company1.give_freebie(dev1, "Laptop", 1)
    company1.give_freebie(dev2, "smartphone", 2)

    company2.give_freebie(dev1, "notebook", 3)
    company2.give_freebie(dev2, "Headphones", 4)

    freebies = session.query(Freebie).all()
    for freebie in freebies:
        print(freebie.print_details())

    print(dev1.received_one("Laptop"))
    print(dev1.received_one("smart watch"))

