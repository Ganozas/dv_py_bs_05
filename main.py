import os
import random

from faker import Faker

from file_operations import VERSION
import file_operations
from skills import skills
from alphabet import alphabet


if __name__ == '__main__':


    fake = Faker('ru_RU')
    runic_skills = []


    for skill in skills:
        runic_skill = ''
        for i in skill:
            runic_skill += alphabet[i]
        runic_skills.append(runic_skill)
    
    os.makedirs('files', exist_ok=True)

    for range_files in range(1,11):
        first_name = fake.first_name()
        last_name = fake.last_name()
        city = fake.city()
        job = fake.job()
        strength = random.randrange(3, 18)
        agility = random.randrange(3, 18)
        endurance = random.randrange(3, 18)
        intelligence = random.randrange(3, 18)
        luck = random.randrange(3, 18) 
        
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "town": city,
            "job": job,
            "strength": strength,
            "agility": agility,
            "endurance": endurance,
            "intelligence": intelligence,
            "luck": luck,
            "runic_skill": random.sample(runic_skills, 3),
            "skill_1": runic_skill[1],
            "skill_2": runic_skill[2],
            "skill_3": runic_skill[3],
        }

        file_operations.render_template(
                        "template.svg",
                        "files/result{}.svg".format(range_files),
                         context) 

    

