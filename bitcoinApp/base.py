import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc

import tkinter as tk
from tkinter import ttk

import urllib
import json

import numpy as np
import pandas as pd

NORMAL_FONT=("Verdana",10,'bold')
SMALL_FONT=("Verdana",9,'bold')
LARGE_FONT=("Verdana",12,'bold')
style.use("ggplot")


f=plt.figure()
#a=f.add_subplot(111)
#a.plot([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])

exchange="BTC-e"
DatCounter=9000
programName="btce"

resampleSize="15Min"
dataPace="tick"
candleWidth=0.008
paneCount=1

topIndicator='none'
mainIndicator='none'
bottomIndicator='none'
EMAs=[]
SMAs=[]

chartLoad=True

darkColor="#183A54"
lightColor="#00A3E0"

def addTopIndicator(what):
	global topIndicator
	global DatCounter
	
	if dataPace=='tick':
		popupmsg("Indicators in tick data not availble.")
	elif what=='none':
		topIndicator=what
		DatCounter=9000
	elif what=='rsi':
		topIndicator=what
		rsiQ=tk.Tk()
		rsiQ.wm_title("Periods?")
		label=ttk.Label(rsiQ,text="Choose how many periods you want ach RSI calculation to consider.")
		label.pack(side="top",fill="x",pady=10)

		e=ttk.Entry(rsiQ)
		e.insert(0,14)
		e.pack()
		e.focus_set()

		def callback():
			global topIndicator
			global DatCounter

			periods=(e.get())
			group=[]
			group.append("rsi")
			group.append(periods)

			topIndicator=group
			DatCounter=9000
			print("set top indicator to ",group)
			rsiQ.destroy()

		btn=ttk.Button(rsiQ,text="Submit",command=callback).pack()
		tk.mainloop()
	elif what=='macd':
		topIndicator="macd"
		DatCounter=9000

def addBottomIndicator(what):
	global bottomIndicator
	global DatCounter
	
	if dataPace=='tick':
		popupmsg("Indicators in tick data not availble.")
	elif what=='none':
		bottomIndicator=what
		DatCounter=9000
	elif what=='rsi':
		bottomIndicator=what
		rsiQ=tk.Tk()
		rsiQ.wm_title("Periods?")
		label=ttk.Label(rsiQ,text="Choose how many periods you want ach RSI calculation to consider.")
		label.pack(side="top",fill="x",pady=10)

		e=ttk.Entry(rsiQ)
		e.insert(0,14)
		e.pack()
		e.focus_set()

		def callback():
			global bottomIndicator
			global DatCounter

			periods=(e.get())
			group=[]
			group.append("rsi")
			group.append(periods)

			bottomIndicator=group
			DatCounter=9000
			print("set bottom indicator to ",group)
			rsiQ.destroy()

		btn=ttk.Button(rsiQ,text="Submit",command=callback).pack()
		tk.mainloop()
	elif what=='macd':
		bottomIndicator="macd"
		DatCounter=9000

