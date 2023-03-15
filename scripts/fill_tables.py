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
    ('cat1', 'Fluffy', 'cat1.png'),
    ('dog1', 'Bob', 'dog1.png')
]

c.executemany('INSERT INTO pet_status (pet_status_name, effect) VALUES (?, ?)', pet_statuses)
c.executemany('INSERT INTO pets (pet_id, pet_name, img_name) VALUES (?, ?, ?)', pets)

print("Filled out tables.")

conn.commit()

c.close()
conn.close()