--[[
--
--    Definition: WebBanking Function
--    -------------------------------
--
--    - Sets global variables
--    - All scripts must include one such call
--
--]]
function WebBanking (arg)
    version = arg.version
    url = arg.url
    services = arg.services
    description = arg.description
end

--[[
--
--    Definition: Test Function
--    -------------------------------
--
--    - Sets global variables
--    - Interesting for lua tests
--
--]]
function Test (arg)
    version = bse_version()
    description = arg.description
end

--[[
--
--    Definition: LocalStorage
--    ------------------------
--
--    - The object LocalStorage can be used in the scripts to manage state between API calls
--]]
LocalStorage = {}

--[[
--
--    Definition: MM
--    --------------
--
--    - The MM object is a collection of util methods to ease the development of lua plugins
--
--]]
MM = {productName = "BSE", productVersion=bse_version()}

function MM.localizeText(str)
    -- Mit dieser Funktion kann ein Text übersetzt werden. Diese Funktion ist primär für die mit MoneyMoney
    -- ausgelieferten Extensions gedacht. Sie ist ein Wrapper für die Cocoa-Funktion NSLocalizedString und liefert
    -- natürlich nur dann eine Übersetzung, wenn der Text in MoneyMoney hinterlegt worden ist.
    --
    -- Parameter:
    -- String str: Englischer Text
    --
    -- Rückgabewert:
    -- String str: Übersetzter Text
    bse_log:debug("[MM] localizeText is not implemented")
    return str
end

function MM.localizeDate(...--[[ [format, ]date]])
    -- Lokalisiert eine Zeitangabe. Da die von Lua unterstützten POSIX Locales innerhalb von macOS-Apps nicht zur
    -- Verfügung stehen, baut diese Funktion auf der Cocoa-Klasse NSDateFormatter auf.
    --
    -- Parameter:
    -- String format (optional): Ausgabeformat; Die Angabe erfolgt wie bei der Cocoa-Klasse NSDateFormatter nach dem
    -- Unicode Technical Standard #35.
    -- Number date: Datum; Die Angabe erfolgt in Form eines POSIX-Zeitstempels.
    --
    -- Rückgabewert:
    -- String str: Datum im lokalisierten Format
    local nargs = #{...}
    local format, date
    if nargs == 2 then
        format, date = ...
    elseif nargs == 1 then
        format = nil
        date = ...
    else
        error("[MM.localizeDate] Incorrect parameters. Expected ([format, ]date), found (" .. ... .. ")")
    end
    return bse_localize_date(date, format)
end

function MM.localizeNumber(...--[[ [format, ]num]])
    -- Lokalisiert eine Zahl. Da die von Lua unterstützten POSIX Locales innerhalb von macOS-Apps nicht zur Verfügung
    -- stehen, baut diese Funktion auf der Cocoa-Klasse NSNumberFormatter auf.
    --
    -- Parameter:
    -- String format (optional): Ausgabeformat; Die Angabe erfolgt wie bei der Cocoa-Klasse NSNumberFormatter nach dem
    -- Unicode Technical Standard #35.
    -- Number num: Zahl
    --
    -- Rückgabewert:
    -- String str: Zahl im lokalisierten Format
    local nargs = #{...}
    local format, num
    if nargs == 2 then
        format, num = ...
    elseif nargs == 1 then
        format = nil
        num = ...
    else
        error("[MM.localizeNumber] Incorrect parameters. Expected ([format, ]num), found (" .. table.concat({...},", ") .. ")")
    end
    return bse_localize_number(num, format)
end

function MM.localizeAmount(...--[[ [format, ]amount[, currency] ]])
    -- Lokalisiert einen Währungsbetrag.
    --
    -- Parameter:
    -- String format (optional): Ausgabeformat; Die Angabe erfolgt wie bei der Cocoa-Klasse NSNumberFormatter nach dem
    -- Unicode Technical Standard #35.
    -- Number amount: Betrag
    -- String currency (optional): Währung; Ohne diesen Parameter wird nur der Betrag ohne Währungsangabe zurückgegeben.
    --
    -- Rückgabewert:
    -- String str: Währungsbetrag im lokalisierten Format
    local nargs = #{...}
    local format, num, currency
    if nargs == 3 then
        format, num, currency = ...
    elseif nargs == 2 then
        a, b = ...
        if type(a) == "string" then
            format = a
            num = b
            currency = nil
        else
            format = nil
            num = a
            currency = b
        end
    elseif nargs == 1 then
        format = nil
        num = ...
        currency = nil
    else
        error("[MM.localizeAmount] Incorrect parameters. Expected ([format, ]num[, currency]), found (" .. table.concat({...},", ") .. ")")
    end
    return bse_localize_amount(num, currency, format)
end

function MM.urlencode(str, ...--[[ [charset] ]])
    -- Wendet eine URL-Kodierung an.
    --
    -- Parameter:
    -- String str: Zu kodierender Text
    -- String charset (optional): Zeichensatz; Die Angabe erfolgt wie bei HTTP nach IANA. Ohne diesen Parameter wird ISO-8859-1 verwendet.
    --
    -- Rückgabewert:
    -- String urlencoded: URL-kodierter Text.
    if ... then
        return bse_urlencode(str, ...)
    end
    return bse_urlencode(str)
end

function MM.urldecode(urlencoded)
    -- Entfernt die URL-Kodierung.
    --
    -- Parameter:
    -- String urlencoded: URL-kodierter Text.
    --
    -- Rückgabewert:
    -- String str: Text ohne URL-Kodierung.
    return bse_urldecode(urlencoded)
end

