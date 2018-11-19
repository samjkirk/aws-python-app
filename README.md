# aws-python-app

This is a simple command line CRUD application hosted on AWS. It stores a 'name' attribute and an automatically generated ID. Users are able to add, update, delete, and view DB entries.

### Technologies used


- Python3
- AWS
  - RDS
  - VPC
  - EC2 (Ubuntu)

### Prerequisites

You must have a an RDS & EC2 instance set up in the same VPC. 

### Running the program

1. SSH into your EC2 instance...
```
ssh -i "the-location-of-your-ec2-pem-file.pem" ubuntu@your-ubuntu-instance
```
2. Clone this repository and ```cd``` into it.
```
git clone https://github.com/samjkirk/aws-python-app.git
cd aws-python-app
```
3. Use nano to edit the ```Constants.py``` file.
```
nano Constants.py
```
4. Change the values of RDS_HOST, REGION, USER_NAME, PASSWORD, and DB_NAME to match your RDS instance. Save and close the file.
5. Run main.py
```
python3 main.py
```
