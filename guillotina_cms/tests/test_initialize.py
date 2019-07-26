async def test_initialize(cms_requester):
    async with cms_requester as requester:
        resp, status = await requester("GET", "/db/guillotina/@types/Container")
        assert "guillotina_cms.interfaces.tiles.ITiles" in resp["properties"]
        assert "guillotina_cms.interfaces.base.ICMSBehavior" in resp["properties"]
        assert "guillotina.behaviors.dublincore.IDublinCore" in resp["properties"]