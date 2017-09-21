#ポケモン素早さ形容辞書
sp2 = {"1":"無振り","2":"準速","3":"最速","4":"最遅"}

#ポケモン素早さ辞書型（dict型）
pokesSpeed = {
	5:"ナマコブシ、ツボツボ",
	20:"メガヤミラミ、メガバクーダ、コータス、シュバルゴ、ナットレイ",
	25:"サマヨール、ギガイアス",
	30:"""
	（メガ）ヤドラン、カビゴン、ヤドキング、（メガ）ハガネール、メガユキノオー、
	デスカーン、モロバレル
	""",
	35:"ヌオー、ドヒドイデ、バンバドロ、シロデスナ",
	36:"ジジーロン、デンヂムシ",
	39:"トリトドン",
	40:"バクーダ、ヌケニン、ドサイドン、グソクムシャ、ダダリン",
	42:"オニシズクモ",
	43:"ユレイドル、クワガノン",
	44:"ドラミドロ",
	45:"ガラガラ（R)、メガデンリュウ、ローブシン",
	47:"カバルドン",
	50:"""
	ベトベトン（R)、ラッキー、マリルリ、ハリテヤマ、（メガ）クチート、ヤミラミ、
	（メガ）ボスゴドラ、３レジ、メレシー
	""",
	55:"イーブイ、オムスター、デンリュウ、ハピナス",
	56:"オーロット",
	58:"ズルズキン",
	59:"ブロスター、タイプ：ヌル",
	60:"""
	ピクシー、ポリゴン２、ラグラージ、エンペルト、ユキノオー、ジバコイル、ブルンゲル、
	ギルガルド、ニンフィア、ガオガエン、アシレーヌ、ヤレユータン、メテノ
	""",
	61:"テッカグヤ、バンギラス",
	65:"ハッサム、サンドパン（R)、シャワーズ、ブラッキー、ブースター、ペリッパー、グレイシア",
	67:"ランターン",
	68:"バクオング",
	70:"""
	レアコイル、パルシェン、エアームド、カポエラー、メガラグラージ、ルンパッパ、
	キノガッサ、メタグロス、キリキザン
	""",
	71:"メガバンギラス",
	72:"アマージョ",
	75:"メガハッサム、メガヘラクロス、ドーブル、クレッフィ、カプ・ブルル",
	77:"ヒードラン",
	78:"（メガ）カメックス",
	79:"バイバニラ、マッシブーン",
	80:"""
	（メガ）フシギバナ、カブトプス、カイリュー、バシャーモ、サーナイト、オニゴーリ、
	フワライド、トゲキッス、マンムー、エルレイド、シャンデラ、ウォーグル、バルジーナ、
	ヌメルゴン
	""",
	81:"ミロカロス、（メガ）ギャラドス",
	83:"ブーバーン、デンジュモク",
	85:"ヘラクロス、キングドラ、スイクン、クレセリア、ジャラランガ、カプ・レヒレ",
	86:"ロトムFC",
	88:"ドリュウズ",
	90:"ピカチュウ、ガルーラ、カイオーガ、グラードン、ルカリオ、ポリゴンZ、ギギギアル",
	91:"ヤミカラス、霊獣ランド",
	92:"ワルビアル",
	95:"ウインディ、サメハダー、リーフィア、エレキブル、グライオン、シルヴァディ、カプ・テテフ",
	96:"トゲデマル、ミミッキュ",
	97:"オノノクス",
	98:"サザンドラ",
	99:"ゼルネアス",
	100:"""
	リザードン（メガ）、メガガルーラ、サンダー、メガバシャーモ、メガサーナイト、
	ボーマンダ、ウルガモス
	""",
	101:"霊獣ボルト",
	102:"ガブリアス",
	103:"ウツロイド",
	105:"メガサメハダー、ライボルト",
	106:"レパルダス",
	108:"ゴウカザル、デンチュラ、テラキオン",
	109:"キュウコンR、カミツルギ、アイアント",
	110:"ライチュウ（R)、ゲンガー、エーフィ、メガメタグロス、ラティ兄弟、メガエルレイド",
	111:"化身ボルト",
	112:"メガルカリオ",
	113:"ジャローダ",
	115:"ペルシアン（R)、メガレックウザ",
	116:"エルフーン",
	120:"メテノ（コア）、フーディン、ジュカイン、メガボーマンダ",
	122:"ゲッコウガ",
	123:"オンバーン",
	125:"マニューラ",
	126:"ファイアロー",
	130:"メガゲンガー、カプ・コケコ、サンダース、プテラ",
	135:"メガライボルト、メガミミロップ",
	145:"メガジュカイン、メガスピアー",
	150:"メガフーディン、メガプテラ",
	151:"フェローチェ"
}




#入力されたポケモンの実数値計算
def calc(pokemon):
	sem = pokemon + 52
	max = int(sem*1.1)
	std = pokemon + 20
	min = int((pokemon + 5)*0.9)
	return std,sem,max,min

#計算結果の記述
def tellMine(std,sem,max,min,effect,sign):
	if sign == 1:
		fmt = """
	このポケモンの{effect}段階上昇の素早さ実数値は、
	無振りで{std}、準速で{sem}、最速で{max}、最遅で{min}となります。
		"""
		print(fmt.format(effect = effect,std = std,sem = sem,max = max,min = min))	
	elif sign == -1:
		fmt = """
	このポケモンの{effect}段階下降の素早さ実数値は、
	無振りで{std}、準速で{sem}、最速で{max}、最遅で{min}となります。
		"""
		print(fmt.format(effect = effect,std = std,sem = sem,max = max,min = min))
	else :
		fmt = """
	このポケモンの素早さ実数値は、
	無振りで{std}、準速で{sem}、最速で{max}、最遅で{min}となります。
		"""
		print(fmt.format(std = std,sem = sem,max = max,min = min))

