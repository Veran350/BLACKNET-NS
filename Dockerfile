FROM kalilinux/kali-rolling  
RUN apt update && apt install -y python3  
COPY . /app  
WORKDIR /app  
CMD ["python3", "core/menu.py"]  
