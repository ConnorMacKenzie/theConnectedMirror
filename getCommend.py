import speech

def getCommand():
    
    s = speech.Speech()
    words = s.record().split()

    isLED = False
    isNews = False
    isWeather = False
    
    if words[0] != 'mirror':
        return

    for word in words:
        if word == 'news':
            isNews = True
        if word == 'weather':
            isWeather = True
        if word == 'LED':
            isLED = True

    if isNews:
        for word in words:
            if word == 'on':
                return 'news on'
            elif word == 'off':
                return 'news off'
           
    if isWeather:
        for word in words:
            if word == 'on':
                return 'weather on'
            elif word == 'off':
                return 'weather off'
            
    if isLED == True:
        for word in words:
            if word == 'on':
                for word in words:
                    if word == '1':
                        return 'LED 1 on'
                    if word == '2':
                        return 'LED 2 on'
                    if word == '3':
                        return 'LED 3 on'
                    if word == '4':
                        return 'LED 4 on'
                    if word == '5':
                        return 'LED 5 on'
            elif word == 'off':
                return 'LED off'
            
