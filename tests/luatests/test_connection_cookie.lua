Test { description = "Testing Connection Cookies" }

local url = "https://httpbin.org/cookies/set/CookieName/CookieValue"

local parameters = {}
local headers = {}
headers["accept"] = "application/json"

local conn = Connection()
jsonText = conn:request("GET", url, parameters, nil, headers)
local json = JSON(jsonText):dictionary()
assert(json["cookies"]["CookieName"] == "CookieValue")
local cookies = conn:getCookies()
assert(cookies["CookieName"] == "CookieValue")

conn:request("GET", '/cookies', parameters, nil, headers)
local cookies = conn:getCookies()
assert(cookies["CookieName"] == "CookieValue")
