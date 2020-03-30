function WebBanking (arg)
    -- sets global variables
    -- these fields are mandatory but lupa erros are very confusing, so I will manage them in the bse.lua module
    version = arg.version
    url = arg.url
    services = arg.services
    description = arg.description
end

-- TODO implement proper version update
MM = {productName = "bse", productVersion="0.1.0"}

function MM.localizeText(str)
    --[[
    Mit dieser Funktion kann ein Text übersetzt werden. Diese Funktion ist primär für die mit MoneyMoney
    ausgelieferten Extensions gedacht. Sie ist ein Wrapper für die Cocoa-Funktion NSLocalizedString und liefert
    natürlich nur dann eine Übersetzung, wenn der Text in MoneyMoney hinterlegt worden ist.

    Parameter:
    String str: Englischer Text

    Rückgabewert:
    String str: Übersetzter Text
    ]]
    bse_log:debug("[MM] localizeText is not implemented")
    return str
end

function MM.localizeDate(...--[[ [format, ]date]])
    --[[
    Lokalisiert eine Zeitangabe. Da die von Lua unterstützten POSIX Locales innerhalb von macOS-Apps nicht zur
    Verfügung stehen, baut diese Funktion auf der Cocoa-Klasse NSDateFormatter auf.

    Parameter:
    String format (optional): Ausgabeformat; Die Angabe erfolgt wie bei der Cocoa-Klasse NSDateFormatter nach dem
    Unicode Technical Standard #35.
    Number date: Datum; Die Angabe erfolgt in Form eines POSIX-Zeitstempels.

    Rückgabewert:
    String str: Datum im lokalisierten Format
    ]]
end

function MM.localizeNumber(...--[[ [format, ]num]])
    --[[
    Lokalisiert eine Zahl. Da die von Lua unterstützten POSIX Locales innerhalb von macOS-Apps nicht zur Verfügung
    stehen, baut diese Funktion auf der Cocoa-Klasse NSNumberFormatter auf.

    Parameter:
    String format (optional): Ausgabeformat; Die Angabe erfolgt wie bei der Cocoa-Klasse NSNumberFormatter nach dem
    Unicode Technical Standard #35.
    Number num: Zahl

    Rückgabewert:
    String str: Zahl im lokalisierten Format
    ]]
end

function MM.localizeAmount(...--[[ [format, ]amount[, currency] ]])
    --[[
    Lokalisiert einen Währungsbetrag.

    Parameter:
    String format (optional): Ausgabeformat; Die Angabe erfolgt wie bei der Cocoa-Klasse NSNumberFormatter nach dem
    Unicode Technical Standard #35.
    Number amount: Betrag
    String currency (optional): Währung; Ohne diesen Parameter wird nur der Betrag ohne Währungsangabe zurückgegeben.

    Rückgabewert:
    String str: Währungsbetrag im lokalisierten Format
    ]]
end

function MM.urlencode(... --[[str, [charset] ]])
    --[[
    Wendet eine URL-Kodierung an.

    Parameter:
    String str: Zu kodierender Text
    String charset (optional): Zeichensatz; Die Angabe erfolgt wie bei HTTP nach IANA. Ohne diesen Parameter wird ISO-8859-1 verwendet.

    Rückgabewert:
    String urlencoded: URL-kodierter Text.
    ]]
end

function MM.urldecode(urlencoded)
    --[[
    Entfernt die URL-Kodierung.

    Parameter:
    String urlencoded: URL-kodierter Text.

    Rückgabewert:
    String str: Text ohne URL-Kodierung.
    ]]
end

function MM.toEncoding(... --[[charset, str[, bom] ]])
    --[[
    Konvertiert einen Text von UTF-8 zu einem anderen Zeichensatz.

    Parameter:
    String charset: Zeichensatz; Die Angabe erfolgt wie bei HTTP nach IANA.
    String str: Text in UTF-8
    Boolean bom (optional): Wenn dieser Parameter mit true belegt ist, wird der Rückgabewert um eine Byte Order Mark
    (BOM) ergänzt, sofern sie für den angegeben Zeichensatz existiert.

    Rückgabewert:
    Binary data: Text im angegebenen Zeichensatz
    ]]
end

