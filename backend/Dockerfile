FROM python:3.12-slim                                   
# we are asking to install the ver of py of 3.12, if any higher it wont work

WORKDIR /app                                             
# this creates a new directory called app

COPY requirements.txt .                                  
# it copies the txt file from the folder to /app in the 

RUN pip install --no-cache-dir -r requirements.txt     
# no cache is like to delete what ever there is in the txt file and reinstall all again

COPY . .                                                 
# its to copy all the files and put it in the new directory

EXPOSE 8001                                              
# this is the expose the port 

CMD ["uvicorn", "main:app","--host","0.0.0.0", "--port", "8001"]               
# comands to run 0 0 0 0 is like the house no. and 8000 is like the door no.

