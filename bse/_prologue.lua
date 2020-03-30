function WebBanking (arg)
    -- sets global variables
    -- these fields are mandatory but lupa erros are very confusing, so I will manage them in the bse.lua module
    version = arg.version
    url = arg.url
    services = arg.services
    description = arg.description
end
