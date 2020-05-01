Test { description = "Testing POST HTTP requests" }

local url = "https://postman-echo.com/post"

local parameters = {}
parameters["title"] = "title"

local headers = {}

local conn = Connection()

local jsonText = conn:request("POST", url, parameters, nil, headers)
local json = JSON(jsonText):dictionary()
assert(json["form"]["title"] == "title")

jsonText = conn:request("POST", "/post", parameters, nil, headers)
json = JSON(jsonText):dictionary()
assert(json["form"]["title"] == "title")