function MM.fromEncoding(charset, data)
    --[[
    Konvertiert einen Text von einem anderen Zeichensatz zu UTF-8.

    Parameter:
    String charset: Zeichensatz; Die Angabe erfolgt wie bei HTTP nach IANA.
    Binary data: Text im angegebenen Zeichensatz

    Rückgabewert:
    String str: Text in UTF-8
    ]]
end

function MM.base64(data)
    --[[
    Konvertiert Daten zu Base64.

    Parameter:
    Binary data: Zu konvertierende Daten

    Rückgabewert:
    String encoded: Base64-kodierte Daten
    ]]
end

function MM.base64decode(encoded)
    --[[
    Konvertiert Daten von Base64.

    Parameter:
    Binary encoded: Base64-kodierte Daten

    Rückgabewert:
    String data: konvertierte Daten
    ]]
end

function MM.sha512(data)
    --[[
    Berechnet einen SHA512-, SHA256-, SHA1- oder MD5-Hashwert.

    Parameter:
    Binary data: Daten, über die der Hashwert berechnet werden soll.

    Rückgabewert:
    String digest: Hashwert als hexidezimaler String
    ]]
end

function MM.sha256(data)
    --[[
    Berechnet einen SHA512-, SHA256-, SHA1- oder MD5-Hashwert.

    Parameter:
    Binary data: Daten, über die der Hashwert berechnet werden soll.

    Rückgabewert:
    String digest: Hashwert als hexidezimaler String
    ]]
end

function MM.sha1(data)
    --[[
    Berechnet einen SHA512-, SHA256-, SHA1- oder MD5-Hashwert.

    Parameter:
    Binary data: Daten, über die der Hashwert berechnet werden soll.

    Rückgabewert:
    String digest: Hashwert als hexidezimaler String
    ]]
end

function MM.md5(data)
    --[[
    Berechnet einen SHA512-, SHA256-, SHA1- oder MD5-Hashwert.

    Parameter:
    Binary data: Daten, über die der Hashwert berechnet werden soll.

    Rückgabewert:
    String digest: Hashwert als hexidezimaler String
    ]]
end

function MM.hmac512(key, data)
    --[[
    Berechnet einen HMAC512-, HMAC384- oder HMAC256-Message-Authentication-Code.

    Parameter:
    Binary key: HMAC-Schlüssel
    Binary data: Daten, über die der Message Authentication Code berechnet werden soll.

    Rückgabewert:
    Binary digest: Message Authentication Code als binärer String
    ]]
end

function MM.hmac384(key, data)
    --[[
    Berechnet einen HMAC512-, HMAC384- oder HMAC256-Message-Authentication-Code.

    Parameter:
    Binary key: HMAC-Schlüssel
    Binary data: Daten, über die der Message Authentication Code berechnet werden soll.

    Rückgabewert:
    Binary digest: Message Authentication Code als binärer String
    ]]
end

function MM.hmac256(key, data)
    --[[
    Berechnet einen HMAC512-, HMAC384- oder HMAC256-Message-Authentication-Code.

    Parameter:
    Binary key: HMAC-Schlüssel
    Binary data: Daten, über die der Message Authentication Code berechnet werden soll.

    Rückgabewert:
    Binary digest: Message Authentication Code als binärer String
    ]]
end

function MM.time()
    --[[
    Gibt die aktuelle Uhrzeit zurück. Im Gegensatz zum Aufruf os.time() enthält der Rückgabewert auch Millisekunden
    als Nachkommestellen.

    Rückgabewert:
    Number timestamp: Aktuelle Uhrzeit in Form eines POSIX-Zeitstempels.
    ]]
end

function MM.sleep(seconds)
    --[[
    Unterbricht die Ausführung des Skripts für ein paar Sekunden.

    Parameter:
    Number seconds: Anzahl der Sekunden
    ]]
end

function MM.printStatus(...)
    --[[
    Diese Funktion arbeitet ähnlich zur Lua-Funktion print: Die Parameter werden mittels der Lua-Funktion tostring
    zu einem String konvertiert und im Protokoll-Fenster von MoneyMoney angezeigt. Zusätzlich wird der String als
    Statusmeldung in der GUI angezeigt.
    ]]
    print(arg)
end
