Test {description = "JSON utility tests"}

local jsonText = '{"key": "value"}'
local json_parser = JSON(jsonText)
local json = json_parser:dictionary()
assert(json["key"] == "value")
