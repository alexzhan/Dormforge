def get_namedomain_by_id(db, client, userid):
    namedomain = client.hmget('u:' + userid, ['name', 'domain'])
    if namedomain:
        return namedomain
    else:
        userinfo = db.get("select name,domain from fd_People where id = %s", userid)
        client.hmset('u:' + userid, {"name":userinfo.name, "domain":userinfo.domain})
        return [userinfo.name, userinfo.domain]

def get_domain_by_name(db, client, username):
    domain = client.hmget("u:name:%s" % username, ["domain",])
    if domain[0]:
        return domain[0]
    else:
        domainid = db.get("select id,domain from fd_People where name = %s", username)
        if domainid:
            client.hmset("u:name:%s" % username, {"domain":domainid.domain, "id":domainid.id})
            return domainid.domain
    return None

def get_id_by_name(db, client, username):
    user_id = client.hmget("u:name:%s" % username, ["id",])
    if user_id[0]:
        return user_id[0]
    else:
        domainid = db.get("select id,domain from fd_People where name = %s", username)
        if domainid:
            client.hmset("u:name:%s" % username, {"domain":domainid.domain, "id":domainid.id})
            return domainid.id
    return None
