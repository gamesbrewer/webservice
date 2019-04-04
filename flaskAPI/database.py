import pymysql
import cx_Oracle

class mysqlDB:
    def __init__(self):
        host = "10.1.12.232"
        user = "tableausuperadmin"
        password = "thisismyboomsticksaidthegreatestmanever"
        db = "tableau"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

class oracleDB:
    def __init__(self):		
        ip = '10.1.12.106'
        port = 1521
        SID = 'HEXP'
        dsn_tns = cx_Oracle.makedsn(ip, port, SID)

        self.con = cx_Oracle.connect('tableausuperadmin', 'thisismyboomsticksaidthegreatestmanever', dsn_tns)
        self.con.autocommit = True
        self.cur = self.con.cursor()

    def list_clients(self):
        self.cur.execute("select ccd01.numcpt, ccd01.numcli, ccd01.datcrt from ccd01_2 ccd01 WHERE rownum <= 100")
        result = []
        for account_no, cif_no, date_registered in self.cur:
            result.append({
            "ACCOUNT NO": account_no,
            "CIF NO": cif_no,
            "ACCOUNT CREATED DATE": date_registered
            })
        return result
