import requests
import re
import argparse



def get_age(name): 
    print(name)
    #replace the space with underscore 
    name = name.replace(" ", "_")
    
    #create url by adding name
    url = f"http://en.wikipedia.org/wiki/{name}"
    
    #get html
    response = requests.get(url)
    html = response.text
    
    #extracting age from html 
    pattern = "\(age.+\d{2}\)"
    age = re.findall(pattern, html)[0]
    age = age.split(";")[-1].replace(")", "")
    
    #creating an fstring for the name and how 
    name = name.replace("_", " ")
    result = f"{name.title()} is {age} years old"
    
    #returning output from function 
    return result 


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")

    args=parser.parse_args()
    result= get_age(args.name)
    print(result)
