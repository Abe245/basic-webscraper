import requests #The requests Python library allows you to send HTTP requests and handle the response in your Python code.
import re #The re Python library provides support for regular expressions, which are used to match patterns in strings.



def get_age(name): 
 
    # replace the space with underscore 
    name = name.replace(" ", "_")
    
    # create url by adding name
    url = f"http://en.wikipedia.org/wiki/{name}"
    
    # get html
    response = requests.get(url)
    html = response.text #returuning the return value 

    
    # extracting age from html 
    pattern = "\(age.+\d{2}\)"
    age = re.findall(pattern, html)[0]
    age = age.split(";")[-1].replace(")", "") #when split that means replacing the value for a line. "dog; cat; donkey" would equal 'dog', cat' monkey'
    
    # creating an fstring for the name and how 
    name = name.replace("_", " ")
    result = f"{name.title()} has been alive for {age} years"
    #anything that changes hte string is called string malipulation

    # returning output from function 
    return result 


if __name__=="__main__":

    name = input("Enter name:")

    result = get_age(name)
    print(result)