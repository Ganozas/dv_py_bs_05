import os
import random

from faker import Faker

from file_operations import VERSION
import file_operations
from skills import skills
from alphabet import alphabet


fake = Faker('ru_RU')
runic_skills = []
end = 0


if __name__ == '__main__': 
    for skill in skills:
        runic_skill = ''
        for i in skill:
            runic_skill += alphabet[i]
        runic_skills.append(runic_skill)
    
    os.makedirs('files', exist_ok=True)

    for range_files in range(1,11):
        name = fake.name()
        city = fake.city()
        job = fake.job()
        roll_dice = random.randrange(3, 18)
        runic_skills = random.sample(runic_skills, 3) 
        
        context = {
      "name": name,
      "city": city,
      "job": job,
      "roll_dice": roll_dice,
      "runic_skills": runic_skills 
    }
        file_operations.render_template(
                        "template.svg",
                        "files/result{}.svg".format(range_files),
                         context) 
        end += 1
    

