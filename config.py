import json
#config worker
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
    print("บันทึกข้อมูลเรียบร้อยแล้ว")