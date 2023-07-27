import sys
import sqlite3
import json
import concurrent.futures
import logging
import time

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('/tmp/mylog.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def rm_eventx_from_db(sqlitefilename,logger):
    try:
        conn = sqlite3.connect(sqlitefilename)
        cursor = conn.cursor()

        cursor.execute('SELECT ID,LOG FROM OLD_LOGS')
        idlist=[]

        for row in cursor.fetchall():
            colid = row[0]
            msg = row[1]
            m = msg.decode('utf-8')
            msgjson = json.loads(m)
            # print(msgjson['_normalized_fields']['event_id'])
            if msgjson['_normalized_fields']['event_id'] == 36870:
                idlist.append(colid)
        for delete_id in idlist:
            cursor.execute('DELETE FROM OLD_LOGS WHERE ID = ?', (delete_id,))

        conn.commit()

        cursor.close()
        conn.close()
        logger.warning(f"processing done for {sqlitefilename}")
    except Exception as e:
        logger.warning(f"rm_eventx_from_db err: {sqlitefilename} "+str(e))

def vaccumdb(sqlitefilename):
    try:
        conn = sqlite3.connect(sqlitefilename)
        cursor = conn.cursor()
        cursor.execute('VACUUM')
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as e:
        logger.warning(f"vaccum_db err: {sqlitefilename} "+str(e))    

def main():
    start_time = time.perf_counter()
    futures=[]
    listfile=sys.argv[1]
    base_path=sys.argv[2]


    with open(listfile, 'r') as file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            for line in file:
                line = line.strip()
                file_path=base_path+str(line)
                print(file_path)
                futures.append(executor.submit(rm_eventx_from_db,file_path,logger))
        for future in concurrent.futures.as_completed(futures):
            logger.warning("futures msg : "+str(future.result()))      
    fut_vac=[]
    with open(listfile, 'r') as file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            for line in file:
                line = line.strip()
                file_path=base_path+line
                fut_vac.append(executor.submit(vaccumdb,file_path))
    for future in concurrent.futures.as_completed(fut_vac):
        logger.warning("vaccum futures msg : "+str(future.result()))             
            
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Elapsed time: {execution_time:.6f} Seconds")

if __name__ == "__main__":
    main()
