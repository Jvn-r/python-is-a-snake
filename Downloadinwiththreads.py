import threading 
import requests
import re 


def download_file(url):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    file_name = re.sub(r'[<>:"/\\|?*]', '', file_name)  # Remove invalid characters
    with open(file_name,'wb') as file:
        file.write(response.content)
    print(f"Dowmnloaded {file_name}")

urls = [
    "https://levellifeup.com/wp-content/uploads/gege-akutami.webp"
]

threads = []
for url in urls:
    thread = threading.Thread(target = download_file,args=(url,))
    threads.append(thread)
    thread.start()
    thread.setName("False_Thread")
    
for thread in threads:
    thread.join()

print("All downloads complete")
print("The thread is called false thread")