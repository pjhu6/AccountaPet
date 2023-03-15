import sqlite3

conn = sqlite3.connect('db/accountapet.db')

c = conn.cursor()

pet_statuses = [
    ('Arthritis',-6),
    ('Asthma',-8),
    ('Cancer',-12),
    ('Cataracts',-4),
    ('Dental disease',-4),
    ('Diabetes',-10),
    ('Digestive problems',-6),
    ('Ear infections',-3),
    ('Eye infections',-3),
    ('Feline immunodeficiency virus (FIV)',-12),
    ('Feline infectious peritonitis (FIP)',-12),
    ('Fleas/ticks',-2),
    ('Heart disease',-8),
    ('Hyperthyroidism',-10),
    ('Hypothyroidism',-6),
    ('Inflammatory bowel disease',-8),
    ('Kennel cough',-4),
    ('Kidney disease',-10),
    ('Leukemia',-12),
    ('Liver disease',-10),
    ('Lyme disease',-8),
    ('Mange',-4),
    ('Obesity',-6),
    ('Osteoporosis',-6),
    ('Pancreatitis',-8),
    ('Parvovirus',-12),
    ('Periodontal disease',-4),
    ('Pneumonia',-8),
    ('Rabies',-12),
    ('Ringworm',-4),
    ('Salmonella',-8),
    ('Seizures',-8),
    ('Skin allergies',-6),
    ('Tapeworms',-4),
    ('Toxoplasmosis',-10),
    ('Urinary tract infections',-6),
    ('Vestibular disease',-6),
    ('Warts',-2),
    ('West Nile virus',-8),
    ('Whipworms',-4),
    ('Addison\'s disease',-10),
    ('Cushing\'s disease',-10),
    ('Distemper',-12),
    ('Ehrlichiosis',-8),
    ('Gingivitis',-4),
    ('Heartworm disease',-12),
    ('Hip dysplasia',-6),
    ('Lyme nephritis',-8),
    ('Pyometra',-10),
    ('Valley fever',-8)
]

pets = [
    ("dog1", "Buddy", "dog1.png"),
    ("dog2", "Max", "dog2.png"),
    ("dog3", "Charlie", "dog3.png"),
    ("dog4", "Cooper", "dog4.png"),
    ("dog5", "Bailey", "dog5.png"),
    ("cat1", "Smokey", "cat1.png"),
    ("cat2", "Tiger", "cat2.png"),
    ("cat3", "Mittens", "cat3.png"),
    ("cat4", "Shadow", "cat4.png"),
    ("cat5", "Simba", "cat5.png"),
    ("hamster1", "Biscuit", "hamster1.png"),
    ("hamster2", "Nibbles", "hamster2.png"),
    ("hamster3", "Peanut", "hamster3.png"),
    ("hamster4", "Honey", "hamster4.png"),
    ("hamster5", "Oreo", "hamster5.png"),
    ("rabbit1", "Thumper", "rabbit1.png"),
    ("rabbit2", "Bugs", "rabbit2.png"),
    ("rabbit3", "Flopsy", "rabbit3.png"),
    ("rabbit4", "Peter", "rabbit4.png"),
    ("rabbit5", "Cottontail", "rabbit5.png"),
    ("fish1", "Bubbles", "fish1.png"),
    ("fish2", "Nemo", "fish2.png"),
    ("fish3", "Goldie", "fish3.png"),
    ("fish4", "Finley", "fish4.png"),
    ("fish5", "Splash", "fish5.png"),
    ("bird1", "Tweety", "bird1.png"),
    ("bird2", "Polly", "bird2.png"),
    ("bird3", "Kiwi", "bird3.png"),
    ("bird4", "Sunny", "bird4.png"),
    ("bird5", "Robin", "bird5.png"),
    ("snake1", "Slytherin", "snake1.png"),
    ("snake2", "Rattler", "snake2.png"),
    ("snake3", "Viper", "snake3.png"),
    ("snake4", "Cobra", "snake4.png"),
    ("snake5", "Python", "snake5.png"),
    ("turtle1", "Shelly", "turtle1.png"),
    ("turtle2", "Speedy", "turtle2.png"),
    ("turtle3", "Crush", "turtle3.png"),
    ("turtle4", "Flash", "turtle4.png"),
    ("turtle5", "Squirtle", "turtle5.png"),
    ("lizard1", "Iggy", "lizard1.png"),
    ("lizard2", "Spike", "lizard2.png"),
    ("lizard3", "Gex", "lizard3.png"),
    ("lizard4", "Gecko", "lizard4.png"),
    ("lizard5", "Rango", "lizard5.png")
]

c.executemany('INSERT INTO pet_status (pet_status_name, effect) VALUES (?, ?)', pet_statuses)
c.executemany('INSERT INTO pets (pet_id, pet_name, img_name) VALUES (?, ?, ?)', pets)

print("Filled out tables.")

conn.commit()

c.close()
conn.close()