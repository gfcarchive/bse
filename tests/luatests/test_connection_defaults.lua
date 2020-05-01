Test { description = "Testing default data in Connection" }

local conn = Connection()
assert(string.find(conn.useragent, "requests") ~= nil)

assert(conn.language == "en-US")
