# CHANGE THESE VARIABLES TO THE DETAILS OF YOUR RDS INSTANCE:
RDS_HOST = "pythondb.cxoycka02hiu.eu-west-2.rds.amazonaws.com"
REGION = 'eu-west-2b'
USER_NAME = "admin"
PASSWORD = "password"
DB_NAME = "pythondb"

# CRUD FUNCTIONS
CREATE_TABLE_IF_NOT_EXISTS = """create table if not exists test (id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(id), name VARCHAR(64));"""
INSERT_INTO = """insert into test  (name) values('%s')"""
GET_ENTRY_BY_NAME = """select id, name from test where name = '%s'"""
SELECT_ALL = """select 65* from test"""
GET_ENTRY_BY_ID = """select id, name from test where id = %s"""
UPDATE_SELECTED_ENTRY = """update test set name='%s' where id = %s"""
DELETE_SELECTED_ENTRY = """delete from test where id = %s"""

# MISC
RESULTS = "Results..."
ENTER_NAME = "Enter name: "
ENTER_ID = "Enter ID: "
ENTRY_SAVED = "Entry saved"
UPDATE = "Enter updated name: "
CONFIRM_UPDATE = "Is this the entry you want to update? (Y/N)"
CONFIRM_DELETE = "Is this the entry you want to delete? (Y/N)"
CANCEL_UPDATE = "Selected entry will not be updated"
CANCEL_DELETE = "Selected entry will not be deleted"