#採用する値の決定
def decisVal(button):
	if button == 1:
		speed = n1
	elif button == 2:
		speed = n2
	elif button == 3:
		speed = n3
	else :
		speed = n4
	return speed

#選択した素早さのポケモンがギリギリ抜けるラインのポケモンの素早さを計算 
def calcEnemy(value):
	std = value - 20 -1
	sem = value - 52 - 1
	max = 0	# mine = int((enemy + 52)*1.1) + 1
	while int((max+52)*1.1) < value-1:
		max += 1
	###########上の文だけでよいはずだが何故かこの文が抜けるとバグ#####################
	if max % 11 == 0:
		max -= 1
	#################################ここまで###################################
	return std,sem,max

#どんな素早さ種族値を抜けるかを記述
def tellPokeSp(std,sem,max,sp,pokemon,mine,effect,sign):
	if sign == 1:
		fmt = """
	{pokemon}族の{sp}の{effect}段階上昇した素早さは、{mine} で、
	{std}族の無振り、{sem}族の準速、{max}族の最速ポケモンを抜いています。
		"""
		print(fmt.format(pokemon = pokemon,sp = sp2[sp],effect = effect,
			mine = mine,std = std, sem = sem,max = max))
	elif sign == -1:
		fmt = """
	{pokemon}族の{sp}の{effect}段階下降した素早さは、{mine} で、
	{std}族の無振り、{sem}族の準速、{max}族の最速ポケモンを抜いています。
		"""
		print(fmt.format(pokemon = pokemon,sp = sp2[sp],effect = effect,
			mine = mine,std = std, sem = sem,max = max))
	else:	
		fmt = """
	{pokemon}族の{sp}の素早さは、{mine} で、
	{std}族の無振り、{sem}族の準速、{max}族の最速ポケモンを抜いています。
		"""
		print(fmt.format(pokemon = pokemon,sp = sp2[sp],
			mine = mine,std = std, sem = sem,max = max))

#素早さ付近のポケモンを計算
def findPoke(value):
	count = 0 
	writeList = []
	values = []
	while count < 3:	
		if value in pokesSpeed :
			writeList += [pokesSpeed[value]]
			values += [value]
			count += 1
			value -= 1
		else:
			value -= 1	
	return writeList,values

#素早さ付近のポケモンを記述
def tellFind(lis,vals,sp):
	fmt = """
	{sp0}の
	{speed0}族:{pokes0}
	{speed1}族:{pokes1}
	{speed2}族:{pokes2}
	"""
	print(fmt.format(sp0 = sp2[sp],speed0 = vals[0],pokes0 = lis[0],
					 speed1 = vals[1],pokes1 = lis[1],
					 speed2 = vals[2],pokes2 = lis[2]),end="")

#素早さのエフェクト
def sChange(s,effect,sign):
	if sign == 1:
		if effect == 1:
			s *= 1.5
		elif effect == 2:
			s *= 2
	elif sign == -1:
		if effect == 1:
			s *= 2
			s /= 3
		elif effect == 2:
			s *= 0.5 		
	return int(s)



#main文のようななにか
print("やめるときは[q]キーを入力してください。")
while True:
	sign = 0
	effect = [0,0]	#
	for x in range(3):
		print("")
	pokemon = input("ポケモンの素早さ種族値(半角整数)を入力してください。")
	#s効果判定
	if pokemon.find("+") != -1:
		effect = pokemon.split("+")
		pokemon = effect[0]
		sign = 1
	elif pokemon.find("-") != -1:
		effect = pokemon.split("-")
		pokemon = effect[0]
		sign = -1
	###############################################
	if pokemon == "q":
		exit()
	
	n1,n2,n3,n4 = calc(int(pokemon))
	##speed effect
	if sign != 0:
		n1 = sChange(n1,int(effect[1]),sign)
		n2 = sChange(n2,int(effect[1]),sign)
		n3 = sChange(n3,int(effect[1]),sign)
		n4 = sChange(n4,int(effect[1]),sign)

	tellMine(n1,n2,n3,n4,int(effect[1]),sign)
	sp = input("特に知りたい素早さはどれですか？1:無振り、2:準速、3:最速、4:最遅、q:やめる  ")
	if sp == "q":
		exit()
	mySpeed = decisVal(int(sp))
	N1,N2,N3 = calcEnemy(mySpeed)
	tellPokeSp(N1,N2,N3,sp,pokemon,mySpeed,int(effect[1]),sign)

	more = input("抜いているポケモンについて調べますか？y:はい、n:いいえ、q:やめる  ")
	if more == "q":
		exit()
	elif more == "n":
		continue
	elif more == "y":
		stdList,stdVals = findPoke(int(N1))
		semList,semvals = findPoke(int(N2))
		maxList,maxVals = findPoke(int(N3))
		print("選択した素早さのポケモンは")
		tellFind(stdList,stdVals,"1")
		tellFind(semList,semvals,"2")
		tellFind(maxList,maxVals,"3")
		print("")
		print("等のポケモンを抜きます。")




#素早さ種族値がマイナスになる場合のバグ修正
#
#
#
#