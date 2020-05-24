Test {description = "JSON utility tests"}

local jsonText = '{"key": "value"}'
local json_parser = JSON(jsonText)
local json = json_parser:dictionary()
assert(json["key"] == "value")

json["key"] = "another value"
jsonText = json_parser:set(json):json()
assert(jsonText == '{"key": "another value"}')

json_parser = JSON("")
json = json_parser:dictionary()
assert(python.builtins.len(json) == 0)
