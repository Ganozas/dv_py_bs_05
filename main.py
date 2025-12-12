from file_operations import VERSION
import file_operations
from faker import Faker
import random
from skills import skills
from alphabet import alphabet

print(VERSION)

fake = Faker('ru_RU')
name = fake.name()
city = fake.city()
job = fake.job()

roll_dice = random.randrange(3, 18)
roll_skills = random.sample(skills, 3)

print(roll_skills)
runic_skill_0 = ''
runic_skill_1 = ''
runic_skill_2 = ''
runic_skills = []


end = 0
for range_files in range(1,11):
    runic_skills = []
    name = fake.name()
    city = fake.city()
    job = fake.job()
    roll_dice = random.randrange(3, 18)
    roll_skills = random.sample(skills, 3)

    for skill in roll_skills[0]:
        for i in skill:
            for user_letters, un_user_letters in alphabet.items():
                if user_letters == i:
                    runic_skill_0 += un_user_letters          
                    runic_skill_0 = ''.join(runic_skill_0)            

    for skill in roll_skills[1]:
        for i in skill:
            for user_letters, un_user_letters in alphabet.items():
                if user_letters == i:
                    runic_skill_1 += un_user_letters          
                    runic_skill_1 = ''.join(runic_skill_1)            

    for skill in roll_skills[2]:
        for i in skill:
            for user_letters, un_user_letters in alphabet.items():
                if user_letters == i:
                    runic_skill_2 += un_user_letters          
                    runic_skill_2 = ''.join(runic_skill_2)
                    

runic_skills.append(runic_skill_0)
runic_skills.append(runic_skill_1)
runic_skills.append(runic_skill_2)

    context = {
  "name": name,
  "city": city,
  "job": job,
  "roll_dice": roll_dice,
  "runic_skills": runic_skills 
}
    file_operations.render_template("template.txt", "result{}.txt".format(range_files), context) 
    end += 1
    

