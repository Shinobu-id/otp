#coding by : hudaxcode
import requests,json,os
logo = """
__________        __    ________   __          
\______   \ _____/  |_  \_____  \_/  |_______  
 |    |  _//  _ \   __\  /   |   \   __\____ \ 
 |    |   (  <_> )  |   /    |    \  | |  |_> >
 |______  /\____/|__|   \_______  /__| |   __/ 
        \/                      \/     |__|    
 • api from website  : https://otpinaja.com
 • Secrip Created by : hudaxcode
"""
r = requests
try:
	grey = '\x1b[90m'
	red = '\x1b[91m'
	green = '\x1b[92m'
	yellow = '\x1b[93m'
	blue = '\x1b[94m'
	purple = '\x1b[95m'
	cyan = '\x1b[96m'
	white = '\x1b[37m'
	flag = '\x1b[47;30m'
	off = '\x1b[m'
except:
	pass

def cek_tersedian(api):
	z = "https://otpinaja.com/api/services"
	_z = {"api_key":api}
	z_ = r.post(z,_z).text 
	x = json.loads(z_)
	for c in x["data"]:
		print(f" ID :{off}",c["id"],f">{green}",c["nama_aplikasi"],f"\n {off}• {cyan}harga {yellow}:",c["harga_idr"],f"\n {off}• {cyan}total tersedia :{yellow}",c['jumlah_tersedia'])

def order(api,ordr):
	sc = "https://otpinaja.com/api/order"
	_sc = {"api_key":api,"service_id":ordr}
	_p_ = r.post(sc,_sc).text 
	sx = json.loads(_p_)
	xz = sx["data"]
	x = xz["id"]
	nmr = xz["number"]
	if "sukses membeli nomor virtual" in _p_:
		print(" [!] Sukses Membeli Nomor virtual")
		print(f" [!] nomor virtual : {nmr}")
		print(f" [!] id orderan anda : {x}")
	else:
		print(" [!] gagal order aplikasi :( ")

def menu(api):
	print(logo)
	print(" [1] Cek Ketersediaan Aplikasi")
	print(" [2] Membuat pesanan ")
	print(" [3] Checking kode otp")
	print(" [4] Merubah Status pesanan aktif")
	print(" [0] keluar Tools")
	zx = input(" Choose : ")
	if zx =="1":
		cek_tersedian(api)
		input(f" [!] enter untuk kembali > {off}")
		menu(api)
	if zx =="2":
		print(" [!] silahkan masukan id aplikasi ")
		sx = input(" [!] id apk : ")
		order(api,sx)
		input(f" [!] enter untuk kembali > {off}")
		menu(api)
	if zx =="3":
		print(" [!] Masukan id orderan anda ")
		id = input(" [!] id : ")
		cek_otp(api,id)
		input(f" [!] enter untuk kembali > {off}")
		menu(api)
	if zx =="4":
		print( " [!] masukan id orderan anda ")
		id = input(" [!] id : ")
		print("  [ silahkan pilih status ]  ")
		print(" [0] Memproses orderan")
		print(" [1] Cacel orderan aktif")
		print(" [2] Selsai Mengunakan otp")
		xc = input(" choose :")
		if xc =="0":
			x_ = "processing"
			change(api,id,x_)
			input(f" [!] enter untuk kembali > {off}")
			menu(api)
		if xc =="1":
			x_ = "cancel"
			change(api,id,x_)
			input(f" [!] enter untuk kembali > {off}")
			menu(api)
		if xc =="2":
			x_ = "done"
			change(api,id,x_)
			input(f" [!] enter untuk kembali > {off}")
			menu(api)

from time import sleep
def animate(teks):
	lis = list("\|/-")
	for cy in lis:
		print("\r"+str(teks)+"", end="")
		sleep(0.5)

def cek_otp(api,id):
	while True:
		animate(" [*] sedang menunggu otp masuk")
		f = 'https://otpinaja.com/api/status' 
		_ = {"api_key":api,"order_id":id}
		_h_ = r.post(f,_).text 
		d = json.loads(_h_)
		print(d)
		x = d["data"]
		c = x["otp"]
		if "..." in c:
			continue
		if"..." not in c:
			print("\n\n"+c+"\n")
			
	

def change(api,id,st):
	f_ = "https://otpinaja.com/api/set_status"
	_s = {"api_key":api,"order_id":id,"status":st}
	_h_ = r.post(f_,_s).text 
	if "nomor mulai menunggu sms masuk" in _h_:
		print(" [!] nomor mulai menunggu sms masuk")
	if "membatalkan nomor" in _h_:
		print(" [!] membatalkan nomor berhasil")
	else:
		print(" [!] selesai mengunkan nomor virtual")

def api():
	print(" Login Dengan Api terlebih dahulu ")
	x = input(" [!] api : ")
	with open("api.txt","w") as w:
		w.write(x)
	menu(x)
	
def cek_api():
	try:
		op = open("api.txt","r").read()
		menu(op)
	except IOError:
		api()


cek_api()






