def addMainIndicator(what):
	global mainIndicator
	global DatCounter
	
	if dataPace=='tick':
		popupmsg("Indicators in tick data not availble.")

	if what !='none':
		if mainIndicator=='none':
			if what == 'sma':
				midIQ=tk.Tk()
				midIQ.wm_title("Periods")
				label=ttk.Label(midIQ,text="Choose how many periods you want your SMA to be .")
				label.pack(side='top',pady=10,fill='x')
				e=ttk.Entry(midIQ)
				e.insert(0,10)
				e.pack()
				e.focus_set()

				def callback():
					global mainIndicator
					global DatCounter

					mainIndicator=[]
					periods=(e.get())
					group=[]
					group.append("sma")
					group.append(int(periods))
					mainIndicator.append(group)
					DatCounter=9000
					print("Middle Indicator set to :",mainIndicator)
					midIQ.destroy()

				btn=ttk.Button(midIQ,text="Submit",command=callback).pack()
				tk.mainloop()
			if what == 'ema':
				midIQ=tk.Tk()
				midIQ.wm_title("Periods")
				label=ttk.Label(midIQ,text="Choose how many periods you want your EMA to be .")
				label.pack(side='top',pady=10,fill='x')
				e=ttk.Entry(midIQ)
				e.insert(0,10)
				e.pack()
				e.focus_set()

				def callback():
					global mainIndicator
					global DatCounter

					mainIndicator=[]
					periods=(e.get())
					group=[]
					group.append("ema")
					group.append(int(periods))
					mainIndicator.append(group)
					DatCounter=9000
					print("Middle Indicator set to :",mainIndicator)
					midIQ.destroy()

				btn=ttk.Button(midIQ,text="Submit",command=callback).pack()
				tk.mainloop()	
		else:
			if what == 'sma':
				midIQ=tk.Tk()
				midIQ.wm_title("Periods")
				label=ttk.Label(midIQ,text="Choose how many periods you want your SMA to be .")
				label.pack(side='top',pady=10,fill='x')
				e=ttk.Entry(midIQ)
				e.insert(0,10)
				e.pack()
				e.focus_set()

				def callback():
					global mainIndicator
					global DatCounter

					#middleIndicators=[]
					periods=(e.get())
					group=[]
					group.append("sma")
					group.append(int(periods))
					mainIndicator.append(group)
					DatCounter=9000
					print("Middle Indicator set to :",mainIndicator)
					midIQ.destroy()

				btn=ttk.Button(midIQ,text="Submit",command=callback).pack()
				tk.mainloop()
			if what == 'ema':
				midIQ=tk.Tk()
				midIQ.wm_title("Periods")
				label=ttk.Label(midIQ,text="Choose how many periods you want your EMA to be .")
				label.pack(side='top',pady=10,fill='x')
				e=ttk.Entry(midIQ)
				e.insert(0,10)
				e.pack()
				e.focus_set()

				def callback():
					global mainIndicator
					global DatCounter

					#middleIndicators=[]
					periods=(e.get())
					group=[]
					group.append("ema")
					group.append(int(periods))
					mainIndicator.append(group)
					DatCounter=9000
					print("Middle Indicator set to :",mainIndicator)
					midIQ.destroy()

				btn=ttk.Button(midIQ,text="Submit",command=callback).pack()	
				tk.mainloop()
	else:
		mainIndicator='none'

def startStopFunc(value):
	global chartLoad
	chartLoad=value

def popupmsg(msg):
	popup=tk.Tk()

	popup.wm_title("!")
	label=ttk.Label(popup,text=msg,font=NORMAL_FONT).pack(side="top",fill="x",pady=10)
	B1=ttk.Button(popup,text="OK",command=lambda:popup.destroy()).pack()
	popup.mainloop()


def changeTimeFrame(tf):
	global dataPace
	global DatCounter
	if tf=="7d" and resampleSize=="1Min":
		popupmsg("TOO MUCH DATA CHOSEN , CHOSE A SMALLER INTERVAL")
	else:
		dataPace=tf
		DatCounter=9000

def changeSampleSize(size,width):
	global resampleSize
	global DatCounter
	global candleWidth
	if dataPace=="7d" and resampleSize=="1Min":
		popupmsg("TOO MUCH DATA CHOSEN , CHOSE A SMALLER INTERVAL")
	if dataPace=='tick':
		popupmsg("YOU'RE VIEWING TICK DATA,NOT OHLCI")
	else:
		resampleSize=size
		DatCounter=9000	
		candleWidth=width

def changeExchange(toWhat,pn):
	global exchange
	global DatCounter
	global programName

	exchange=toWhat
	programName=pn
	DatCounter=9000