function MM.toEncoding(charset, str, ...--[[ [bom] ]])
    -- Konvertiert einen Text von UTF-8 zu einem anderen Zeichensatz.
    --
    -- Parameter:
    -- String charset: Zeichensatz; Die Angabe erfolgt wie bei HTTP nach IANA.
    -- String str: Text in UTF-8
    -- Boolean bom (optional): Wenn dieser Parameter mit true belegt ist, wird der Rückgabewert um eine Byte Order Mark
    -- (BOM) ergänzt, sofern sie für den angegeben Zeichensatz existiert.
    --
    -- Rückgabewert:
    -- Binary data: Text im angegebenen Zeichensatz
    local bom = ... or false
    if bom then
        error("[MM.toEncoding] bom flag is enabled but not supported")
    end
    return bse_encode_str(str, charset)
end

function MM.fromEncoding(charset, data)
    -- Konvertiert einen Text von einem anderen Zeichensatz zu UTF-8.
    --
    -- Parameter:
    -- String charset: Zeichensatz; Die Angabe erfolgt wie bei HTTP nach IANA.
    -- Binary data: Text im angegebenen Zeichensatz
    --
    -- Rückgabewert:
    -- String str: Text in UTF-8
    return bse_decode_stream(data, charset)
end

function MM.base64(data)
    -- Konvertiert Daten zu Base64.
    --
    -- Parameter:
    -- Binary data: Zu konvertierende Daten
    --
    -- Rückgabewert:
    -- String encoded: Base64-kodierte Daten
    return bse_base64_encode(data)
end

function MM.base64decode(encoded)
    -- Konvertiert Daten von Base64.
    --
    -- Parameter:
    -- Binary encoded: Base64-kodierte Daten
    --
    -- Rückgabewert:
    -- String data: konvertierte Daten
    return bse_base64_decode(encoded)
end

function MM.sha512(data)
    -- Berechnet einen SHA512-, SHA256-, SHA1- oder MD5-Hashwert.
    --
    -- Parameter:
    -- Binary data: Daten, über die der Hashwert berechnet werden soll.
    --
    -- Rückgabewert:
    -- String digest: Hashwert als hexidezimaler String
    return bse_sha512(data)
end

function MM.sha256(data)
    -- Berechnet einen SHA512-, SHA256-, SHA1- oder MD5-Hashwert.
    --
    -- Parameter:
    -- Binary data: Daten, über die der Hashwert berechnet werden soll.
    --
    -- Rückgabewert:
    -- String digest: Hashwert als hexidezimaler String
    return bse_sha256(data)
end

function MM.sha1(data)
    -- Berechnet einen SHA512-, SHA256-, SHA1- oder MD5-Hashwert.
    --
    -- Parameter:
    -- Binary data: Daten, über die der Hashwert berechnet werden soll.
    --
    -- Rückgabewert:
    -- String digest: Hashwert als hexidezimaler String
    return bse_sha1(data)
end

function MM.md5(data)
    -- Berechnet einen SHA512-, SHA256-, SHA1- oder MD5-Hashwert.
    --
    -- Parameter:
    -- Binary data: Daten, über die der Hashwert berechnet werden soll.
    --
    -- Rückgabewert:
    -- String digest: Hashwert als hexidezimaler String
    return bse_md5(data)
end

function MM.hmac512(key, data)
    -- Berechnet einen HMAC512-, HMAC384- oder HMAC256-Message-Authentication-Code.
    --
    -- Parameter:
    -- Binary key: HMAC-Schlüssel
    -- Binary data: Daten, über die der Message Authentication Code berechnet werden soll.
    --
    -- Rückgabewert:
    -- Binary digest: Message Authentication Code als binärer String
    return bse_hmac512(data, key)
end

function MM.hmac384(key, data)
    -- Berechnet einen HMAC512-, HMAC384- oder HMAC256-Message-Authentication-Code.
    --
    -- Parameter:
    -- Binary key: HMAC-Schlüssel
    -- Binary data: Daten, über die der Message Authentication Code berechnet werden soll.
    --
    -- Rückgabewert:
    -- Binary digest: Message Authentication Code als binärer String
    return bse_hmac384(data, key)
end

function MM.hmac256(key, data)
    -- Berechnet einen HMAC512-, HMAC384- oder HMAC256-Message-Authentication-Code.
    --
    -- Parameter:
    -- Binary key: HMAC-Schlüssel
    -- Binary data: Daten, über die der Message Authentication Code berechnet werden soll.
    --
    -- Rückgabewert:
    -- Binary digest: Message Authentication Code als binärer String
    return bse_hmac256(data, key)
end

function MM.time()
    -- Gibt die aktuelle Uhrzeit zurück. Im Gegensatz zum Aufruf os.time() enthält der Rückgabewert auch Millisekunden
    -- als Nachkommestellen.
    --
    -- Rückgabewert:
    -- Number timestamp: Aktuelle Uhrzeit in Form eines POSIX-Zeitstempels.
    return bse_time()
end

function MM.sleep(seconds)
    -- Unterbricht die Ausführung des Skripts für ein paar Sekunden.
    --
    -- Parameter:
    -- Number seconds: Anzahl der Sekunden
    bse_sleep(seconds)
end

function MM.printStatus(...)
    -- Diese Funktion arbeitet ähnlich zur Lua-Funktion print: Die Parameter werden mittels der Lua-Funktion tostring
    -- zu einem String konvertiert und im Protokoll-Fenster von MoneyMoney angezeigt. Zusätzlich wird der String als
    -- Statusmeldung in der GUI angezeigt.
    print(...)
end

--[[
--
--    Definition: Connection
--    ----------------------
--
--    - Factory method to create a connection object
--]]

function Connection()
    return bse_connection()
end

function JSON(text)
    return bse_json(text)
end
