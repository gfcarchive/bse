Test { description = "Testing POST HTTP requests" }

local url = "https://jsonplaceholder.typicode.com/posts"

local parameters = {}
parameters["title"] = ""
parameters["body"] = "bar"
parameters["userId"] = 1

local headers = {}
headers["Accept"] = "application/json"

local conn = Connection()
local jsonText = conn:request("POST", url, parameters, nil, headers)

local json = JSON(jsonText):dictionary()

assert(json["title"] == "")
assert(json["body"] == "bar")
assert(json["userId"] == "1")
