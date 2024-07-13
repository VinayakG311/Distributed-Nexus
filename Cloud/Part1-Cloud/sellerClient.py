import sys
import threading
from concurrent import futures
import grpc
import grpc_tools
import time
import market_pb2
import market_pb2_grpc
import concurrent
import uuid
import Notification_pb2
import Notification_pb2_grpc
# https://www.tutorialspoint.com/python-program-to-find-the-ip-address-of-the-client
import socket
port = sys.argv[1]
hostname = socket.gethostname()
ipAddr = socket.gethostbyname(hostname)
notification_server_ip=ipAddr+":50052"
ipAddr = ipAddr + ":" + port
seller = market_pb2.Seller(UUID="-1", address="1", products=[])

s_id = ""
s_addr = ""
s = seller
categories = ["ELECTRONICS", "FASHION", "OTHERS"]


# ---------------------------------Seller---------------------------------
def registerSeller(stub):
    global s, s_id, s_addr
    id = str(uuid.uuid1())
    s_id = id

    seller = market_pb2.Seller(UUID=str(id), address=ipAddr, products=[])
    req = market_pb2.registerSellerReq(address=ipAddr, uuid=id,notif_ip=notification_server_ip)
    res = stub.registerSeller(req)
    if (res.status == 0):
        print(f"Success,Seller registered with uuid : {id}")
        s_addr = ipAddr
        s = seller
    else:

        print(f"Failure,Seller with address {ipAddr} already exists")


def addItem(stub):
    global s
    name = input("Enter product name : ")
    qty = int(input("Enter product quantity : "))
    description = input("Enter product description : ")
    sellerAddress = ipAddr
    price = float(input("Enter prodcut price : "))
    sellerUUID = s_id
    category = int(input("Enter category (Elec 0, Fas 1, Oth 2)"))

    req = market_pb2.sellItemReq(name=name, quantity=qty, description=description, sellerAddress=sellerAddress,
                                 price=price, sellerUUID=sellerUUID, Category=categories[category], seller=s)
    res = stub.sellItem(req)

    if res != None:
        print(f'SUCCESS. Product has been added with uuid {res.productUUID}')
        s = res.seller
    else:
        print('FAILURE')


# print(f"Product added with UUID : {res.productUUID}")


def DeleteItem(stub):
    id = input("Enter product id of the product to be deleted : ")
    s_uuid = input('Enter Seller id : ')
    s_aadr = input('Enter Seller Address : ')

    req = market_pb2.DeleteItemReq(Product_UUID=id, seller_UUID=s_uuid, seller_address=s_aadr)
    res = stub.deleteProduct(req)
    if res.status == 'SUCCESS':
        for p in s.products:
            if p.Product_UUID == id:
                s.products.remove(p)
        print('SUCCESS')
    else:
        print('FAILURE')


def UpdateItem(stub):
    global s
    p_id = input("Enter product id of the product to be Updated : ")
    s_uuid = input('Enter Seller id : ')
    s_aadr = input('Enter Seller Address : ')
    Price = int(input('Enter Updated price : '))
    Quant = int(input('Enter Updated Quant : '))
    Desc = input('Enter Updated Desc : ')

    req = market_pb2.UpdateItemReq(Product_UUID=p_id, seller_UUID=s_uuid, seller_address=s_aadr, price=Price,
                                   quantity=Quant, description=Desc, seller=s)
    res = stub.updateProduct(req)

    if (res.status == 'SUCCESS'):
        print('SUCCESS')
        for p in s.products:
            if p.Product_UUID == p_id:
                p.price = Price
                p.description = Desc
                p.quantity = Quant
    else:
        print('FAILURE')


def DisplayItem(stub):
    s_uuid = input('Enter Seller id : ')
    s_aadr = input('Enter Seller Address : ')
    res = stub.displayProducts(s)
    print(res)


def run():
    try:
        while True:
            with grpc.insecure_channel('10.128.0.3:50051') as channel:
                stub = market_pb2_grpc.MarketStub(channel)
                print(
                    '1: Register\n 2: Add Product\n 3: Delete Product\n 4: Update Product\n 5: Display Products\n 6: Exit\n')
                a = int(input('Enter Choice : '))
                if a == 1:
                    registerSeller(stub)
                elif a == 2:
                    addItem(stub)
                elif a == 3:
                    DeleteItem(stub)
                elif a == 4:
                    UpdateItem(stub)
                elif a == 5:
                    DisplayItem(stub)
                else:
                    break
    except KeyboardInterrupt:
        return


class NotificationServicer(Notification_pb2_grpc.NotificationServicer):
    def Notif1(self, request, context):
        print(request.message)
        return Notification_pb2.void2()

def runserver():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    Notification_pb2_grpc.add_NotificationServicer_to_server(NotificationServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(3600)  # One hour
    except KeyboardInterrupt:
        server.stop(0)

t=[]
if __name__ == '__main__':
    th = threading.Thread(target=run)
    th2 = threading.Thread(target=runserver)
    t.append(th)
    t.append(th2)
    try:
        for i in t:

            i.start()
        for i in t:
            i.join()
    except KeyboardInterrupt:

        sys.exit(0)
    # try:
    #     th.start()
    #     th2.start()
    #     th.join()
    #     th2.join()
    #
    # except KeyboardInterrupt:
    #
    #     sys.exit(0)
