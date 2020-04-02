Test { description = "Testing Connection utility function" }

local echo_url = "http://echo.jsontest.com/key/value/k/v"
local conn = Connection()
local jsonText, charset, mimeType, filename, headers = conn:request("GET", echo_url)
local json = JSON(jsonText):dictionary()
assert(json["k"] == "v")
assert(charset == "ASCII")
assert(mimeType == "application/json")
assert(filename == "")
assert(headers["Content-Length"] == "" .. #jsonText)
