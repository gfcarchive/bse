WebBanking {
  version = 1.0,
  url = "http://localhost",
  services = {"Service Name"},
  description = "this is a description",
}

local jsonText = '{"key": "value"}'
local json_parser = JSON(jsonText)
local json = json_parser:dictionary()
assert(json["key"] == "value")
