Test { description = "Testing POST HTTP requests" }

local url = "https://postman-echo.com/post"

local parameters = {}
parameters["title"] = ""
parameters["body"] = "bar"
parameters["userId"] = 1

local headers = {}

-- needed as the endpoint returns other HTTP codes apart from 200
-- headers["Accept"] = "application/json"

local conn = Connection()
conn:setCookie("SESSION=foobar; path=/")
local jsonText = conn:request("POST", url, parameters, nil, headers)

local json = JSON(jsonText):dictionary()

assert(json["form"]["title"] == "")
assert(json["form"]["body"] == "bar")
assert(json["form"]["userId"] == "1")


local urlParameters = {}
for key, value in pairs(parameters) do
    if value == nil or value == "" then
      table.insert(urlParameters, MM.urlencode(key))
    else
      table.insert(urlParameters, MM.urlencode(key) .. "=" .. MM.urlencode(value))
    end
end

local encodedUrl = ""
for _, value in pairs(urlParameters) do
    if #encodedUrl == 0 then
        encodedUrl = encodedUrl .. value
    else
        encodedUrl = encodedUrl .. "&" .. value
    end
end

print(encodedUrl)
jsonText = conn:request("POST", url, encodedUrl, nil, headers)

json = JSON(jsonText):dictionary()

assert(json["form"]["title"] == "")
assert(json["form"]["body"] == "bar")
assert(json["form"]["userId"] == "1")

