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
        runic_skills = random.sample(runic_skills, 8)
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
            "skill_1": runic_skills[0],
            "skill_2": runic_skills[1],
            "skill_3": runic_skills[2],
        }

        file_operations.render_template(
                        "template.svg",
                        "files/result{}.svg".format(range_files),
                         context) 

    

