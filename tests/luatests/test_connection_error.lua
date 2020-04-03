Test { description = "Testing Response errors in the Connection function" }


local echo_url = "http://google.com/aaaa" -- Google will return a 404 status code
local conn = Connection()
if pcall(function() conn:request("GET", echo_url) end) then
    assert(false, "conn:request did not raise an error on status code != 200 and no Accept header")
end

local header = {}
header["Accept"] = "application/json"
local content = conn:request("GET", echo_url, nil, nil, header)
assert(#content > 0)
