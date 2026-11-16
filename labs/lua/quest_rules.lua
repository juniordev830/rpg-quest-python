-- Independent quest-rule prototype for evaluating RPG mission rewards.
local M = {}

--- Compute a quest reward without mutating its inputs.
--- Returns nil and an error for invalid requests.
function M.reward(level, monsters, boss)
    if type(level) ~= "number" or level % 1 ~= 0 or level < 1 or level > 100 then
        return nil, "level must be an integer from 1 to 100"
    end
    if type(monsters) ~= "number" or monsters % 1 ~= 0 or monsters < 0 then
        return nil, "monsters must be a nonnegative integer"
    end
    if type(boss) ~= "boolean" then
        return nil, "boss must be boolean"
    end
    local experience = monsters * (10 + 2 * level)
    if boss then experience = experience + 50 * level end
    return { experience = experience, gold = monsters * 3 + (boss and level * 5 or 0) }
end

return M
