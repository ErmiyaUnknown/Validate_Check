def email_validator(email):
    
    if email.find("@") != -1 and email.find(".") != -1:
        email_username = email.split("@")
        
        if email_username[0].isalnum() == True or (email_username[0].isalnum() == False and email_username[0].find("_") != -1):
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
    
    


def phone_validator(phone): 
    
    if len(phone) == 11 and  phone.startswith("09") == True:
        print("phonenumber is true")
        
    elif len(phone) == 13 and phone.startswith("+989") == True:
         print("phonenumber is true")
    
    elif len(phone) == 14 and phone.startswith("00989") == True:
        print("phonenumber is true")
                
    else:
        raise Exception(f"invalid phone number: {phone}")   
     
     
    
while True:
    
    email = input("email: ")
    if email == "exit":
        break
    
    email_validator(email)
    
    
    phone = input("phone: ")
    if phone == "exit":
        break
    
    phone_validator(phone) 
    