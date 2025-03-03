from faker import Faker  

def generate_card():  
    fake = Faker()  
    return {  
        'number': fake.credit_card_number(),  
        'exp': fake.credit_card_expire(),  
        'cvv': f"{random.randint(000, 999):03d}",  
        'name': fake.name()  
    }  
