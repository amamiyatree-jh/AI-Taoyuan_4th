import pymysql
import os, sys, time
import prettytable as pt
#from pynput import keyboard


link=pymysql.connect(
	host = "localhost",
	user ="root",
	passwd = "",
	db = "python_ai",
	charset = "utf8",
	port = 3306
)

cur=link.cursor()

def add_member(link,cur):
	os.system('clear')
	param={
	"name":input("會員姓名： "),
	"birthday":input("會員生日： "),
	"address":input("會員地址： "),
	}

	cur.execute("INSERT INTO `member`(`name`,`birthday`,`address`) "+
	"VALUES(%(name)s,%(birthday)s,%(address)s)",
	param)
	link.commit()
	newid=cur.lastrowid
	print("剛剛新增的那筆資料的ID:",newid)
	time.sleep(2)
	return

def member_BYID_del(link,cur):
	os.system('clear')
	p=pt.PrettyTable(["ID","name","birthday","address"], encoding="utf8")
	del_ID = input('請輸入需要刪除的會員ID: ')
	sql_line = "SELECT * FROM `member` WHERE ID = " + del_ID
	cur.execute(sql_line)
	ret=cur.fetchall()
	for d in ret:
		p.add_row(d)
	print(p)
	del_ans = input('確認是否刪除 Y or N ？ --> ' )
	if del_ans == 'Y':
		cur.execute("DELETE FROM `member` WHERE ID = "+ del_ID)
		print('！！！！會員資料已經刪除！！！！')
	else:
		print('！！放棄刪除！！')
		pass
				
	time.sleep(3)
	return

def member_BYID_upBR(link,cur):
	os.system('clear')
	p=pt.PrettyTable(["ID","name","birthday","address"], encoding="utf8")
	del_ID = input('請輸入需要修改地址的會員ID: ')
	sql_line = "SELECT * FROM `member` WHERE ID = " + del_ID
	cur.execute(sql_line)
	ret=cur.fetchall()
	for d in ret:
		p.add_row(d)
	print(p)
	del_ans = input('確認是否修改 Y or N ？ --> ' )
	if del_ans == 'Y':
		member_BR = input('請輸入會員地址：')
		cur.execute("UPDATE `member` SET `address` = '" + member_BR + "' WHERE ID = "+ del_ID)
		print('！！！！會員資料已經修改！！！！')
	else:
		print('！！放棄修改！！')
		pass
				
	time.sleep(3)
	return

def show_member_Info(link,cur):
	os.system('clear')

	p=pt.PrettyTable(["ID","name","birthday","address"], encoding="utf8")
	cur.execute("SELECT * FROM `member`")
	ret=cur.fetchall()
	for d in ret:
		p.add_row(d)
	print(p)
	time.sleep(5)
	return

while True:
	os.system('clear')
	print('＝＝＝!!歡迎!!使用 會員管理系統 ＝＝＝\n' +
		'請輸入數字選擇所要的功能\n' +
		'1 -- 新增會員資料\n' +
		'2 -- 依照ID刪除會員資料\n' +
		'3 -- 依照ID修改會員地址資料\n' +
		'4 -- 顯示會員資料\n' +
		'5 -- 離開程式\n'
		)
	function_number = input('輸入所需功能為(1-5)： ')
	try:
		function_number = int(function_number)
		if isinstance(function_number,int):
			if function_number >= 6 :
				print('！！輸入錯誤請重新輸入！！\n')
				time.sleep(2)
				os.system('clear')
				continue
			else:
				pass
	except Exception as e:
		print('！！你輸入的不是數字！！\n')
		time.sleep(2)
		os.system('clear')
		continue

	if function_number == 1:
		add_member(link,cur)

	if function_number == 2:
		member_BYID_del(link,cur)

	if function_number == 3:
		member_BYID_upBR(link,cur)

	if function_number == 4:
		show_member_Info(link,cur)

	if function_number == 5:
		sys.exit()

link.close()