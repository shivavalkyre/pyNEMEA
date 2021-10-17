import psycopg2
from pyais.stream import TCPStream



con = psycopg2.connect(database="masdex_dev", user="postgres", password="dbapptgprK2021", host="37.44.244.235", port="5432")
print("Database opened successfully")

cur = con.cursor()

host = '202.43.178.187'
port = 4711


for msg in TCPStream(host,port):
    #json_data = msg.decode().to_json()
    #print(json_data)
    decoded_message = msg.decode()
    ais_content = decoded_message.content
    msg_type = int(ais_content['type'])
    #print(ais_content['type'])
    #print(ais_content)
   
    #q = "INSERT INTO tbl_ais(type,repeat,mmsi,status,turn) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(status)s,%(turn)s)"
    #cur.execute(q, ais_content)
    #con.commit()

    if msg_type == 1 or msg_type == 2 or msg_type == 3 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,status,turn,speed,accuracy,lon,lat,course,heading,second,maneuver,raim,radio) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(status)s,%(turn)s,%(speed)s,%(accuracy)s,%(lon)s,%(lat)s,%(course)s,%(heading)s,%(second)s,%(maneuver)s,%(raim)s,%(radio)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 4 or msg_type == 11 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,year,month,day,hour,minute,second,accuracy,lon,lat,epfd,raim,radio) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(year)s,%(month)s,%(day)s,%(hour)s,%(minute)s,%(second)s,%(accuracy)s,%(lon)s,%(lat)s,%(epfd)s,%(raim)s,%(radio)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 5 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,ais_version,imo,callsign,shipname,shiptype,to_bow,to_stern,to_port,to_starboard,epfd,month,day,hour,minute,draught,destination,dte) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(ais_version)s,%(imo)s,%(callsign)s,%(shipname)s,%(shiptype)s,%(to_bow)s,%(to_stern)s,%(to_port)s,%(to_starboard)s,%(epfd)s,%(month)s,%(day)s,%(hour)s,%(minute)s,%(draught)s,%(destination)s,%(dte)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 6 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,seqno,dest_mmsi,retransmit,dac,fid,data) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(seqno)s,%(dest_mmsi)s,%(retransmit)s,%(dac)s,%(fid)s,%(data)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 7 or msg_type == 13 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,mmsi1,mmsiseq1,mmsi2,mmsiseq2,mmsi3,mmsiseq3,mmsi4,mmsiseq4) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(mmsi1)s,%(mmsiseq1)s,%(mmsi2)s,%(mmsiseq2)s,%(mmsi3)s,%(mmsiseq3)s,%(mmsi4)s,%(mmsiseq4)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 8 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,dac,fid,data) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(dac)s,%(fid)s,%(data)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 9 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,alt,speed,accuracy,lon,lat,course,second,dte,assigned,raim,radio) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(alt)s,%(speed)s,%(accuracy)s,%(lon)s,%(lat)s,%(course)s,%(second)s,%(dte)s,%(assigned)s,%(raim)s,%(radio)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 10 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,dest_mmsi) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(dest_mmsi)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 12 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,seqno,dest_mmsi,retransmit,text) VALUES(%(type)s, %(repeat)s, %(mmsi)s, %(seq_no)s,%(dest_mmsi)s,%(retransmit)s,%(text)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 14 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,text) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(text)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 15 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,mmsi1,type1_1,offset1_1,mmsi2,type2_1,offset2_1) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(mmsi1)s,%(type1_1)s,%(offset1_1)s,%(mmsi2)s,%(type2_1)s,%(offset2_1)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 16 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,mmsi1,offset1,increment1,mmsi2,offset2,increment2) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(mmsi1)s,%(offset1)s,%(increment1)s,%(mmsi2)s,%(offset2)s,%(increment2)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 17 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,lon,lat,data) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(lon)s,%(lat)s,%(data)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 18 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,speed,accuracy,lon,lat,course,heading,second,regional,cs,display,dsc,band,msg22,assigned,raim,radio) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(speed)s,%(accuracy)s,%(lon)s,%(lat)s,%(course)s,%(heading)s,%(second)s,%(regional)s,%(cs)s,%(display)s,%(dsc)s,%(band)s,%(msg22)s,%(assigned)s,%(raim)s,%(radio)s)"
        cur.execute(q, ais_content)
        con.commit()
    elif msg_type == 19 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,speed,accuracy,lon,lat,course,heading,second,regional,shipname,shiptype,to_bow,to_stern,to_port,to_starboard,epfd,raim,dte,assigned) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(speed)s,%(accuracy)s,%(lon)s,%(lat)s,%(course)s,%(heading)s,%(second)s,%(regional)s,%(shipname)s,%(shiptype)s,%(to_bow)s,%(to_stern)s,%(to_port)s,%(to_starboard)s,%(epfd)s,%(raim)s,%(dte)s,%(assigned)s)"
        cur.execute(q, ais_content)
        con.commit()  
    elif msg_type == 20 :
        q = "INSERT INTO tbl_ais(type,repeat,mmsi,offset1,number1,timeout1,increment1,offset2,number2,timeout2,increment2,offset3,number3,timeout3,increment3,offset4,number4,timeout4,increment4) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(offset1)s,%(number1)s,%(timeout1)s,%(increment1)s,%(offset2)s,%(number2)s,%(timeout2)s,%(increment2)s,%(offset3)s,%(number3)s,%(timeout3)s,%(increment3)s,%(offset4)s,%(number4)s,%(timeout4)s,%(increment4)s)"
        cur.execute(q, ais_content)
        con.commit()  
    elif msg_type == 24 :
        if "shipname" in ais_content:
            q = "INSERT INTO tbl_ais(type,repeat,mmsi,partno,shipname) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(partno)s,%(shipname)s)"
            cur.execute(q, ais_content)
            con.commit()
        else :
            q = "INSERT INTO tbl_ais(type,repeat,mmsi,partno,shiptype,vendorid,model,serial,callsign,to_bow,to_stern,to_port,to_starboard,mothership_mmsi) VALUES(%(type)s, %(repeat)s, %(mmsi)s,%(partno)s,%(shiptype)s,%(vendorid)s,%(model)s,%(serial)s,%(callsign)s,%(to_bow)s,%(to_stern)s,%(to_port)s,%(to_starboard)s,%(mothership_mmsi)s)"
            cur.execute(q, ais_content)
            con.commit()
    
     