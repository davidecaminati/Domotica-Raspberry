from flask import Flask, url_for
import smbus
import time

bus = smbus.SMBus(1) # Rev 2 Pi uses 1
DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Register for outputs
GPIOA  = 0x12 # Register for output
GPIOB  = 0x13 # Register for inputs
bus.write_byte_data(DEVICE,IODIRA,0x00)
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/releon/<int:number>')
def api_articles(number):
    if number > 8 or number < 1:
        print 'this rele not exist \n'
        return 'error'
    NeedChange = False
    OldState = bus.read_byte_data(DEVICE,GPIOB)
    BinReleNumber = 2** (number - 1)
    if OldState == '0b0':
        NeedChange = True
        bus.write_byte_data(DEVICE,OLATA,BinReleNumber)
    else:
        #is already on ?
        print 'number ' + str(number) + '\n'
        print 'OldState ' + str(OldState) + '\n'
        print 'BinReleNumber ' + str(BinReleNumber) + '\n'
        if BinReleNumber & OldState == BinReleNumber:
            NeedChange = False
            print 'already done \n'
            return 'already done'
        else:
            NeedChange = True
            bus.write_byte_data(DEVICE,OLATA,BinReleNumber)
    time.sleep(0.3)
    bus.write_byte_data(DEVICE,OLATA,0)
    time.sleep(0.3)
    #test if rele has changed
    NewState = bus.read_byte_data(DEVICE,GPIOB)
    print NewState
    print OldState
    if NeedChange:
        if NewState != OldState:
            return 'ok'
        else:
            return 'malfunction'

			

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()
