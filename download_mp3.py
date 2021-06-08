# imported the requests library
import requests
mp3_url = "https://newsonair.gov.in/writereaddata/Bulletins_Audio/Regional/2021/Jun/Regional-Kolkata-Bengali-1950-202167205351.mp3"

output_path = "testing_bn/"
filename = "bengali_1950_202167.mp3"
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(mp3_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open(output_path + filename,'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)