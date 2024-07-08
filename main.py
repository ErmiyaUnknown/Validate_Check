email = input("email: ")
phone = input("phone: ")

def email_validator(email):
    
    if email.find("@") != -1:
        email_username = email.split("@")
        
        if email_username[0].isalnum() == True:
            email_domain = email_username[1].split(".")
            
            if email_domain[0].isalnum() == True and email_domain[1].find("_") == -1:
                
                if len(email_domain[1]) == 3:
                    print("Email is true")
                    
                else:
                    raise Exception(f"invalid email address: {email}")    
            else:
                raise Exception(f"invalid email address: {email}")      
        else:
            raise Exception(f"invalid email address: {email}")     
    else:    
        raise Exception(f"invalid email address: {email}")  
    
email_validator(email)    


def phone_validator(phone): 
    
    if len(phone) == 11 and  phone.startswith("09") == True:
        print("phonenumber is true")
        
    elif len(phone) == 13 and phone.startswith("+989") == True:
         print("phonenumber is true")
    
    elif len(phone) == 14 and phone.startswith("+9899") == True:
        print("phonenumber is true")
                
    else:
        raise Exception(f"invalid phone number: {phone}")   
     
     
phone_validator(phone)     