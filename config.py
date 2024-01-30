import json
#config worker

def main():
    while True:
        print("กรุณาเลือกเมนู")
        print("1. ตั้งค่า API")
        print("2. ตั้งค่า Worker")
        print("3. ออกจากโปรแกรม")
        
        try:
            menu = int(input("เลือกเมนู: "))
            
            if menu == 1:
                setupApi()
            elif menu == 2:
                editWorker()
            elif menu == 3:
                print("ออกจากโปรแกรม")
                break
            else:
                print("กรุณาเลือกเมนูใหม่")
        except ValueError:
            print("กรุณาป้อนตัวเลขเท่านั้น")
            
def setupApi():
    with open('./data/api.json', 'r') as f:
        url_data = json.load(f)
        url = url_data.get('url')
    print("API ของคุณตอนนี้คือ " + url)
    print("กรุณากรอก API ที่มีข้อมูล pool, wallet, password ")
    print("เช่น https://raw.githubusercontent.com/danunaise/ccminer-verus-autostart/main/data/data.json")
    url = input("กรุณากรอก API ของคุณ: ")
    with open('./data/api.json', 'w') as f:
        json.dump(url, f)
        print("บันทึกข้อมูล API เรียบร้อยแล้ว")

def editWorker():
    with open('./data/worker.json', 'r') as f:
        worker_data = json.load(f)
        worker = worker_data.get('worker')
    print("worker ของคุณตอนนี้คือ " + worker)
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

if __name__ == "__main__":
    main()