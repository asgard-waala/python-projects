
import urllib.request as url_request


def main(url):
    print("Checking connectivity...")  
    response = url_request.urlopen(url)  
    print(f"Conneted to {url} successfully!")
    print("The response was:", response.getcode())
    
print("This is a website connetivity checker program.")
input_url = input("Enter the URL of the website you want to check: ")

main(input_url)