def animate(i):
	global refreshRate
	global DatCounter

	if chartLoad:
		if paneCount==1:
			if dataPace=='tick':
				try:
					if exchange=='BTC-e':

						a=plt.subplot2grid((6,4),(0,0),rowspan=5,colspan=4)
						a2=plt.subplot2grid((6,4),(5,0),rowspan=1,colspan=4,sharex=a)

						dataLink="https://wex.nz/api/3/trades/btc_usd?limit=2000"
						data=urllib.request.urlopen(dataLink)
						data=data.read().decode("utf-8")
						data=json.loads(data)
						
						data=data["btc_usd"]
						data=pd.DataFrame(data)

						data["datestamp"]=np.array(data['timestamp']).astype("datetime64[s]")
						allDates=data["datestamp"].tolist()


						buys=data[(data['type']=="bid")]
						#buys["datestamp"]=np.array(buys["timestamp"]).astype("datetime64[s]")
						buyDates=(buys["datestamp"]).tolist()


						sells=data[(data['type']=="ask")]
						#sells["datestamp"]=np.array(sells["timestamp"]).astype("datetime64[s]")
						sellDates=(sells["datestamp"]).tolist()

						volume=data["amount"]


						a.clear()
						a.plot_date(buyDates,buys["price"],lightColor,label="buys")
						a.plot_date(sellDates,sells["price"],darkColor,label="sells")
						
						a2.fill_between(allDates,0,volume,facecolor=darkColor)
						
						a.xaxis.set_major_locator(mticker.MaxNLocator(5))
						a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
						plt.setp(a.get_xticklabels(),visible=False)

						a.legend(bbox_to_anchor=(0,1.02,1,.102),loc=3,ncol=2,borderaxespad=0)
						a.set_title("BTC-e BTCUSD Prices\nLast Price:"+str(data["price"][1999]))
						a.set_xlabel("Date and Time")
						a.set_ylabel("Price in $")
						priceData=data['price'].apply(float).tolist()
						print("Graph revised")
					if exchange=='Bitstamp':

						a=plt.subplot2grid((6,4),(0,0),rowspan=5,colspan=4)
						a2=plt.subplot2grid((6,4),(5,0),rowspan=1,colspan=4,sharex=a)

						dataLink="https://www.bitstamp.net/api/transactions/"
						data=urllib.request.urlopen(dataLink)
						data=data.read().decode("utf-8")
						data=json.loads(data)
						
						data=pd.DataFrame(data)

						data["datestamp"]=np.array(data['date'].apply(int)).astype("datetime64[s]")
						dateStamps=data['datestamp'].tolist()
						#allDates=data["datestamp"].tolist()

						volume=data["amount"].apply(float).tolist()

						a.clear()
						a.plot_date(dateStamps,data["price"],lightColor,label="buys")
						
						a2.fill_between(dateStamps,0,volume,facecolor=darkColor)
						
						a.xaxis.set_major_locator(mticker.MaxNLocator(5))
						a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
						plt.setp(a.get_xticklabels(),visible=False)	

						a.legend(bbox_to_anchor=(0,1.02,1,.102),loc=3,ncol=2,borderaxespad=0)
						a.set_title("Bitstamp BTCUSD Prices\nLast Price:"+str(data["price"][0]))
						a.set_xlabel("Date and Time")
						a.set_ylabel("Price in $")
						priceData=data['price'].apply(float).tolist()	
						print("Graph revised")
					if exchange=='Bitfinex':

						a=plt.subplot2grid((6,4),(0,0),rowspan=5,colspan=4)
						a2=plt.subplot2grid((6,4),(5,0),rowspan=1,colspan=4,sharex=a)

						dataLink="https://api.bitfinex.com/v1/trades/btcusd?limit=2000"
						data=urllib.request.urlopen(dataLink)
						data=data.read().decode("utf-8")
						data=json.loads(data)
						
						data=pd.DataFrame(data)

						data["datestamp"]=np.array(data['timestamp']).astype("datetime64[s]")
						allDates=data["datestamp"].tolist()


						buys=data[(data['type']=="buy")]
						#buys["datestamp"]=np.array(buys["timestamp"]).astype("datetime64[s]")
						buyDates=(buys["datestamp"]).tolist()


						sells=data[(data['type']=="sell")]
						#sells["datestamp"]=np.array(sells["timestamp"]).astype("datetime64[s]")
						sellDates=(sells["datestamp"]).tolist()

						volume=data["amount"].apply(float).tolist()


						a.clear()
						a.plot_date(buyDates,buys["price"],lightColor,label="buys")
						a.plot_date(sellDates,sells["price"],darkColor,label="sells")
						plt.setp(a.get_xticklabels(),visible=False)

						a2.fill_between(allDates,0,volume,facecolor=darkColor)
						
						a.xaxis.set_major_locator(mticker.MaxNLocator(5))
						a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))

						a.legend(bbox_to_anchor=(0,1.02,1,.102),loc=3,ncol=2,borderaxespad=0)
						a.set_title("Bitfinex BTCUSD Prices\nLast Price:"+str(data["price"][0]))
						a.set_xlabel("Date and Time")
						a.set_ylabel("Price in $")
						priceData=data['price'].apply(float).tolist()
						print("Graph revised")
					if exchange=='Huobi':

						a=plt.subplot2grid((6,4),(0,0),rowspan=6,colspan=4)

						dataLink="https://seaofbtc.com/api/basic/price?key=1&tf=1d&exchange=huobi"
						data=urllib.request.urlopen(dataLink)
						data=data.read().decode("utf-8")
						data=json.loads(data)
						
						dateStamp=np.array(data[0]).astype("datetime64[s]")
						dateStamp=dateStamp.tolist()

						df=pd.DataFrame({'Datetime':dateStamp})

						df['Price']=data[1]
						df['Volume']=data[2]
						df['Symbole']="BTCUSD"

						df['MPLDate']=df['Datetime'].apply(lambda date:mdates.date2num(date.to_pydatetime()))
						df=df.set_index("Datetime")

						lastPrice=df['Price'][-1]


						data["datestamp"]=np.array(data['timestamp']).astype("datetime64[s]")
						allDates=data["datestamp"].tolist()

						a.clear()
						a.plot_date(df['MPLDate'][-4500:],df["Price"][-4500:],lightColor,label="Price")
						
						a.xaxis.set_major_locator(mticker.MaxNLocator(5))
						a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))

						a.set_title("HUOBI BTCUSD Prices\nLast Price:"+str(lastPrice))
						a.set_xlabel("Date and Time")
						a.set_ylabel("Price in $")

						a.legend(bbox_to_anchor=(0,1.02,1,.102),loc=3,ncol=2,borderaxespad=0)
						priceData=df['price'].apply(float).tolist()	
						print("Graph revised")
							
				except Exception as e:
					print("Falied because of :",e)
			else:
				if DatCounter>12:
					try:
						if exchange=="Huobi":
							if topIndicator!="none":
								a=plt.subplot2grid((6,4),(1,0),rowspan=5,colspan=4)
								a2=plt.subplot2grid((6,4),(0,0),rowspan=1,colspan=4,sharex=a) 
							else:
								a=plt.subplot2grid((6,4),(0,0),rowspan=5,colspan=4)
						else:
							if topIndicator!='none' and bottomIndicator!='none':
								#Main
								a=plt.subplot2grid((6,4),(1,0),rowspan=3,colspan=4)
								#Volume
								a2=plt.subplot2grid((6,4),(4,0),sharex=a,rowspan=1,colspan=4)
								#Bottom Indicator
								a3=plt.subplot2grid((6,4),(5,0),sharex=a,rowspan=1,colspan=4)
								#Top Indicator
								a0=plt.subplot2grid((6,4),(0,0),sharex=a,rowspan=1,colspan=4)
							elif topIndicator!="none":
								#Main
								a=plt.subplot2grid((6,4),(1,0),rowspan=4,colspan=4)
								#Top Indicator
								a0=plt.subplot2grid((6,4),(0,0),sharex=a,rowspan=1,colspan=4)
								#Volume
								a2=plt.subplot2grid((6,4),(5,0),sharex=a,rowspan=1,colspan=4)
							elif bottomIndicator!="none":
								#Main
								a=plt.subplot2grid((6,4),(0,0),rowspan=4,colspan=4)
								#Volume
								a2=plt.subplot2grid((6,4),(4,0),sharex=a,rowspan=1,colspan=4)
								#Bottom Indicator
								a3=plt.subplot2grid((6,4),(5,0),sharex=a,rowspan=1,colspan=4)
							else:
								#Main
								a=plt.subplot2grid((6,4),(0,0),rowspan=4,colspan=4)
								#Volume
								a2=plt.subplot2grid((6,4),(5,0),sharex=a,rowspan=1,colspan=4)
						data=urllib.request.urlopen("http://seaofbtc.com/api/basic/price?key=1&tf="+dataPace+"&exchange="+programName).read()
						data=data.decode()
						data=json.loads(data)
						dateStamp=np.array(data[0]).astype("datetime64[s]")
						dateStamp=dateStamp.tolist()

						df=pd.DataFrame({'Datetime':dateStamp})

						df['Price']=data[1]
						df['Volume']=data[2]
						df['Symbol']='BTCUSD'
						df['MPLDate']=df['Datetime'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
						df=df.set_index("Datetime")

						OHLC=df['Price'].resample(resampleSize,how="ohlc")
						OHLC=OHLC.dropna()

						volumeData=df['Volume'].resample(resampleSize,how={'volume':'sum'})

						OHLC["dateCopy"]=OHLC.index
						OHLC["MPLDates"]=OHLC['dateCopy'].apply(lambda date:mdates.date2num(date.to_pydatetime()))

						del OHLC['dateCopy']

						volumeData["dateCopy"]=volumeData.index
						volumeData["MPLDates"]=volumeData['dateCopy'].apply(lambda date:mdates.date2num(date.to_pydatetime()))

						del volumeData['dateCopy']

						priceData=OHLC['close'].apply(float).tolist()	

						a.clear()

						if mainIndicator!='none':
							for eachMA in mainIndicator:
								if eachMA[0]=="sma":
									sma=pd.rolling_mean(OHLC["close"],eachMA[1])
									label=str(eachMA[1]+" SMA")
									a.plot(OHLC["MPLDates"],sma,label=label)
								if eachMA[0]=="ema":
									ewma=pd.stats.moments.ewma
									label=str(eachMA[1]+" EMA")
									a.plot(OHLC["MPLDates"],ewma(OHLC["close"],eachMA[1]),label=label)

							a.legend(loc=0)
						if topIndicator[0]=="rsi":
							rsiIndicator(priceData,"top")
						elif topIndicator[0]=="macd":
							try:
								computeMACD(priceData,location="top")
							except Exception as e:
								print(str(e))
							
						if bottomIndicator[0]=="rsi":
							rsiIndicator(priceData,"bottom")
						elif bottomIndicator[0]=="macd":
							try:
								computeMACD(priceData,location="bottom")
							except Exception as e:
								print(str(e))
						csticks=candlestick_ohlc(a,OHLC[["MPLDates","open","high","low","close"]].values,
							width=candleWidth,colorup=lightColor,colordown=darkColor)
						a.set_ylabel("Price")
						if exchange!="Huobi":
							a2.fill_between(volumeData["MPLDates"],0,volumeData['volume'],facecolor=darkColor)
							a2.set_ylabel("Volume")
						a.xaxis.set_major_locator(mticker.MaxNLocator(3))
						a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

						if exchange!="Huobi":
							plt.setp(a.get_xticklabels(),visible=False)
						if topIndicator!="none":
							plt.setp(a0.get_xticklabels(),visible=False)
						if bottomIndicator!="none":
							plt.setp(a2.get_xticklabels(),visible=False)

						x=len(OHLC['close'])-1

						if dataPace=='1d':
							title=exchange+" 1 Day Data with "+resampleSize+" Bars\nLast Price:"+str(OHLC['close'][x])
						if dataPace=='3d':
							title=exchange+" 3 Day Data with "+resampleSize+" Bars\nLast Price:"+str(OHLC['close'][x])
						if dataPace=='7d':
							title=exchange+" 7 Day Data with "+resampleSize+" Bars\nLast Price:"+str(OHLC['close'][x])
						if topIndicator!="none":
							a0.set_title(title)
						else:
							a.set_title(title)

						print("New Graph ")
						DatCounter=0
					except Exception as e:
						print("Failed in the no-tick animate :",e)
						DatCounter=9000
				else:
					DatCounter+=1


class SeaOfBTCApp(tk.Tk):

	def __init__(self,*args,**kwargs):

		tk.Tk.__init__(self,*args,**kwargs)
		tk.Tk.wm_title(self,"Bitcoin Application")

		container=tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		menubar=tk.Menu(container)
		filemenu=tk.Menu(menubar,tearoff=0)
		filemenu.add_command(label="Save settings",command=lambda:popupmsg("Not supported just yet"))
		filemenu.add_separator()
		filemenu.add_command(label="Exit",command=quit)
		menubar.add_cascade(label="File",menu=filemenu)

		exchangeChoice=tk.Menu(menubar,tearoff=1)
		exchangeChoice.add_command(label="BTC-e",command=lambda:changeExchange("BTC-e","btce"))
		exchangeChoice.add_command(label="Bitfinex",command=lambda:changeExchange("Bitfinex","bitfinex"))
		exchangeChoice.add_command(label="Bitstamp",command=lambda:changeExchange("Bitstamp","bitstamp"))
		exchangeChoice.add_command(label="Huobi",command=lambda:changeExchange("Huobi","huobi"))
		menubar.add_cascade(label="Exchange",menu=exchangeChoice)

		dataTf=tk.Menu(menubar,tearoff=1)
		dataTf.add_command(label="Tick",command=lambda:changeTimeFrame('tick'))
		dataTf.add_command(label="1 Day",command=lambda:changeTimeFrame('1d'))
		dataTf.add_command(label="3 Day",command=lambda:changeTimeFrame('3d'))
		dataTf.add_command(label="1 Week",command=lambda:changeTimeFrame('7d'))
		menubar.add_cascade(label="Data time frame",menu=dataTf)

		OHLCI=tk.Menu(menubar,tearoff=1)
		OHLCI.add_command(label="Tick",command=lambda:changeTimeFrame('tick'))
		OHLCI.add_command(label="1 Min",command=lambda:changeSampleSize("1Min",0.0005))
		OHLCI.add_command(label="5 Min",command=lambda:changeSampleSize("5Min",0.003))
		OHLCI.add_command(label="15 Min",command=lambda:changeSampleSize("15Min",0.008))
		OHLCI.add_command(label="30 Min",command=lambda:changeSampleSize("30Min",0.016))
		OHLCI.add_command(label="1 Hour",command=lambda:changeSampleSize("1H",0.032))
		OHLCI.add_command(label="3 Hour",command=lambda:changeSampleSize("3H",0.096))
		menubar.add_cascade(label="OHLC Interval",menu=OHLCI)

		topIndi=tk.Menu(menubar,tearoff=1)
		topIndi.add_command(label="None",command=lambda:addTopIndicator("none"))
		topIndi.add_command(label="RSI",command=lambda:addTopIndicator("rsi"))
		topIndi.add_command(label="MACD",command=lambda:addTopIndicator("macd"))
		menubar.add_cascade(label="Top Indicator",menu=topIndi)

		mainIndi=tk.Menu(menubar,tearoff=1)
		mainIndi.add_command(label="None",command=lambda:addMainIndicator("none"))
		mainIndi.add_command(label="SMA",command=lambda:addMainIndicator("sma"))
		mainIndi.add_command(label="EMA",command=lambda:addMainIndicator("ema"))
		menubar.add_cascade(label="Main/Middle Indicator",menu=mainIndi)

		bottomIndi=tk.Menu(menubar,tearoff=1)
		bottomIndi.add_command(label="None",command=lambda:addBottomIndicator("none"))
		bottomIndi.add_command(label="RSI",command=lambda:addBottomIndicator("rsi"))
		bottomIndi.add_command(label="MACD",command=lambda:addBottomIndicator("macd"))
		menubar.add_cascade(label="Bottom Indicator",menu=bottomIndi)

		startStop=tk.Menu(menubar,tearoff=1)
		startStop.add_command(label="Start",command=lambda:startStopFunc(True))
		startStop.add_command(label="Stop",command=lambda:startStopFunc(False))
		menubar.add_cascade(label="Start/Stop",menu=startStop)


		tk.Tk.config(self,menu=menubar)



		self.frames=dict()

		for f in (StartPage,PageOne,BTCe_page):			

			frame=f(container,self)

			self.frames[f]=frame

			frame.grid(row=0,column=0,sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self,controller):
		frame=self.frames[controller]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="""Alpha Bitcoin trading Application use at your own risk. There is no promise of warranty.""",font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		btn1=ttk.Button(self,text="Agree",command=lambda:controller.show_frame(BTCe_page)).pack()
		btn2=ttk.Button(self,text="Disagree",command=quit).pack()

class PageOne(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="Page 1",font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		btn=ttk.Button(self,text="Back to Home",command=lambda:controller.show_frame(StartPage)).pack()
		btn2=ttk.Button(self,text="Page 2",command=lambda:controller.show_frame(PageTwo)).pack()

class BTCe_page(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="Graph Page",font=LARGE_FONT).pack(pady=10,padx=10)

		btn=ttk.Button(self,text="Back to Home",command=lambda:controller.show_frame(StartPage)).pack()

		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)


app=SeaOfBTCApp()
app.geometry("1280x720")
ani=animation.FuncAnimation(f,animate,interval=2000)
app.mainloop()