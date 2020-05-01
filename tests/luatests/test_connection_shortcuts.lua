Test { description = "Testing Method shortcuts" }

local url = "https://postman-echo.com/get?k=v"
local conn = Connection()
local jsonText, charset, mimeType, filename, headers = conn:get(url)
local json = JSON(jsonText):dictionary()
assert(json["args"]["k"] == "v")
assert(charset == "UTF-8")
assert(mimeType == "application/json")
assert(filename == "")
assert(tonumber(headers["Content-Length"]) > 0)


local url = "https://postman-echo.com/post"
local parameters = {}
parameters["title"] = ""
local headers = {}
local conn = Connection()
local jsonText = conn:post(url, parameters, nil)
local json = JSON(jsonText):dictionary()
assert(json["form"]["title"] == "")
