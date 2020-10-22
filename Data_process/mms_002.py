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
	os.system('cls')
	param={
	"name":input("會員姓名： "),
	"birthday":input("會員生日： "),
	"address":input("會員地址： "),
	"tel":input("會員電話： "),
	"newid" : " ",
	}

	cur.execute("INSERT INTO `member`(`name`,`birthday`,`address`) "+
	"VALUES(%(name)s,%(birthday)s,%(address)s)",
	param)
	link.commit()
	newid=cur.lastrowid
	print("剛剛新增的那筆資料的ID:",newid)

	param['newid'] = newid

	cur.execute("INSERT INTO `tel`(`member_id`,`tel`) "+
	"VALUES(%(newid)s,%(tel)s)",
	param)
	link.commit()	

	time.sleep(2)
	return

def member_BYID_del(link,cur):
	os.system('cls')
	show_member_Info(link,cur)
	del_ID = input('請輸入需要刪除的會員ID: ')
	del_ans = input('確認是否刪除 Y or N ？ --> ' )
	if del_ans == 'Y':
		cur.execute("DELETE FROM `member` WHERE `ID` = "+ del_ID)
		print('！！！！會員資料已經刪除！！！！')
	else:
		print('！！放棄刪除！！')
		pass
				
	time.sleep(3)
	return

def member_BYID_upBR(link,cur):
	os.system('cls')
	show_member_Info(link,cur)
	del_ID = input('請輸入需要修改的會員ID: ')
	del_ans = input('確認是否修改 Y or N ？ --> ' )
	if del_ans == 'Y':
		
		param={
			"member_id": del_ID,
			"name":input("請輸入會員姓名："),
			"birthday":input("請輸入會員生日："),
			"address":input("請輸入會員地址：")
		}
		cur.execute("UPDATE `member` SET" + 
			" `name` = %(name)s," + 
			" `birthday` = %(birthday)s," +
			" `address` = %(address)s"+ 
			" WHERE `id` = %(member_id)s", param)

		link.commit()
		print('！！！！會員資料已經修改！！！！')
	else:
		print('！！放棄修改！！')
		pass
				
	time.sleep(3)
	return

def show_member_Info(link,cur):
	os.system('cls')
	p=pt.PrettyTable(["ID","name","birthday","address","tel"], encoding="utf8")
	cur.execute("select case when a.table_id > 1 THEN '"''"'ELSE a.id END as '"'id'"', case when a.table_id > 1 THEN '"''"'ELSE a.name END as '"'name'"', case when a.table_id > 1 THEN '"''"'ELSE a.birthday END as '"'birthday'"', case when a.table_id > 1 THEN '"''"'ELSE a.address END as '"'address'"', a.tel from ( select rank()over(PARTITION by a.id ORDER by a.tel) as '"'table_id'"',a.id,a.name,a.birthday,a.address,a.tel from(select a.*,b.tel,b.member_id from `member` as a LEFT join `tel` as b on a.`id` = b.`member_id`) as a ) as a")
	ret=cur.fetchall()
	for d in ret:
		p.add_row(d)
	print(p)
	time.sleep(5)
	return

def member_tel_add(link,cur):
	os.system('cls')
	show_member_Info(link,cur)
	del_ID = input('請輸入需要增加電話的會員ID: ')
	del_ans = input('確認是否增加 Y or N ？ --> ' )
	if del_ans == 'Y':
		
		param={
			"member_id": del_ID,
			"tel":input("請輸入會員電話："),
		}
		cur.execute("INSERT INTO `tel`(`member_id`,`tel`) "+
			"VALUES(%(member_id)s,%(tel)s)",
			param)
		
		link.commit()
		newid=cur.lastrowid
		print("剛剛新增的那筆資料的ID:",newid)
		print('！！！！會員電話已經增加！！！！')
	else:
		print('！！放棄修改！！')
		pass
				
	time.sleep(3)
	return

def member_tel_del(link,cur):
	os.system('cls')
	show_member_Info(link,cur)
	del_ID = input('請輸入需要修改的會員ID: ')
	del_ans = input('確認是否修改 Y or N ？ --> ' )
	if del_ans == 'Y':
		os.system('cls')
		p=pt.PrettyTable(["ID","member_id","tel"], encoding="utf8")
		cur.execute("SELECT * FROM `tel` WHERE `member_id` = " + del_ID)
		ret=cur.fetchall()
		for d in ret:
			p.add_row(d)
		print(p)
		del_ID2 = input('請輸入需要修改電話的ID: ')

		param={
			"tel":input("請輸入修改需要電話："),
		}
		cur.execute("UPDATE `tel` SET" + 
			" `tel` = %(tel)s WHERE `id` = " + del_ID2

			,param)
		link.commit()
		print('！！！！會員電話已經修改！！！！')
	else:
		print('！！放棄修改！！')
		pass
	time.sleep(3)
	return

while True:
	os.system('cls')
	show_member_Info(link,cur)
	print('＝＝＝!!歡迎!!使用 會員管理系統 ＝＝＝\n' +
		'請輸入數字選擇所要的功能\n' +
		'1 -- 顯示會員資料\n' +
		'2 -- 新增會員資料\n' +
		'3 -- 刪除會員資料\n' +
		'4 -- 修改會員資料\n' +
		'5 -- 新增會員電話\n' +
		'6 -- 修改會員電話\n' +
		'0 -- 離開程式\n'
		)
	function_number = input('輸入所需功能為(1-5)： ')
	try:
		function_number = int(function_number)
		if isinstance(function_number,int):
			if function_number >= 7 :
				print('！！輸入錯誤請重新輸入！！\n')
				time.sleep(2)
				os.system('cls')
				continue
			else:
				pass
	except Exception as e:
		print('！！你輸入的不是數字！！\n')
		time.sleep(2)
		os.system('cls')
		continue

	if function_number == 0:
		sys.exit()

	if function_number == 1:
		show_member_Info(link,cur)

	if function_number == 2:
		add_member(link,cur)

	if function_number == 3:
		member_BYID_del(link,cur)

	if function_number == 4:
		member_BYID_upBR(link,cur)

	if function_number == 5:
		member_tel_add(link,cur)

	if function_number == 6:
		member_tel_del(link,cur)		

link.close()