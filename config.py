import json
#config worker

def setupApi():
    print("กรุณากรอก API ที่มีข้อมูล pool, wallet, password ")
    print("เช่น https://raw.githubusercontent.com/danunaise/ccminer-verus-autostart/main/data/data.json")
    url = input("API ของคุณ: ")
    with open('./data/api.json', 'w') as f:
        json.dump(url, f)
        print("บันทึกข้อมูล API เรียบร้อยแล้ว")

def editWorker():
    print("กรุณากรอกข้อมูล worker ของคุณ เช่น miner1")
    worker = input("ชื่อ worker ของคุณ: ")

    #config cpu_threads
    print("จำนวน cpu_threads ที่ต้องการใช้ขุด ใส่ค่า 0 - 8")
    cpu_threads = input("cpu_threads ของคุณ: ")

    #save data
    data = {
        "worker": worker,
        "cpu_threads": cpu_threads
    }

    with open('./data/worker.json', 'w') as f:
        json.dump(data, f, indent=2)
        print("บันทึกข้อมูล Worker เรียบร้อยแล้ว")