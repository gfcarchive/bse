Test { description = "Testing Connection utility function" }

local url = "https://postman-echo.com/get?k=v"
local conn = Connection()
local jsonText, charset, mimeType, filename, headers = conn:request("GET", url)
local json = JSON(jsonText):dictionary()
assert(json["args"]["k"] == "v")
assert(charset == "UTF-8")
assert(mimeType == "application/json")
assert(filename == "")
assert(tonumber(headers["Content-Length"]) > 0)
